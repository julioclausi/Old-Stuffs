#Basic OOP

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def description(self):
        return f'{self.name} is {self.age} years old.'

    def birthday(self):
        self.age +=1
    
    def __str__(self):
        return f'{self.name} is {self.age} years old.'

class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = "Worker " + self.name

    def __str__(self):
        return f'{super().description()} He is a worker!!!'

someone = Person('John Doe', 33)
print (someone.description())
someone.birthday()
print (someone)
print ()

another_person = Worker('Jack Jones', 45)

print (another_person)
another_person.birthday()
print (another_person)