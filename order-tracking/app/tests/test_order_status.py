"""Story 1.1 acceptance tests: TC-1.1-01 .. TC-1.1-05 (run against a live local HTTP server)."""

import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

import pytest

from app.order_system import NOT_FOUND_MESSAGE, UNAVAILABLE_MESSAGE, create_server
from app.store import OrderStore

CUSTOMER_A = "cust-a"
CUSTOMER_B = "cust-b"


@pytest.fixture
def store():
    return OrderStore()


@pytest.fixture
def base_url(store):
    server = create_server(store=store, port=0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()
    server.server_close()


def get(base_url, path, customer=CUSTOMER_A):
    """Return (status, body, elapsed_seconds) for a GET, including 4xx/5xx responses."""
    headers = {"X-Customer-Id": customer} if customer else {}
    request = urllib.request.Request(base_url + path, headers=headers)
    started = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            status, body = response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        status, body = error.code, error.read().decode("utf-8")
    return status, body, time.monotonic() - started


def test_tc_1_1_01_customer_sees_own_order_live_status(base_url):
    """TC-1.1-01 (AC1): logged-in customer opens own order #1001 and sees Shipped at 10:00:00Z in under 2s."""
    status, body, elapsed = get(base_url, "/orders/1001")

    assert status == 200
    assert "Order #1001" in body
    assert '<span id="order-status">Shipped</span>' in body
    assert '<time id="status-changed-at">2026-11-17T10:00:00Z</time>' in body
    assert elapsed < 2.0


def test_tc_1_1_02_status_change_shown_on_next_view(base_url, store):
    """TC-1.1-02 (AC2): Packed -> Shipped at 10:05:00Z is shown on the next view (no cache, so well within 5 min)."""
    store.update_status("1001", "Packed", datetime(2026, 11, 17, 10, 0, tzinfo=timezone.utc))
    _, before, _ = get(base_url, "/orders/1001")
    assert '<span id="order-status">Packed</span>' in before

    store.update_status("1001", "Shipped", datetime(2026, 11, 17, 10, 5, tzinfo=timezone.utc))
    status, after, _ = get(base_url, "/orders/1001")

    assert status == 200
    assert '<span id="order-status">Shipped</span>' in after
    assert '<time id="status-changed-at">2026-11-17T10:05:00Z</time>' in after


def test_tc_1_1_03_other_customers_order_is_refused(base_url):
    """TC-1.1-03 (AC3): Customer A requesting Customer B's order #1002 gets 404 and no order data."""
    status, body, _ = get(base_url, "/orders/1002", customer=CUSTOMER_A)

    assert status == 404
    assert NOT_FOUND_MESSAGE in body
    assert "Packed" not in body
    assert "2026-11-17T09:00:00Z" not in body
    assert "1002" not in body

    # Control: the owner can still see the order.
    owner_status, owner_body, _ = get(base_url, "/orders/1002", customer=CUSTOMER_B)
    assert owner_status == 200
    assert "Packed" in owner_body


def test_tc_1_1_04_nonexistent_order_shows_not_found(base_url):
    """TC-1.1-04 (AC4): order #9999 shows the 'Order not found' empty state with a link back to orders."""
    status, body, elapsed = get(base_url, "/orders/9999")

    assert status == 404
    assert NOT_FOUND_MESSAGE in body
    assert 'href="/orders"' in body
    assert elapsed < 2.0


@pytest.mark.parametrize("failure", ["unavailable", "slow"])
def test_tc_1_1_05_backend_failure_shows_retry_message(base_url, store, failure):
    """TC-1.1-05 (AC5): backend unavailable or slow (>2s) returns the retry message, not a stack trace or stale status."""
    if failure == "unavailable":
        store.set_available(False)
    else:
        store.set_latency(3.0)

    status, body, elapsed = get(base_url, "/orders/1001")

    assert status == 503
    assert UNAVAILABLE_MESSAGE in body
    assert "Shipped" not in body
    assert "Traceback" not in body
    assert elapsed < 2.5


def test_unauthenticated_request_is_refused(base_url):
    """Supporting check: a request without a customer identity is not given any order data."""
    status, body, _ = get(base_url, "/orders/1001", customer=None)

    assert status == 401
    assert "Shipped" not in body
