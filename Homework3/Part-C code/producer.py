ng=utf-8

from kafka import KafkaProducer
import time
import random
import multiprocessing


def mainloop(id, tid):
    print ("fdf")
    random_section = 15
    cancel_id = -1
    producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
    while True:
        id.value = id.value + 1
        if (id.value % random_section == 0):
            random_section = random.randrange(15, 40)
            cancel_id = id.value + random.randrange(0, 20)

        money = random.randrange(15, 4000)
        if (id.value != cancel_id):
            msg = "collector %d send request id %d, money %d, " % (tid, id.value, money)
            sendmsg = "%d,%d" % (id.value, money)
            producer.send('request', sendmsg.encode('utf-8'))
        else:
            msg = "collector %d send cancel id %d, " % (tid, id.value)
            sendmsg = "%d" % id.value
            producer.send('cancel', sendmsg.encode('utf-8'))

        print(msg)
        time.sleep(1)
    producer.close()

if __name__ == "__main__":
    id = multiprocessing.Value('i', 0)
    pool = multiprocessing.Pool(processes=4)

    for i in xrange(4):
        print("i")
        pool.apply_async(mainloop, (id, i,))

    pool.close()
    pool.join()