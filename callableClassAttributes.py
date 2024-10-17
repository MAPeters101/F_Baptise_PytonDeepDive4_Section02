class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')

print(Program.__dict__)
print(Program.say_hello, getattr(Program, 'say_hello'))
print(Program.say_hello())
print(getattr(Program, 'say_hello'))
print(getattr(Program, 'say_hello')())

print(Program.__dict__['say_hello']())




