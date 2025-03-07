import threading
import time


print_lock = threading.Lock()


def thread_counter(id: int, max: int, delay: float):
    for i in range(1, max + 1):
        with print_lock:
            print(f"Thread-{id}: Count {i}")
        time.sleep(delay)


def main():

    threads = [
        threading.Thread(target=thread_counter, args=(1, 10, 0.7)),
        threading.Thread(target=thread_counter, args=(2, 15, 0.5)),
        threading.Thread(target=thread_counter, args=(3, 20, 0.3)),
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("All completed!")


if __name__ == "__main__":
    main()
