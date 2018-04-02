# Helper functions for tests
import ipdb


class mockdebugger():

    def __enter__(self):
        def callback(frame, context=None):
            self.call_count += 1
            self.lineno = frame.f_lineno
            self.fname = frame.f_code.co_name
        self.call_count = 0
        self.original = ipdb.sset_trace
        ipdb.sset_trace = callback
        return self

    def __exit__(self, *args):
        debugger.enabled = True
        ipdb.sset_trace = self.original
