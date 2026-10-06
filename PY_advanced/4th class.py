# class Phone:
#     def __init__(self, brand, model, color, year) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.year = year
        
#     def call(self):
#         no = input('Enter number to call: ')
#         print(f'My {self.brand}, {sel.model}, phone is calling... {no}')
        
#     def camera(self):
#         print('CHAKAMMM')
        
# phn = Phone("Samsung", "s24", "Red", "2024")

# phn.call()
# phn.camera()



# class Person:
#     def __init__(self, fname, lname, age) -> None:
#         self.fname = fname
#         self.lname = lname
#         self.age = age
        
#     def welcome(self):
#         course = input('Enter your course')
#         print(f'Hello {self.fname} {self.lname}, welcome to {course} class')
        
# per1 = Person('Musa', 'Adams', '21')
# per2 = Person('Jane', 'Ade', '24')
# print(per1.fname)
# per1.welcome()
# per2.welcome()


class Person:
    def __init__(self, fname, lname, age) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def welcome(self):
        print(f'Hello {self.fname} {self.lname}, welcome to class')
        
per = Person('Zara', 'Ayo', '23')


class Student(Person):
    # pass

    def course(self):
        cou = input('Enter your course: ')
        print(f'{self.fname} {self.lname} is in {cou} class.')

stu = Student('Adams', 'John', '21')
stu.welcome()
# per.welcome()
stu.course()
