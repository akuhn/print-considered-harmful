from breakpoint import breakpoint


def wrap(function):
    def wrapper(*args, **quarks):
        breakpoint(up=2)
        return function(*args, **quarks)
    return wrapper
