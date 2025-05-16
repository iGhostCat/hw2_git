import functools
from datetime import datetime


def log_output(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = (
                    f"[{timestamp}] Function {func.__name__} has been called with args={args}, kwargs={kwargs}. Result: {result}\n"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message, end="")
                return result
            except Exception as e:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = (
                    f"[{timestamp}] Function {func.__name__} has been called with args={args}, kwargs={kwargs}. Result: {e}!"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message, end="")


        return wrapper

    return decorator



@log_output(filename="operations.log")
def divide_foo(base,divider):
    '''Функция деления двух чисел, принимает два числа - делимое и делитель,
     возвращает частное в виде числа'''
    try:
        return base/divider
    except Exception as e:
        return f"Error {e}"


# Примеры использования
divide_foo(1,1)
divide_foo(1,0)
divide_foo('1',1)