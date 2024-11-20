import threading
import time

# Locks (Mutex)
resource_lock = threading.Lock()
read_count_lock = threading.Lock()
read_count = 0

def reader(reader_id):
    global read_count
    read_count_lock.acquire()
    read_count += 1
    if read_count == 1:
        resource_lock.acquire()  # First reader locks the resource
    read_count_lock.release()

    # Reading
    print(f"Reader {reader_id} is reading.")
    time.sleep(1)
    print(f"Reader {reader_id} finished reading at {time.strftime('%H:%M:%S')}")

    read_count_lock.acquire()
    read_count -= 1
    if read_count == 0:
        resource_lock.release()  # Last reader unlocks the resource
    read_count_lock.release()

def writer(writer_id):
    resource_lock.acquire()

    # Writing
    print(f"Writer {writer_id} is writing.")
    time.sleep(1)
    print(f"Writer {writer_id} finished writing at {time.strftime('%H:%M:%S')}")

    resource_lock.release()

# Create threads
readers = [threading.Thread(target=reader, args=(i+1,)) for i in range(3)]
writers = [threading.Thread(target=writer, args=(i+1,)) for i in range(2)]

# Start threads
for t in readers + writers:
    t.start()

# Wait for threads to finish
for t in readers + writers:
    t.join()