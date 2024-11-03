# fruits = ['apple','banana','mango']
# x,y,z = fruits

# print(x)
# print(y)
# print(z)

# a = 5
# b = 'john'
# print(a,b)

# x = "awesome"
# def myfunc():
#     x = "fantastic"
#     print("Python is "+ x)
    
# myfunc()

# print("Python is " + x)

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""

# print(a)

# txt = "The best things in life are free!"
# # if "free" in txt:
# #     print("Yes,'free' is present.")

# # print("expensive" not in txt)
# if "expensive" not in txt:
#     print("No,'expexsive' is Not present")

# b = "Hello, World"
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# print(b[-5:-2])

# print(b.split(","))

# txt = "We are the so-called \"viking\"from the north "
# print(txt)

# print(bool("hello"))
# print(bool(15))

# x = 200
# print(isinstance(x,int))

# thislist = ["apple","banana","cherry"]
# # thislist[1:2] = ["blackcurrent","watermelon"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# fruits = ["apple","banana","cherry","kiwi","mango"]
# # newlist = [x for x in fruits if "a" in x]
# # newlist = [x.upper() for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# fruits = ["Orange","Ananas","Apple","apple","banana","cherry","Kiwi","pineapple","mango"]
# # fruits.sort()
# # fruits.sort(reverse=True)
# fruits.sort(key=str.lower)
# print(fruits)

# def myfunc(n):
#     return abs(n-50)

# thislist = [100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)

# fruits = ("apple","banana","cherry","streawberry","rasberry")
# (green,*yellow,red) = fruits
# print(green)
# print(yellow)
# print(red)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": "1964"
# }
# x = car.items()
# print(x)
# car["color"] = "red"
# print(x)

# for x,y in car.items():
#     print(x, y)

# for x in range(2,30,3):
#     print(x)

# x = lambda a : a + 10
# print(x(5))

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("john",36)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
        
#     def printname(self):
#         print(self.firstname,self.lastname)

# p1 = Person("John","Doe")
# p1.printname()

# class Student(Person):
#     pass

# x = Student("Mike","Olsen")
# x.printname()

# mytuple = ("apple","banana","cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Drive")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("Sail")
        
# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Fly")
        
        
# car1 = Car("Ford","Mustang")
# boat1 = Boat("Ibiza","Touring 20")
# plane1 = Plane("Boeing","747")

# for x in (car1,boat1,plane1):
#     x.move()

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     def move(self):
#         print("Move")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail")

# class Plane(Vehicle):
#     def move(self):
#         print("fly")        
        
# car1 = Car("Ford","Mustang")
# boat1 = Boat("Ibiza","Touring 20")
# plane1 = Plane("Boeing","747")

# for x in (car1,boat1,plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

# import platform
# x = platform.system()
# y = dir(platform)
# print(y)
# print(x)

# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

quantity = 4
itemno = 590
price = 43

myorder = "I want {0} pice of item number {1} for {2:.2f} dollers."
print(myorder.format(quantity,itemno,price))