from messaging.settings import RabbitMQExchange, RabbitMQExchangeType


def main():
    # sync publisher example
    from messaging.publisher.sync_publisher import SyncPublisher
    publisher = SyncPublisher()
    publisher.publish(
        message="Published by sync publisher",
        exchange=RabbitMQExchange.TEST_EXCHANGE,
        exchange_type=RabbitMQExchangeType.FANOUT,
    )

    # async publisher example
    import asyncio
    from messaging.publisher.async_publisher import AsyncPublisher
    asyncio.run(
        AsyncPublisher().publish(
            message="Published by async publisher",
            exchange=RabbitMQExchange.TEST_EXCHANGE,
            exchange_type=RabbitMQExchangeType.FANOUT,
        )
    )

if __name__ == "__main__":
    main()
