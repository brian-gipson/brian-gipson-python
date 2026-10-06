#Section 1: Variables and Types 

name = "Brian"
age = 47
height = 6.0
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


#Section 2: User Input and Math

name = input("What is your name? ")
year_born = int(input("What year were you born? "))

from datetime import date
this_year = date.today().year

approx_age = (this_year - year_born)

print(f"Hi, {name}! You are approximately {approx_age} years old.")


#Section 3: Type Conversion and f-strings

num1 = float(input("Pick a number: "))
num2 = float(input("Pick a number: "))

num = (num1 * num2)

print(f"{num1} x {num2} = {num}")


#Section 4: Formatted Receipt

item = "Python textbook"
price = 29.99
quantity = 2

total = (price * quantity)

print("===========================")
print("          RECEIPT          ")
print("===========================")
print(f"Item:      {item:}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity:}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


#Section 5: Mini-Project — Profile Card

fname = input("What is your first name? ")
lname = input("What is your last name? ")
hometown = input("Where are you from? City, State ")
hobby = input("What do you like to do during your free time? ")
fun_fact = input("Give me a fun fact about you. ")
age = input("How old are you? ")

print("╔══════════════════════════════╗")
print(f"   Profile:  {fname} {lname}")
print("╚══════════════════════════════╝")
print(f"Hometown: {hometown}")
print(f"Hobby: {hobby}")
print(f"Fun fact: {fun_fact}")
print(f"Age: {age}")
