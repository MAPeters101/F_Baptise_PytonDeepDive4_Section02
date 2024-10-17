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

Program.x = 100
print(Program.x, getattr(Program, 'x'))

a = 'hello'
#a.x = 100
#str.x = 100

print(Program.__dict__)

setattr(Program, 'x', -100)
print(Program.__dict__)

delattr(Program, 'x')
print(Program.__dict__)

Program.y = 'hello'
print(Program.__dict__)
del Program.y
print(Program.__dict__)

print(Program.__dict__['language'])
print(list(Program.__dict__.items()))

#Program.__dict__['language'] = 'Java'

print(Program.__name__)

