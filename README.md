# Print statement considered harmful

Switch from `print` to `debugger()` and never look back.

Import this module in your main file to add `debugger` as a builtin command.

Calling `debugger` opens the `ipdb` debugger,

    import debug

    debugger() # <-- breaks here


Calling `debugger.disable` from the ipdb prompt disables all breakpoints,

    import debug

    debugger() # <-- breaks here

    # Call `debugger.disable()` and continue

    debugger() # <-- does not break here


Using `debug.wrap` sets a function breakpoint,

    def function():
        pass

    def example():
        function()

    function = debug.wrap(function)
    example() # <-- breaks above at function definition


## Installation

To install this package, run

    pip install print-considered-harmful

## Contributing

Bug reports and pull requests are welcome on github at, https://github.com/akuhn/print-considered-harmful
