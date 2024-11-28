from pydantic import BaseModel


class WazuhAlertSchema(BaseModel):
    alert_id: str
    level: int
    description: str

