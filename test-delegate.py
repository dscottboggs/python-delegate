from delegate import delegate
from contextlib import contextmanager
class Parent:
    def __init__(self):
        self.a = "a"
        self.b = "b"

@delegate("a", "b", to="parent")
class Child:
    """A class with a delegate"""
    def __init__(self):
        self.parent = Parent()
        self.c = "c"


print("TESTING delegate()...", end='\r')

@contextmanager
def expect_raises(errtype):
    err = None
    try:
        yield
    except errtype as e:
        err = e
    finally:
        assert err

instance = Child()
assert instance.a == instance.parent.a == "a"
instance.b = "d"
print(instance.__dict__, instance.parent.__dict__)
assert instance.b == instance.parent.b == "d"
err = None
del instance.a
with expect_raises(Exception):
    instance.a
assert instance.c == 'c'
with expect_raises(Exception):
    instance.parent.c
assert instance.__doc__ == "A class with a delegate"
assert instance.__class__.__name__ == "Child"
with expect_raises(AttributeError):
    instance.z

print("TESTING delegate()...done")
