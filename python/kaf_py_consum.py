from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'test1',
    bootstrap_servers=['172.30.1.129:32100'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,

    value_deserializer=lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms=10000
)

print('[begin] get consumer list')

for message in consumer:
    print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" % ( message.topic, message.partition, message.offset, message.key, message.value ))

print('[end] get consumer list')
