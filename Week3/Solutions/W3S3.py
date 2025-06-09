"""
More file handling and Decorators

Logging Decorator
Timing Decorator

Implement two functions that do the same thing through different methods
Log and time the execution of each function.
"""

from time import time

def timing_decorator(func):
    """
    Decorator to time the execution of a function.
    """
    def wrapper(*args: tuple, **kwargs: dict):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def logging_decorator(func, filename: str = "./Data/Logs.txt"):
    """
    Decorator to log the execution of a function.
    """
    def wrapper(*args: tuple, **kwargs: dict):
        with open(filename, 'a') as log_file:
            log_file.write(f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}\n")
        result = func(*args, **kwargs)
        with open(filename, 'a') as log_file:
            log_file.write(f"Function '{func.__name__}' returned: {result}\n")
        return result
    return wrapper


@logging_decorator
@timing_decorator
def sum1(n: int):
    """
    Example function that computes the sum of the first n natural numbers.
    """
    return sum(range(n))


@logging_decorator
@timing_decorator
def sum2(n: int):
    """
    Another example function that computes the sum of the first n natural numbers.
    This could be implemented differently, e.g., using a generator.
    """
    return sum(i for i in range(n))

@logging_decorator
@timing_decorator
def sum3(n: int):
    """
    Yet another example function that computes the sum of the first n natural numbers.
    This could be implemented using a different algorithm or approach.
    """
    total = 0
    for i in range(n):
        total += i
    return total


sum1(10000)
sum2(10000)
sum3(10000)
