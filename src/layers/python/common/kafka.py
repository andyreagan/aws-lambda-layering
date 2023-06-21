from confluent_kafka import Consumer
import logging

from aws_lambda_powertools import Logger

logger = Logger(service="AWS Lambda Layering Test")

logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

c = Consumer({
    'bootstrap.servers': 'mybroker',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mytopic'])


def get_message():
    msg = c.poll(1.0)

    if msg is None:
        logger.info("No message")
    elif msg.error():
        logger.info("Consumer error: {}".format(msg.error()))
    else:
        logger.info('Received message: {}'.format(msg.value().decode('utf-8')))

# c.close()