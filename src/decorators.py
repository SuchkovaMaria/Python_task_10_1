from functools import wraps
from time import time


def log(filename=None):
    """Декоратор для логирования результата выполнения функции"""
    def wrapper(func):
        @wraps(func)
        def loging_func(*args, **kwargs):
            time_begin = time()
            try:
                result = func(*args, **kwargs)
                time_end = time()
                result_str = f"{func.__name__} ok"
            except Exception as e:
                error_type = type(e).__name__
                result_str = f"{func.__name__} error:{error_type}. Inputs: {args}, {kwargs}. {e}"
            if filename:
                with open(filename, "w", encoding="utf--8") as f:
                    f.write(str(result_str))
                    return result
            else:
                print(result_str)
            try:
                return result
            except UnboundLocalError:
                return result_str

        return loging_func

    return wrapper
