from abc import ABCMeta, abstractmethod
from messaging.settings import RabbitMQExchange, RabbitMQExchangeType

class IPublisher(metaclass=ABCMeta):
    @abstractmethod
    def publish(
        self,
        message: str,
        exchange: RabbitMQExchange,
        exchange_type: RabbitMQExchangeType,
    ):
        pass
