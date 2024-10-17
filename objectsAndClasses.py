class Person:
    pass

print(type(Person))
print(type(type))
print(Person.__name__)

p = Person()
print(type(p))
print(p.__class__)
print(type(p) is p.__class__)

print(isinstance(p, Person))
print(isinstance(p, str))
print(isinstance('hello', str))
print(type(str))
print(help(type))





