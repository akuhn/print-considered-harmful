# Import this module into your script to enable debugging.
from debug import breakpoint
from debug import *


breakpoint.log = log
breakpoint.logs = logs
breakpoint.sample = sample
breakpoint.wrap = wrap


__builtins__['debugger'] = breakpoint
