from queue import Queue
import random
import time

queue = Queue(maxsize=10)

def generate_request():
    request = {"id": random.randint(1, 999),
               "type": random.choice(["Type A", "Type B", "Type C"]),
               "priority": random.randint(1, 5)}
    if queue.full():
        print("Queue is full")
    else:
        queue.put(request)
        return print(f"Request {request} has been added to queue")


def process_request():
    if not queue.empty():
        el = queue.get()
        return print(f"Request{el} have been proceed")
    else:
        return print("Queue is empty")


def main():
    while True:
        for _ in range(random.randint(1, 4)):
            generate_request()
        for _ in range(random.randint(1, 2)):
            process_request()
        time.sleep(random.randint(1, 4))
        print(f"Current queue: {list(queue.queue)}")


if __name__ == "__main__":
    main()
