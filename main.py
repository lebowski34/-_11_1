import inspect
import sys


def introspection_info(obj):
    info = {}

    info['type'] = str(type(obj).__name__)

    if hasattr(obj, '__dict__'):
        info['attributes'] = list(obj.__dict__.keys())
    else:
        info['attributes'] = []

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    module = getattr(obj, '__module__', '__main__')
    info['module'] = module

    info['is_callable'] = callable(obj)
    info['has_doc'] = bool(getattr(obj, '__doc__', None))

    return info


class ExampleClass:

    def __init__(self, value):
        self.value = value

    def example_method(self):
        return f"Value is {self.value}"

    def __str__(self):
        return f"ExampleClass(value={self.value})"


example_instance = ExampleClass(42)

info = introspection_info(example_instance)
print(info)
