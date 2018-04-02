# Import this module into your script to enable debugging.
from breakpoint import breakpoint
from sample import sample
from wrap import wrap


__builtins__['debugger'] = breakpoint
