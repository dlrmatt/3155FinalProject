from pydantic import BaseModel

class SalesData(BaseModel):
    total_revenue: float
