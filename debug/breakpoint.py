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


def eneable_all_breakpoints():
    breakpoint.enabled = True


breakpoint.enable = eneable_all_breakpoints
breakpoint.disable = disable_all_breakpoints
breakpoint.enable()
