#Variable = A container for a value (string, integer, float boolean)
#           A variable behaves as if it was the value it contains

#Strings
first_name = "Inda"
food = "Kiwi"
email = "inda@gmail.com"

#Integers
age = 29
quantity = 3
num_of_students = 30




print(age + quantity)

#format?
print (f"I am {age} years old")
print (f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")
#WRONG:
# print ("I am" + age + "years old")

#Float
price=10.99
gpa = 3.5
distance = 5.5

print (f"The price is ${price}")
print (f"My gpa is: {gpa}")
print(f"You ran {distance}km")

is_student = False
for_sale = True

print(f"Are you a student? {is_student}")

#if statement
if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")


