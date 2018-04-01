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


def test____should_call_debugger_with_correct_frame():
    def example():
        debugger()

    with mockdebugger() as mock:
        example()

    frame = mock.call_args[0][0]
    expect(frame.f_code.co_name).to(equal('example'))
    expect(frame.f_lineno).to(equal(21))
