from chatserver import RedisMemoryBroker
from chatserver import Chat

import os
import signal
import sys
import time


def signal_handler(sig, frame):
    print('Catch signal')
    sys.exit(0)


if __name__ == '__main__':
    outputString = "gunicorn -k \"geventwebsocket.gunicorn.workers.GeventWebSocketWorker\" -w 4 --bind 0:8000 chatserver"
    starttime = time.time()
    serverNumber = input("Put number how many clients you want to make: ")
    os.system(outputString)
    signal.signal(signal.SIGINT, signal_handler)

    while(1):
        print("1")
        time.sleep(60.0 - ((time.time() - starttime) % 20.0))
