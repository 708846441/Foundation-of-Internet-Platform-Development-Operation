from kafka import KafkaConsumer

consumer = KafkaConsumer('cancel', group_id='my_group', bootstrap_servers=['127.0.0.1:9092'])  

for message in consumer:
	print("%s:%d:%d: key=%s id=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

