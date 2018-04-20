# Print statement considered harmful

Switch from `print` to `debugger()` and never look back.

    import debug

    debugger() # <-- breaks here

Import this module in your main file to add `debugger` as a builtin command.


## Documentation

All functions

    debugger()
    debugger.enable()
    debugger.disable()
    debug.wrap(function)
    debug.sample(function)
    function.samples


Calling `debugger` opens the `ipdb` debugger,

    import debug

    debugger() # <-- breaks here


Calling `debugger.disable` from the ipdb prompt disables all breakpoints,

    import debug

    debugger() # <-- breaks here

    # >> debugger.disable()
    # >> continue

    debugger() # <-- does not break here


Using `debug.wrap` sets a function breakpoint,

    def fun():
        pass

    def example():
        fun()

    fun = debug.wrap(fun)
    example() # <-- breaks above at definition of fun


Using `debug.sample` collects function arguments,

    def fun(a, b=None):
        return

    fun = debug.sample(fun)
    fun(23)
    fun(42, 'hello worlds')

    debugger() # <-- breaks here

    # >> len(fun.samples)
    # 2
    # >> fun.samples
    # [{0: 23, '$': 529}, {0: 42, 'b': 'hello worlds', '$': 1764}]


Using `debug.log` collects values,

    for each in range(3):
        debug.log(each)

    debugger() # <-- breaks here

    # >> debugger.logs
    # {'example.py': {2: [0, 1, 2]}}


## Installation

To install this package, run

    pip install print-considered-harmful


## Contributing

Bug reports and pull requests are welcome on github at, https://github.com/akuhn/print-considered-harmful
