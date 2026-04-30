from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..routers.orders import router
from ..dependencies.database import get_db
from unittest.mock import MagicMock
from datetime import datetime

app = FastAPI()
app.include_router(router)
client = TestClient(app)

mock = MagicMock()

def override_get_db():
    return mock

app.dependency_overrides[get_db] = override_get_db

testOrder = [{"id": 1,"customer_id": 1,"tracking_number": "TEST-123","order_type": "delivery","order_status": "Testing","total_price": 0,"order_date": datetime.now()}]

def test_read_all_orders():
    mock.query.return_value.all.return_value = testOrder
    response = client.get("/orders")
    assert response.status_code == 200
    assert (response.json()[0]["tracking_number"] == "TEST-123" )