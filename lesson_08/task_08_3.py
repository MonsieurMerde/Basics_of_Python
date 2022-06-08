def type_logger(func):

    def wrapper(*args, **kwargs):
        print(f'Call for: {func.__name__}')
        if args:
            print(*(f'{elem}: {type(elem)}' for elem in args), sep=', ')
        if kwargs:
            print(*(f'{key} = {value}: {type(value)}' for key, value in kwargs.items()), sep=', ')
        result = func(*args, **kwargs)
        print(f'Result: {result} type: {type(result)}')
        return result

    return wrapper


@type_logger
def render_input(*args, **kwargs):
    return 1


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
render_input(1, 45, a=2, b=True, c="q")
