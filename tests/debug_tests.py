# Run this with nosetests
from expects import *
from helper import *

import debug


def test____should_install_buildin_function():
    expect(__builtins__).to(have_key('debugger'))


def test____should_call_the_debugger():
    with mockdebugger() as mock:
        debugger()

    expect(mock.call_count).to(be(1))


def test____should_break_at_correct_frame():
    def example():
        "lorem ipsum"
        debugger()
        "lorem ipsum"

    with mockdebugger() as mock:
        example()

    expect(mock.fname).to(equal('example'))
    expect(mock.lineno).to(equal(22))


def test____should_wrap_function_call():
    def function():
        pass

    with mockdebugger() as mock:
        function = debug.wrap(function)
        function()

    expect(mock.call_count).to(be(1))


def test____should_break_at_function_call():
    def function():
        pass

    def example():
        "lorem ipsum"
        function()
        "lorem ipsum"

    with mockdebugger() as mock:
        function = debug.wrap(function)
        example()

    expect(mock.fname).to(equal('example'))
    expect(mock.lineno).to(equal(49))
