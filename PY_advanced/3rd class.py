# class Car:
#     def __init__(self) -> None:
#         self.brand = "Toyota"
#         self.model = "Camry"
#         self.color = "Black"
#         self.year = "2025"
        
# mycar = Car()
# print(f"I just bought my self a brand new {mycar.brand} {mycar.model}, {mycar.year},{mycar.color} Ride")


# class Car:
#     def __init__(self, brand, model, color, year) -> None:
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.year = year
        
# car1 = Car("Toyota", "Corolla", "Black", "2020")
# car2 = Car("Tesla", "S", "Silver", "2024")
# car3 = Car("BMW", "M-5", "Green", "2026")
# print(car1.brand, car2.year, car3.color)
# print(f'I just gor myself a brand new {car1.brand} {car1.model}, {car1.year}, {car1.color} Ride')
# print(f'I just gor myself a brand new {car2.brand} {car2.model}, {car2.year}, {car2.color} Ride')
# print(f'I just gor myself a brand new {car3.brand} {car3.model}, {car3.year}, {car3.color} Ride')


# class Person:
#     def __init__(self, FirstName, LastName, Age) -> None:
#         self.FirstName = FirstName
#         self.LastName = LastName
#         self.Age = Age
     
# p1 = Person("Zara", "Adamu", "15")
# p2 = Person("John", "Ayo", "21")
# print(p1.FirstName, p1.LastName, p1.Age)
# print(p2.FirstName, p2.LastName, p2.Age)

class Person:
    def __init__(self, FirstName, LastName, Age) -> None:
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        
    def __str__(self) -> str:
        return f'Hello Everyone, Mn name is {self.FirstName} {self.LastName} and i am {self.Age} years old.'
         
p1 = Person("Zara", "Adamu", "15")
p2 = Person("John", "Ayo", "21")
print(p1)
print(p2)    