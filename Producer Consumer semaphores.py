import threading
import time
import random
from datetime import datetime

# Shared buffer
buffer = []
buffer_size = 5

# Semaphores
empty = threading.Semaphore(buffer_size)  # initially has n empty slots
full = threading.Semaphore(0)  # initially buffer is empty
mutex = threading.Lock()  # mutex for critical section, initial value is unlocked

# Producer function
def producer():
    global buffer
    while True:
        item = random.randint(1, 10)
        timestamp = datetime.now().strftime("%H:%M:%S")
        empty.acquire()  # wait for empty slot
        mutex.acquire()  # enter critical section
        buffer.append(item)
        print(f"Produced: {item} at position {len(buffer)} at {timestamp}")
        print(f"Current buffer: {buffer}")
        mutex.release()  # leave critical section
        full.release()  # signal an item is produced
        time.sleep(random.uniform(0.1, 0.5))  # Simulating production time

# Consumer function
def consumer():
    global buffer
    while True:
        full.acquire()  # wait for available item
        timestamp = datetime.now().strftime("%H:%M:%S")
        mutex.acquire()  # enter critical section
        item = buffer.pop(0)
        print(f"Consumed: {item} from position 1 at {timestamp}")
        print(f"Current buffer: {buffer}")
        mutex.release()  # leave critical section
        empty.release()  # signal an empty slot
        time.sleep(random.uniform(0.1, 0.5))  # Simulating consumption time

# Threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()








