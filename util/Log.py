import inspect


def p(msg):
    caller_class = inspect.currentframe().f_back.f_locals['self'].__class__.__name__
    print(f"{caller_class}: {msg}")
