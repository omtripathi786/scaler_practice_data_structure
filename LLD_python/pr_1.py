import time
import threading

start = time.perf_counter()


def do_something():
    print(f"Thread name {threading.current_thread().name} and id is {threading.get_ident()}")
    print('doing somthing..')
    time.sleep(1)
    print('done somethings..')


if __name__ == '__main__':
    print(f"Thread name {threading.current_thread().name} and id is {threading.get_ident()}")
    t1 = threading.Thread(target=do_something)
    t1.start()
    t2 = threading.Thread(target=do_something)
    t2.start()
    t3 = threading.Thread(target=do_something)
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    finish = time.perf_counter()
    print(f"\n Finished in {round(finish - start, 2)}")
