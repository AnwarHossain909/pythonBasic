'''
# print Hello World
print("Hello World")

p = 'Hello World'
print(p)


# variables and data type
a = 10
b = 32

sum = a + b
print('Addition :',sum)


#data type
print(type(23))      
print(type('Hello'))
print(type(True))
print(type(25.5))
print(type('a'))


#Condition(if/else)

a = int(input())
b = int(input())

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")



# loop(for/while)
# For loop
for i in range(5):
    print("Number:", i)

# While loop
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1


# functions

def func(name):
    return f"Hello : {name}"

print(func("Anwar"))
print(func("Saidee"))



# list

fruits = ["apple", "banana", "mango"]

# Add item
fruits.append("orange")
print(fruits[0]) # apple asbe

# Loop
for fruit in fruits:
    print(fruit[0])



# dictionary(key/values)
user = {
    "name": "Anwar",
    "age": 22,
    "city": "Dhaka"
}

print(user["name"])   # Access by key

for i in user: # sob golo dekhabe
    print(i)



# to - do app
todos = []

while True:
    task = input("Enter task (or 'exit'): ")
    if task == "exit":
        break
    todos.append(task)

print("Your Tasks:")
for t in todos:
    print("-", t)

'''

#file write and read
# Write into file
with open("notes.txt", "w") as f:
    f.write("Hello, I am learning Backend!\n")

# Read from file
with open("notes.txt", "r") as f:
    print(f.read())

