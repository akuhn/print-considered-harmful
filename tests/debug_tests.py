# Run this with nosetests
from expects import *
from helper import *

import debug


def test____should_install_buildin_function():
    expect(__builtins__).to(have_key('debugger'))


def test____should_call_the_debugger():
    with mockdebugger() as mock:
        debugger()

    expect(mock.call_count).to(equal(1))


def test____should_break_at_correct_frame():
    def example():
        "lorem ipsum"
        debugger()
        "lorem ipsum"

    with mockdebugger() as mock:
        example()

    expect(mock.fname).to(equal('example'))
    expect(mock.lineno).to(equal(22))


def test____should_disable_breakpoint():
    with mockdebugger() as mock:
        debugger.disable()
        debugger()

    expect(mock.call_count).to(equal(0))


def test____should_wrap_function_call():
    def function():
        pass

    with mockdebugger() as mock:
        function = debug.wrap(function)
        function()

    expect(mock.call_count).to(equal(1))


def test____should_break_at_function_call():
    def function():
        pass

    def example():
        function()

    with mockdebugger() as mock:
        function = debug.wrap(function)
        example()

    expect(mock.fname).to(equal('example'))
    expect(mock.lineno).to(equal(56))


def test____should_sample_function_calls():
    def function(a, b=None):
        return a ** 2

    function = debug.sample(function)
    function(23)
    function(42, b='hello worlds')

    expect(function.samples).to(have_len(2))

    expect(function.samples[0][0]).to(equal(23))
    expect(function.samples[0]).to_not(have_key('b'))
    expect(function.samples[0]['$']).to(equal(529))

    expect(function.samples[1][0]).to(equal(42))
    expect(function.samples[1]['b']).to(equal('hello worlds'))
    expect(function.samples[1]['$']).to(equal(1764))


def test____should_log_values():
    for each in range(3):
        debug.log(each)

    filename = __file__.replace('.pyc', '.py')
    expect(debug.logs).to(have_key(filename))
    expect(debug.logs[filename]).to(have_key(87))
    expect(debug.logs[filename][87]).to(equal([0,1,2]))


def test____should_return_logged_value():
    value = debug.log(42)

    expect(value).to(equal(42))
