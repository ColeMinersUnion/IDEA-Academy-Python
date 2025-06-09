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