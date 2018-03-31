# Import this module into your script to enable debugging.


def breakpoint(value=None):
    if breakpoint.enabled:
        import sys
        import ipdb
        # Call sset_trace (starting with double s) rather than set_trace
        # in order to break free from nosetests's captured stdout!
        ipdb.sset_trace(sys._getframe().f_back, context=7)
    return value


def disable_all_breakpoints():
    breakpoint.enabled = False


breakpoint.enabled = True
breakpoint.disable = disable_all_breakpoints


__builtins__['debugger'] = breakpoint
