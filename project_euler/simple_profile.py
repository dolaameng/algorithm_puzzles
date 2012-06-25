import time

def timed_call(fn, *args):
    t = time.clock()
    r = fn(*args)
    dt = time.clock() - t
    return (dt, r)