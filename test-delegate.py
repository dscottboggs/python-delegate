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


print("TESTING delegate()...", end='\r')

instance = Child()
assert instance.a == instance.parent.a == "a"
instance.b = "d"
print(instance.__dict__, instance.parent.__dict__)
assert instance.b == instance.parent.b == "d"
err = None
del instance.a
try: instance.a
except Exception as e: err = e
finally: assert err
assert instance.c == 'c'
err = None
try: instance.parent.c
except Exception as e: err = e
finally: assert err
z
print("TESTING delegate()...done")
