from kafka import KafkaProducer
import json
from json import dumps
import time

producer = KafkaProducer(
    acks=0,
    compression_type='gzip',
    bootstrap_servers=['172.30.1.129:32100'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

start = time.time()

with open("C:/Users/slinfo/Desktop/seoul_shops5_entertainment.json", 'r', encoding='utf-8') as f:
    for i in f:
        data = i
        producer.send('test1', value=json.loads(data))
        producer.flush()
