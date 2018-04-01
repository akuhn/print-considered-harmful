# Run this with nosetests
from expects import *
from mock import Mock

import debug
import ipdb


def test____should_install_buildin_function():
    expect(__builtins__).to(have_key('debugger'))


def test____should_call_the_debugger():
    try:
        original = ipdb.sset_trace
        ipdb.sset_trace = Mock()
        def example():
            debugger()
        example()

        expect(ipdb.sset_trace.call_count).to(be(1))
        frame = ipdb.sset_trace.call_args[0][0]
        expect(frame.f_code.co_name).to(equal('example'))
        expect(frame.f_lineno).to(equal(18))
    finally:
        ipdb.sset_trace = original
