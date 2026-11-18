"""HTTP server for the customer order status page (Story 1.1).

Run: python -m app.order_system --port 8000
Stdlib only: http.server + ThreadPoolExecutor for the backend timeout.
"""

import argparse
import html
import logging
import re
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

from .store import OrderStore

CUSTOMER_HEADER = "X-Customer-Id"  # stand-in for real authentication
BACKEND_TIMEOUT_SECONDS = 2.0
UNAVAILABLE_MESSAGE = "Live order status is temporarily unavailable. Please try again in a few minutes."
NOT_FOUND_MESSAGE = "Order not found"
ORDER_ROUTE = re.compile(r"^/orders/(#?\d+)$")

logger = logging.getLogger(__name__)
_backend_pool = ThreadPoolExecutor(max_workers=16, thread_name_prefix="order-backend")


class BackendFailure(Exception):
    """The order system timed out or errored."""


class OrderStatusService:
    def __init__(self, store: OrderStore, timeout: float = BACKEND_TIMEOUT_SECONDS):
        self.store = store
        self.timeout = timeout

    def fetch_order(self, order_id: str):
        # Run the read in a pool so a slow backend cannot hold the request past the timeout.
        future = _backend_pool.submit(self.store.get_order, order_id)
        try:
            return future.result(timeout=self.timeout)
        except FuturesTimeout as exc:
            raise BackendFailure("order system timed out") from exc
        except Exception as exc:
            logger.error("order backend read failed for order %s: %r", order_id, exc)
            raise BackendFailure("order system error") from exc


def _page(title: str, body: str) -> str:
    return (
        "<!doctype html><html><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(title)}</title></head><body>{body}</body></html>"
    )


def _render_order(order) -> str:
    return _page(
        f"Order #{order.order_id}",
        f"<h1>Order #{html.escape(order.order_id)}</h1>"
        f"<p>Current status: <span id=\"order-status\">{html.escape(order.status)}</span></p>"
        f"<p>Last status change: <time id=\"status-changed-at\">"
        f"{order.formatted_status_changed_at()}</time></p>",
    )


def _render_not_found() -> str:
    return _page(
        NOT_FOUND_MESSAGE,
        f"<h1>{NOT_FOUND_MESSAGE}</h1>"
        "<p>We could not find that order. <a href=\"/orders\">Back to my orders</a></p>",
    )


def _render_unavailable() -> str:
    return _page(
        "Order status unavailable",
        f"<h1>Order status unavailable</h1><p>{UNAVAILABLE_MESSAGE}</p>",
    )


def handle_order_view(service: OrderStatusService, customer_id: str | None, path: str):
    """Return (status, html_body) for a GET to /orders/{id} as the given customer."""
    match = ORDER_ROUTE.match(urlsplit(path).path)
    if not match:
        return HTTPStatus.NOT_FOUND, _page("Page not found", "<h1>Page not found</h1>")
    if not customer_id:
        return HTTPStatus.UNAUTHORIZED, _page(
            "Sign in required", "<h1>Sign in required</h1><p>Please sign in to view your orders.</p>"
        )

    order_id = match.group(1).lstrip("#")
    try:
        order = service.fetch_order(order_id)
    except BackendFailure:
        return HTTPStatus.SERVICE_UNAVAILABLE, _render_unavailable()

    # Missing and other-customer orders get the same response so existence is not disclosed (FR5).
    if order is None or order.customer_id != customer_id:
        return HTTPStatus.NOT_FOUND, _render_not_found()
    return HTTPStatus.OK, _render_order(order)


def make_handler(service: OrderStatusService):
    class OrderRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            status, body = handle_order_view(service, self.headers.get(CUSTOMER_HEADER), self.path)
            payload = body.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, format, *args):
            logger.debug("%s - %s", self.address_string(), format % args)

    return OrderRequestHandler


def create_server(store: OrderStore | None = None, host: str = "127.0.0.1", port: int = 8000,
                  timeout: float = BACKEND_TIMEOUT_SECONDS) -> ThreadingHTTPServer:
    service = OrderStatusService(store or OrderStore(), timeout)
    return ThreadingHTTPServer((host, port), make_handler(service))


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Customer order status server (Story 1.1)")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO)
    server = create_server(host=args.host, port=args.port)
    print(f"Serving on http://{args.host}:{server.server_address[1]} (send header {CUSTOMER_HEADER}: cust-a)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
