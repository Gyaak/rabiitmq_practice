import asyncio
import aio_pika

from messaging.consumer.interface import IConsumer
from messaging.settings import rabbitmq_settings, RabbitMQQueue


class AsyncConsumer(IConsumer):
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
    
    async def consume(self, queue: RabbitMQQueue)->bytes:
        channel = await self.ensure_connection()
        queue = await channel.get_queue(name=queue.value)
        try:
            message = await queue.get(timeout=10)
            if message:
                async with message.process():  # ack 자동 처리
                    return message.body
            else:
                return b""
        except (asyncio.TimeoutError, aio_pika.exceptions.QueueEmpty):
            return b""