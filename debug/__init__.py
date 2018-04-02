# Import this module into your script to enable debugging.


def breakpoint(value=None, up=1):
    if breakpoint.enabled:
        import sys
        import ipdb
        frame = sys._getframe()
        for __ in range(up): frame = frame.f_back
        # Call sset_trace (starting with double s) rather than set_trace
        # in order to break free from nosetests's captured stdout!
        ipdb.sset_trace(frame, context=7)
    return value


def disable_all_breakpoints():
    breakpoint.enabled = False


breakpoint.enabled = True
breakpoint.disable = disable_all_breakpoints


__builtins__['debugger'] = breakpoint


def wrap(function):
    def wrapper(*args, **quarks):
        breakpoint(up=2)
        return function(*args, **quarks)
    return wrapper


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
