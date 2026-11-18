# Order Status App (Story 1.1)

Stdlib-only Python server (`http.server`). Tests use pytest.

## Setup
```
cd order-tracking
python -m pip install -r app/requirements.txt
```

## Run the server
```
cd order-tracking
python -m app.order_system --port 8000
curl -H "X-Customer-Id: cust-a" http://127.0.0.1:8000/orders/1001
```
Customer identity is the `X-Customer-Id` header (stand-in for auth). Seeded: `1001` (cust-a, Shipped), `1002` (cust-b, Packed).

Status changes: `OrderStore.update_status(order_id, status, changed_at)` (used in tests). The server's store is in-memory and not reachable from another process.

## Run tests
```
cd order-tracking
python -m pytest app/tests -v
```
