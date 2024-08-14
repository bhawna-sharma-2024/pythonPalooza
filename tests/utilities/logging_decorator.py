import functools
import time

def log_function_call(func):
    @functools.wraps(func) #preserves metadata of the function like name and docstring

    def wrapper(*args,**kwargs):
        print(f"Calling function {func.__name__}")
        print(f"Arguments passed: {args} and kwargs={kwargs}")
        start_time=time.time()
        result=func(*args,**kwargs)
        print(f"The function returned response: {result}")
        end_time=time.time()
        print(f"The total time take is: {end_time-start_time:.4f}seconds")
        return result
    return wrapper
