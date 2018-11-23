from kafka import KafkaConsumer

consumer = KafkaConsumer('request', group_id='my_group', bootstrap_servers=['127.0.0.1:9092'])  

for message in consumer:
	list  = message.value.split(',');
	print("%s:%d:%d: key=%s id=%s money=%s" % (message.topic, message.partition, message.offset, message.key, list[0], list[1]))


