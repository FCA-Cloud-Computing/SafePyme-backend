from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    RedisDsn,
    PostgresDsn,
    AmqpDsn,
    Field,
)


class Settings(BaseSettings):
    wazuh_url: str
    wazuh_key: str
    thehive_url: str
    thehive_key: str
    elasticsearch_host: str
    elasticsearch_port: int
    aws_region: str = "us-east-1"

    class Config:
        env_file = ".env"


settings = Settings()

