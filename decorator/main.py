"""
decorator.py
Description: how decorators work.
Decorators are functions that accept a function as input and then return a new function

"""

from datetime import datetime
import time

def notify_proto(f):
    """ A prototype decorator to notify user
    when a function is entered amd exited"""
    def wrapper():
        print("Enter: ", f.__name__)
        f()
        print("Exit: ", f.__name__)

    return wrapper

def notify(f):
    """ A correct decorator to notify user
    when a function is entered amd exited"""
    def wrapper(*args, **kwargs):
        print("Enter: ", f.__name__)
        f(*args, **kwargs)
        print("Exit: ", f.__name__)

    return wrapper

def do_twice(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)

    return wrapper

def log(f):
    """ A correct decorator to notify user
    when a function is entered amd exited"""
    def wrapper(*args, **kwargs):
        print(str(datetime.now()) + " Entering: ", f.__name__)
        val = f(*args, **kwargs)
        return val

    return wrapper

def timer(f):
    """ Modify a function so that it now reports the elapsed time """
    def wrapper(*args, **kwargs):
        start = time.time()
        val = f(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print("Elapsed time: ", elapsed)
        return val

    return wrapper


@notify_proto
def hello_world():
    print("Hello World!")

@timer
def hello(name="World"):
    """ Say hello to <name>"""
    print(f"Hello {name}!")

@timer
@log
def myfunc(x):
    return 3 * x + 1

@timer
def squares(n):
    return [i ** 2 for i in range(n)]


def main():
    # hello("John")
    # z = myfunc(7)
    # print(z)
    squares(100000000)


if __name__ == "__main__":
    main()
