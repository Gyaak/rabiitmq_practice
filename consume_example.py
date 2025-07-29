
from messaging.settings import RabbitMQQueue

def main():
    # sync consumer example
    from messaging.consumer.sync_consumer import SyncConsumer
    consumer = SyncConsumer()
    byte_message = consumer.consume(queue=RabbitMQQueue.TEST_QUEUE)
    print(f"sync consumer received message: {byte_message}")

    # async consumer example
    import asyncio
    from messaging.consumer.async_consumer import AsyncConsumer
    async def async_main():
        byte_message = await AsyncConsumer().consume(queue=RabbitMQQueue.TEST_QUEUE)
        print(f"async consumer received message: {byte_message}")
    asyncio.run(async_main())

if __name__ == "__main__":
    main()