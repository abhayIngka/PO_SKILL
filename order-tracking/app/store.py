"""In-memory order store standing in for the order system (Story 1.1)."""

import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone


class BackendUnavailable(Exception):
    """Raised when the order system cannot be read."""


@dataclass(frozen=True)
class Order:
    order_id: str
    customer_id: str
    status: str
    status_changed_at: datetime  # always UTC

    def formatted_status_changed_at(self) -> str:
        return self.status_changed_at.strftime("%Y-%m-%dT%H:%M:%SZ")


def _utc(year, month, day, hour, minute, second=0) -> datetime:
    return datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)


def seed_orders() -> list[Order]:
    return [
        Order("1001", "cust-a", "Shipped", _utc(2026, 11, 17, 10, 0)),
        Order("1002", "cust-b", "Packed", _utc(2026, 11, 17, 9, 0)),
    ]


class OrderStore:
    def __init__(self, orders=None):
        self._lock = threading.Lock()
        self._orders = {o.order_id: o for o in (orders if orders is not None else seed_orders())}
        # Fault-injection knobs used by tests and local demos to simulate an unavailable or slow order system.
        self._available = True
        self._latency_seconds = 0.0

    def get_order(self, order_id: str) -> Order | None:
        if self._latency_seconds:
            time.sleep(self._latency_seconds)
        with self._lock:
            if not self._available:
                raise BackendUnavailable("order system is unavailable")
            return self._orders.get(order_id)

    def update_status(self, order_id: str, status: str, changed_at: datetime) -> None:
        with self._lock:
            order = self._orders[order_id]
            self._orders[order_id] = Order(order.order_id, order.customer_id, status, changed_at)

    def set_available(self, available: bool) -> None:
        with self._lock:
            self._available = available

    def set_latency(self, seconds: float) -> None:
        self._latency_seconds = seconds
