#!/usr/bin/env python3

def delegate(*args, **named_args):
    dest = named_args.get('to')
    if dest is None:
        raise ArgumentError("the named argument 'to' is required on the delegate function")
    print(args, dest)
    def wraps(cls, *wrapped_args, **wrapped_opts):
        print('in wraps()')
        class Wrapped(cls):
            def __init__(self, *wrapped_args, **wrapped_opts):
                print("in Wrapped#__init__()")
                super().__init__(*wrapped_args, **wrapped_opts)
                for arg in args:
                    setattr(self, arg, getattr(getattr(self, dest), arg))
        return Wrapped
    return wraps
