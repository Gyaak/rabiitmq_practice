import aio_pika
from messaging.publisher.interface import IPublisher
from messaging.settings import rabbitmq_settings, RabbitMQExchange, RabbitMQExchangeType

class AsyncPublisher(IPublisher):
    def __init__(self):
        self.host = rabbitmq_settings.RABBITMQ_HOST
        self.port = rabbitmq_settings.RABBITMQ_PORT
        self.user = rabbitmq_settings.RABBITMQ_USER
        self.password = rabbitmq_settings.RABBITMQ_PASSWORD
        self.vhost = rabbitmq_settings.RABBITMQ_VHOST

        self.__connection = None
        self.__channel = None

    async def ensure_connection(self):
        if self.__connection is None:
            self.__connection = await aio_pika.connect_robust(
                host=self.host,
                port=self.port,
                login=self.user,
                password=self.password,
                virtualhost=self.vhost,
            )
        if self.__channel is None:
            self.__channel = await self.__connection.channel()

        return self.__channel

    async def publish(
        self, message: str, exchange: RabbitMQExchange, exchange_type: RabbitMQExchangeType,
    ):
        channel = await self.ensure_connection()
        exchange = await channel.declare_exchange(name=exchange.value, type=exchange_type.value, durable=True)
        await exchange.publish(aio_pika.Message(body=message.encode()), routing_key=exchange_type.value)