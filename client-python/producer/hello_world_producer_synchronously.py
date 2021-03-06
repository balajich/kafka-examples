import socket

from confluent_kafka import Producer

conf = {'bootstrap.servers': "broker-1:19092,broker-2:29092,broker-3:39092",
        'client.id': socket.gethostname()}
producer = Producer(conf)
producer.produce(topic='hello-world-topic', key=None, value="Hello World from Python")
producer.flush()  # can be used to make writes synchronous.
