from functools import wraps
from time import time
from config import ROOT_DIR


def log(filename=None):
    """Декоратор для логирования результата выполнения функции"""

    def decorator(func):


        @wraps(func)
        def wrapper(*args, **kwargs):
            time_begin = time()
            result = None
            try:
                result = func(*args, **kwargs)
                time_end = time()
                delta_time = time_end - time_begin
                result_str = f"{func.__name__} ok"
            except Exception as e:
                error_type = type(e).__name__
                result_str = f"{func.__name__} error:{error_type}. Inputs: {args}, {kwargs}. {e}"

            if filename:
                with open(f"{ROOT_DIR}/logs/{filename}", "w", encoding="utf--8") as f:
                    f.write(str(result_str))
            else:
                print(result_str)
            return result

        return wrapper

    return decorator
