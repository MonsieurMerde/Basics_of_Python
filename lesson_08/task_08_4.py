from functools import wraps


def val_checker(func):

    def _val_checker(_func):
        @wraps(_func)
        def wrapper(*args, **kwargs):
            try:
                result = _func(*args, **kwargs)
                if func(*args, **kwargs):
                    print(result)
                else:
                    raise ValueError
            except (TypeError, ValueError):
                if args and kwargs:
                    print(f'Error in positional arguments: {args} or error in keyword arguments: {kwargs}')
                elif args:
                    print(f'Error in positional arguments: {args}')
                else:
                    print(f'Error in keyword arguments: {kwargs}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)
