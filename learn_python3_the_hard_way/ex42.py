## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        ## cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self,name):
        ## Person has-a name    
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self,name, salary):
        ## Employee like person has-a name
        super(Employee,self).__init__(name)
        ## Empolyee has-a name
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet has-a name satan
mary.pet = satan

## Frakn is-a Employee has-a salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a salmon
croush = Salmon()

## harry is-a halibut
harry = Halibut()