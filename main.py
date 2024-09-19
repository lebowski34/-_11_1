def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    info['module'] = type(obj).__module__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    if isinstance(obj, (int, float, str, list, dict, set, tuple)):
        info['value'] = obj
    elif hasattr(obj, '__dict__'):
        info['attributes_count'] = len(attributes)
        info['methods_count'] = len(methods)

    return info


class MyClass:
    class_attribute = "Классовый атрибут"

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def greet(self):
        return f"Привет, {self.name}!"

    def set_value(self, new_value):
        self.value = new_value


# Пример использования функции introspection_info

if __name__ == "__main__":
    # Пример 1: Интроспекция целого числа
    number_info = introspection_info(42)
    print("Информация о числе 42:")
    print(number_info)
    print()

    # Пример 2: Интроспекция строки
    string_info = introspection_info("Hello, World!")
    print("Информация о строке 'Hello, World!':")
    print(string_info)
    print()

    # Пример 3: Интроспекция пользовательского объекта
    my_obj = MyClass(name="Алиса", value=100)
    object_info = introspection_info(my_obj)
    print("Информация о пользовательском объекте MyClass:")
    print(object_info)
