import threading
import time
import random
from datetime import datetime

buffer = []
buffer_size = 5
mutex = threading.Lock()  # Unlocked originally (value 1)

# Producer function
def producer():
    global buffer
    while True:
        item = random.randint(1, 10)
        timestamp = datetime.now().strftime("%H:%M:%S")
        mutex.acquire()
        if len(buffer) < buffer_size:
            buffer.append(item)
            print(f"Produced: {item} at position {len(buffer)} at {timestamp}")
        else:
            print(f"Buffer full! Producer is waiting. Current buffer: {buffer}")
        print(f"Current buffer: {buffer}")
        mutex.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulating production time

# Consumer function
def consumer():
    global buffer
    while True:
        timestamp = datetime.now().strftime("%H:%M:%S")
        mutex.acquire()
        if buffer:
            item = buffer.pop(0)
            print(f"Consumed: {item} from position 1 at {timestamp}")
        else:
            print(f"Buffer empty! Consumer is waiting. Current buffer: {buffer}")
        print(f"Current buffer: {buffer}")
        mutex.release()
        time.sleep(random.uniform(0.1, 0.5))  # Simulating consumption time

# Threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
