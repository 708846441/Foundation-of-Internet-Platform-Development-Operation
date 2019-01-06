from kafka import KafkaConsumer
from kafka.structs import TopicPartition
import time

consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092'])
consumer.subscribe(topics=('test'))
consumer.topics()
consumer.pause(TopicPartition(topic=u'test', partition=0))  # pause执行后，consumer不能读取，直到调用resume后恢复。
num = 0
while True:
    print(num)
    print(consumer.paused())   #获取当前挂起的消费者
    msg = consumer.poll(timeout_ms=5)
    print(msg)
    time.sleep(2)
    num = num + 1
    if num == 10:
        print("resume...")
        consumer.resume(TopicPartition(topic='test', partition=0))
        print("resume......")

