"Utils for python develoment"
# Author: Argha Sen
# Start Date : 20th December 2014
import time


def timed_call(func, *args):
    "Call function with args, return time and result"
    t0 = time.clock()
    result = func(*args)
    t1 = time.clock()
    return t1 - t0, result

def timed_calls( n, func, *args):
    " call func n times with args, and print stats"
    times =[timed_call(func, *args)[0] for _ in range(n)]
    return max(times), average(times), max(times)