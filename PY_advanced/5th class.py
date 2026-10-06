# class Car: 
#     def __init__(self, brand, model) -> None:
#         self.brand = brand 
#         self.model = model
        
#     def move(self):
#         print(f'My {self.brand} {self.model} is DRIVING...')
        
# class Plane:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#             print(f'My {self.brand} {self.model} is FLYING...')
            
# class Boat:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#             print(f'My {self.brand} {self.model} is SAILING...')
            
# car1 = Car('Toyota', 'Camry')
# plane1 = Plane('Gulfstream', 'G-650')
# boat1 = Boat('Ibiza', 'Touring-20')

# for x in car1,boat1,plane1:
#     x.move()


# class Transport:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
        
# class Car(Transport):
#     def move(self):
#         print(f'My {self.brand} {self.model} is DRIVING...')
        

# class Plane(Transport):
#     def move(self):
#         print(f'My {self.brand} {self.model} is FLYING...')
        

# class Boat(Transport):
#     def move(self):
#         print(f'My {self.brand} {self.model} is SAILING...')


# car1 = Car('Toyota', 'Camry')
# plane1 = Plane('Embrarer', 'E-25')        
# boat1 = Boat('Flimo', 'F-108')

# for x in car1,plane1,boat1:
#     x.move()
        
class Person:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def hello(self)    :
        print(f'Hello {self.fname} {self.lname} Hope u are fine 😊')
        
per = Person('Sarah', 'Adamu', 21)

class Student(Person):
    def __init__(self, fname, lname, age, gradyear) -> None:
        super().__init__(fname, lname, age)
        self.gradyear = gradyear
        
    def course(self)    :
        cou = input('Enter ur course: ')
        print(f'My name is {self.fname} {self.lname}, i am {self.age} years old, I am in {cou} and graduating in {self.gradyear} ')
        
stu = Student('John', 'Muse', 23, 2026)        
stu.course()