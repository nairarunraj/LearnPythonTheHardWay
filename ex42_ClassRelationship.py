# ex42 Is-A, Has-A

import pprint

## Animal is-a object
class Animal(object):
    pass


## Dog is-a Animal
class Dog(Animal):
    ## Constructor
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    ## toString()
    def __str__(self):
        return "Dog - [name: %s]" % self.name


## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

    def __str__(self):
        return "Cat - [name: %s]" % self.name


## Person is-a Animal
class Person(Animal):
    def __init__(self, name):
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

        # Person has-many moods
        self.moods = None

    def __str__(self):
        return "Person - [name: %s, pet: %s, moods: %s]" % (self.name, self.pet, self.moods)

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## Call the __init__ of Person to set the name
        ## Syntax - super(type, obj) . Premise - isInstance(obj, type)
        super(Employee, self).__init__(name)

        ## Employee has-a salary
        self.salary = salary

    def __str__(self):
        return "Employee - [%s, salary: %s]" % (super(Employee, self).__str__(), self.salary)


## Fish is-a object
class Fish(object):
    pass


## Salmon is-a Fish
class Salmon(Fish):
    pass


## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 12000)

## frank has-a pet rover
frank.pet = rover

## frank is happy and sad
frank.moods = ['Happy', 'Sad']

print frank

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
