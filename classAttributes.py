class Person:
    pass

print(Person.__name__)

class Program:
    language = ('Python')
    version = '3.6'

print(Program.__name__)
print(type(Program))
print(Program.language)
print(Program.version)
Program.version = '3.7'
print(Program.version)


print(getattr(Program, 'version'))
setattr(Program, 'version', '3.6')
print(getattr(Program, 'version'))


#print(getattr(Program, 'x'))
print(getattr(Program, 'x', 'N/A'))


print(getattr('hello', 'x', 'N/A'))






