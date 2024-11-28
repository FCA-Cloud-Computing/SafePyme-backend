class WazuhAlert:
    def __init__(self, alert_id: str, level: int, description: str):
        self.alert_id = alert_id
        self.level = level
        self.description = description
        