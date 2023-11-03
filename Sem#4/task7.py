import threading
import time
import random
from multiprocessing import Process
import asyncio

def rand_arr(num):
    """
    Creates a list with random nums. Quontity of nums is entered in params.
    :param num: int
    :return: [int]
    """
    rand_arr = [random.randint(1, 101) for _ in range(num)]
    return rand_arr

def summarize_arr(arr: list[int])-> int:
    """Summarizes list of ints"""
    return sum(arr)

def time_deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения: {end - start:.5f} сек')
    return wrapper

# @time_deco
# def thread():
#     threads = []
#     for i in range(3):
#         rand_list = rand_arr(1000_000)
#         t = threading.Thread(target=summarize_arr, args=[rand_list], daemon=True)
#         threads.append(t)
#         t.start()
#
#     for thread in threads:
#         thread.join()

@time_deco
def procs():
    processes = []
    for i in range(5):
        rand_list = rand_arr(1000_000)
        t = Process(target=summarize_arr, args=[rand_list], daemon=True)
        processes.append(t)
        t.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    procs()

