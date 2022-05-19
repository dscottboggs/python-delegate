# Delegate
### A python library for delegation (the metaprogramming feature)

This library adds the `@delegate` decorator which may be used to delegate
attributes from an attribute of the existing class. For example:

```python
from delegate import delegate

class Parent:
    def __init__(self):
        self.a = "a"
        self.b = "b"
        self.d = "d"

# The delegate decorator makes .a and .b available on Child, through its
# "parent" attribute, as though Child had an a and b attribute itself.
@delegate("a", "b", to="parent")
class Child:
    def __init__(self):
        self.parent = Parent()
        self.c = "c"

instance = Child()
assert instance.a == "a"
raised = False
try:
    # But d is not available
    instance.d
except e:
    raised = True

assert raised
```

Delegation can also be called multiple times on the same class, and there is an
optional `prefix` option which allows the attribute name to be prefixed on the
delegating class:

```python
from delegate import delegate

class Parent:
    def __init__(self):
        self.a = "a"
        self.b = "b"

@delegate("a", to="parent")
@delegate("b", to="parent", prefix="_")
class Child:
    def __init__(self):
        self.parent = Parent()
        self.c = "c"

instance.a
instance._b
```
