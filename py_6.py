# And, Or and Not Operators
x = True
y = False
print ("x and y:", x and y)
print ("x or y:", x or y)
print ("not x:", not x)

# if, elif, else(Conditionals)
score = 55
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print ("Needs Improvement")

# For Loop
fruits = [ "apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print ("Count:", count)
    count += 1

# in membership
sentence = "I am your world"
if "world" in sentence:
    print ("'world' is in the sentence")
else:
    print ("'world' is not in the sentence")

# is identity operator
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print ("list1 is list2:", list1 is list2)
print ("list2 is list3:", list2 is list3)

# def function definition
def greet(name):
    return f"Hello, {name}"
message = greet("MudduBaby")
print(message)

# import (Module importing)
import math

radius = 5
area = math.pi * (radius ** 2)
print (f"Area of circle: {area}")

# try, except, finally (Exception Handline)
try:
    result = 10 /0
except ZeroDivisionError:
    print ("Cannot divide by zero!")
finally: 
    print ("Execution complete")

# class (Defining a class)
class Dog:
    # Keyword: def(defining a method witihin a class)
    def __init__(self, name):
        self.name = name
        def bark(self):
            print (f"{self.name} sayd woof!")
            my_dog = Dog("Buddy")
            my_dog.bark()
            