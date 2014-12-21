"Utils for python develoment"
# Author: Argha Sen
# Start Date : 20th December 2014
import time
import numpy


def timed_call(func, *args):
    "Call function with args, return time and result"
    t0 = time.clock()
    result = func(*args)
    t1 = time.clock()
    return t1 - t0, result


def timed_calls(n, func, *args):
    " call func n times with args, and print stats \
    else run for n seconds "
    if isinstance(n, int):
        times = [timed_call(func, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timed_call(func, *args)[0])
    return max(times), numpy.mean(times), max(times)
