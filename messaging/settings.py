import pydantic_settings
from enum import Enum

class Settings(pydantic_settings.BaseSettings):
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"
    RABBITMQ_VHOST: str = "/"

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

rabbitmq_settings = Settings()

class RabbitMQExchange(Enum):
    TEST_EXCHANGE = "test.exchange"

class RabbitMQExchangeType(Enum):
    FANOUT = "fanout"
    DIRECT = "direct"
    TOPIC = "topic"
    HEADERS = "headers"

class RabbitMQQueue(Enum):
    TEST_QUEUE = "test.queue"