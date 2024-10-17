class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')

p = Program()
print(type(Program), type(p))
print(isinstance(p, Program))
print(p.__dict__)
print(p.__class__)
print(Program.__dict__)
print(type(p) is p.__class__)
print('-'*30)


class MyClass:
    pass

m = MyClass()
print(type(m), m.__class__)

print('-'*30)


class MyClass:
    __class__ = str

m = MyClass()
print(type(m), m.__class__)

print(isinstance(m, MyClass))
print(isinstance(m, str))
print(isinstance(m, int))

print('-'*30)


class MyClass:
    pass

m = MyClass()
print(type(m), m.__class__)

print(isinstance(m, MyClass))
print(isinstance(m, str))
print(isinstance(m, int))





