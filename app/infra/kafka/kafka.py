import json

from aiokafka import AIOKafkaProducer
from core.config import settings


class KafkaManager:
    def __init__(self, bootstrap_servers: str = settings.kafka_url):
        self.bootstrap_servers = bootstrap_servers
        self.producer = None

    async def start(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()

    async def send_message(self, topic: str, message: dict):
        if not self.producer:
            raise Exception("Kafka producer is not started")
        await self.producer.send(topic, json.dumps(message).encode('utf-8'))


async def get_kafka_service():
    kafka_service = KafkaManager()
    await kafka_service.start()
    try:
        yield kafka_service
    finally:
        await kafka_service.stop()
