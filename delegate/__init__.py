#!/usr/bin/env python3

def bind(instance, func, name):
    """Turn a function into a bound method on instance"""
    setattr(instance, name, func.__get__(instance, instance.__class__))

def delegate(*args, **named_args):
    dest = named_args.get('to')
    if dest is None:
        raise ValueError("the named argument 'to' is required on the delegate function")
    def wraps(cls, *wrapped_args, **wrapped_opts):
        class Wrapped(cls):
            def __init__(self, *wrapped_args, **wrapped_opts):
                super().__init__(*wrapped_args, **wrapped_opts)
                dest_prop = getattr(self, dest)
                for arg in args:
                    # prop =
                    # prop.__doc__ = dest_prop.__doc__
                    setattr(self, arg, property(
                            lambda self: getattr(dest_prop, arg),
                            lambda self, value: setattr(dest_prop, arg, value),
                            lambda self: delattr(dest_prop, arg)
                        ).__get__(self, cls))
        return Wrapped
    return wraps
