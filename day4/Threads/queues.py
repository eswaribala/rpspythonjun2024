import multiprocessing


def process1_send_function(queue, events):
    for event in events:
        queue.put(event)
        print(f"Event Sent: {event}")


def process2_recv_function(queue):
    while True:
        event = queue.get()
        if event == "eod":
            print("Event Received: End of Day")
            return
        print(f"Event Received: {event}")


def run():
    events = ["get up", "brush your teeth", "shower", "work", "eod"]
    queue = multiprocessing.Queue()
    process_1 = multiprocessing.Process(target=process1_send_function, args=(queue, events))
    process_2 = multiprocessing.Process(target=process2_recv_function, args=(queue,))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()


if __name__ == "__main__":
    run()