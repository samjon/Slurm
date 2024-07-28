class MyClass:
    def __init__(self):
        self.name = "Alice"

    def greet(self):
        print("Hello, " + self.name)

obj = MyClass()
print(dir(obj))  # Выводит список атрибутов и методов объекта 'obj'
print(dir())  # Выводит список имен в текущей локальной области видимости