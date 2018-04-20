import sys


def breakpoint(value=None, up=1):
    if breakpoint.enabled:
        import ipdb
        frame = sys._getframe()
        for __ in range(up): frame = frame.f_back
        # Call sset_trace (starting with double s) rather than set_trace
        # in order to break free from nosetests's captured stdout!
        ipdb.sset_trace(frame, context=7)
    return value


def disable_all_breakpoints():
    breakpoint.enabled = False


def eneable_all_breakpoints():
    breakpoint.enabled = True


breakpoint.enable = eneable_all_breakpoints
breakpoint.disable = disable_all_breakpoints
breakpoint.enable()


# More debugging functions...


logs = {}


def log(value):
    frame = sys._getframe().f_back
    filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    if not filename in logs: logs[filename] = {}
    if not lineno in logs[filename]: logs[filename][lineno] = []
    logs[filename][lineno].append(value)
    return value


def sample(function):
    samples = []
    def wrapper(*args, **quarks):
        sample = dict(enumerate(args), **quarks)
        value = function(*args, **quarks)
        sample['$'] = value
        samples.append(sample)
        return value
    wrapper.samples = samples
    return wrapper


def wrap(function):
    def wrapper(*args, **quarks):
        breakpoint(up=2)
        return function(*args, **quarks)
    return wrapper


