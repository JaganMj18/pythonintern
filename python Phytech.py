# python_phytech_basics.py
# 50 Basic Python Codes by Phytech

# 1. Hello World
print("Hello, World!")

# 2. Variables and Data Types
x = 5           # integer
y = 3.14        # float
name = "Jagan"  # string
is_active = True  # boolean
print(x, y, name, is_active)

# 3. Input from User
# name = input("Enter your name: ")
# print("Hello, " + name)

# 4. Basic Arithmetic
a = 10
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# 5. If-Else Condition
num = 5  # example number
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 6. Check Even or Odd
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 7. Find Largest of Three Numbers
a, b, c = 10, 20, 15
if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")

# 8. For Loop - Print Numbers 1 to 10
for i in range(1, 11):
    print(i)

# 9. While Loop - Print Numbers 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 10. Sum of First N Natural Numbers
n = 10
sum_val = 0
for i in range(1, n+1):
    sum_val += i
print("Sum:", sum_val)

# 11. Factorial of a Number (Iterative)
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)

# 12. Factorial of a Number (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial (recursive):", factorial(5))

# 13. Check Prime Number
num = 29
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not prime")
            break
    else:
        print(num, "is prime")
else:
    print(num, "is not prime")

# 14. Fibonacci Series up to N Terms
n = 7
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
print()

# 15. Check Palindrome String
string = "madam"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 16. Reverse a String
string = "Jagan"
print("Reversed string:", string[::-1])

# 17. Count Vowels in a String
string = "Hello World".lower()
vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# 18. Remove Duplicates from List
lst = [1, 2, 3, 2, 4, 3, 5]
unique_lst = list(set(lst))
print(unique_lst)

# 19. List Comprehension - Squares of Numbers 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# 20. Find Max and Min in a List
lst = [10, 5, 7, 3, 9]
print("Max:", max(lst))
print("Min:", min(lst))

# 21. Sum of List Elements
lst = [1, 2, 3, 4, 5]
print("Sum:", sum(lst))

# 22. Dictionary Example - Create and Access
person = {"name": "Jagan", "age": 22, "city": "Tirupati"}
print(person["name"])

# 23. Iterate Over Dictionary Items
for key, value in person.items():
    print(key, ":", value)

# 24. Function with Return Value
def add(a, b):
    return a + b
print(add(5, 3))

# 25. Lambda Function to Square a Number
square = lambda x: x**2
print(square(6))

# 26. File Handling - Write to a File
with open("file.txt", "w") as f:
    f.write("Hello, file!")

# 27. File Handling - Read from a File
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# 28. Exception Handling - Try Except
try:
    x = 5
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# 29. Class and Object Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is", self.name)
p = Person("Jagan", 22)
p.greet()

# 30. Inheritance Example
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
d = Dog()
d.speak()

# 31. List Sorting
lst = [5, 2, 9, 1]
lst.sort()
print(lst)

# 32. Check if List is Empty
lst = []
if not lst:
    print("List is empty")
else:
    print("List is not empty")

# 33. Using Map Function
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)

# 34. Using Filter Function
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 35. List Slicing
lst = [1, 2, 3, 4, 5]
print(lst[1:4])   # from index 1 to 3
print(lst[:3])    # first 3 elements
print(lst[2:])    # from index 2 to end
print(lst[-2:])   # last 2 elements

# 36. Swap Two Variables
a = 5
b = 10
a, b = b, a
print(a, b)

# 37. Check Membership in List
lst = [1, 2, 3, 4]
print(3 in lst)   # True
print(5 in lst)   # False

# 38. Generate Random Number
import random
print(random.randint(1, 100))

# 39. Count Characters in String
string = "hello world"
print(string.count('l'))

# 40. Convert String to List
string = "hello"
lst = list(string)
print(lst)

# 41. Join List into String
lst = ['h', 'e', 'l', 'l', 'o']
string = ''.join(lst)
print(string)

# 42. Check Type of Variable
x = 5
print(type(x))

# 43. Use of Global Variable
x = 10
def func():
    global x
    x = 5
func()
print(x)

# 44. List Append vs Extend
lst = [1, 2]
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]]

lst2 = [1, 2]
lst2.extend([3, 4])
print(lst2) # [1, 2, 3, 4]

# 45. Use of Enumerate
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):
    print(index, value)

# 46. Use of Zip
names = ['Jagan', 'Kiran']
ages = [22, 23]
for name, age in zip(names, ages):
    print(name, age)

# 47. Set Operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# 48. List Copy vs Assignment
lst1 = [1, 2, 3]
lst2 = lst1
lst3 = lst1.copy()
lst2.append(4)
print(lst1)  # [1,2,3,4]
print(lst3)  # [1,2,3]

# 49. Use of __str__ in Class
class PersonStr:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"
p = PersonStr("Jagan")
print(p)

# 50. Simple Calculator Using Functions
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: Divide by zero"
print(add(5,3))
print(sub(5,3))
print(mul(5,3))
print(div(5,0))
