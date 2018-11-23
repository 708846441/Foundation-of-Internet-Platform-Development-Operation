# ng=utf-8

from kafka import KafkaProducer
import time
import random
from multiprocessing import Process, Lock, Manager
from multiprocessing.sharedctypes import Value
import os


def mainloop(tid, lock):
    random_section = 15
    cancel_id = -1
    producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
    while True:
        with lock:
            id.value = id.value + 1
            this_id = id.value

        if (this_id % random_section == 0):
            random_section = random.randrange(15, 40)
            cancel_id = this_id + random.randrange(0, 20)

        money = random.randrange(15, 4000)
        if (this_id != cancel_id):
            msg = "collector %d send request id %d, money %d, " % (tid, this_id, money)
            sendmsg = "%d,%d" % (this_id, money)
            with lock:
                print(msg)
                producer.send('request', sendmsg.encode('utf-8'))
        else:
            msg = "collector %d send cancel id %d, " % (tid, this_id)
            sendmsg = "%d" % this_id
            with lock:
                print(msg)
                producer.send('cancel', sendmsg.encode('utf-8'))


        time.sleep(1)
    producer.close()


if __name__ == "__main__":
    threads = []

    lock = Lock()
    manager = Manager()
    id = manager.Value('tmp', 0)

    for ll in range(4):
        t = Process(target=mainloop, args=(ll, lock))
        t.daemon = True
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for j in range(len(threads)):
        threads[j].join()

    print 'All subprocesses finish Processing.'
