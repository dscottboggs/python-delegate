from delegate import delegate

class Parent:
    def __init__(self):
        self.a = "a"
        self.b = "b"

@delegate("a", "b", to="parent")
class Child:
    def __init__(self):
        self.parent = Parent()
        self.c = "c"

instance = Child()
assert instance.a == "a"
