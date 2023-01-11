#coding=utf-8
import time
from functools import wraps


def my_wrapper(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print('starting:{}'.format(start_time))
        result = fun(*args, **kwargs)
        end_time = time.time()
        print('ending:{}'.format(end_time))
        print(fun.__name__, end_time - start_time)
        return result
    return wrapper
@my_wrapper
def run_my_wrapper():
    value = 0
    for i in range(100):
        print(i)
        value = i
    time.sleep(3)
    return value
# print(run_my_wrapper())
