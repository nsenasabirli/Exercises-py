"""
import math
print(math.ceil(2.9))

weight_lbs = input('weight(lbs):  ' )
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

course = 'Phyton for Beginners'
another = course[0:]
print(another)
print(course[-1])
print(course[0:3])
print(course[0:])
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('f'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Phyton' in course)
print('phyton' in course)

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
print(x)

x = 2.9
print(round(x))
print(abs(-2.9))

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("enjoy your day")
elif is_cold:
    print("It's a cold day")
else:
   print("It's a lovely day")

price = 1000000
has_good_price = True

if has_good_price:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down_payment: {down_payment}")

name = 'J'
if len(name) < 3:
    print("name must be at least 3 characters.")
elif len(name) > 50:
    print("name must be at maximum 50 characters.")
else:
    print("name looks good! ")

i = 1
while i <= 5:
    i = i + 1
    print(i)

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won!')
        break
    else:
        print('please try again')

for item in range(5, 10, 2):
   print(item)

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
    print(total)

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

numbers = [5, 2, 5, 6, 8]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(6)
# numbers.clear()
numbers.pop()
print(numbers.index(5))
print(numbers)
print(50 in numbers)
print(numbers.count(5))
numbers.sort() #kucukten buyuge
numbers.reverse() #buyukten kucuge
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)

coordinates = [1, 2, 3]
x, y, z = coordinates
print(x*y*z)

customer = {
    "name" : "Sena Sabırlı",
    "age" : "21",
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate", "1 june"))

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}
output = ""
for ch in phone:
   output += digits_mapping.get(ch, "!")
print(output)

message = input(">")
words = message.split('  ')
emojis = {
    ":)": "🙃",
}
output = ""
for word in words:
   output += emojis.get(word, word) + " "
print(output)
#functions
def great_user():
    print('Hi there!')
    print("Welcome aboard")

print("Start")
great_user()
print("Finish")

#parameters
def greet_user(name):
    name = "Sena"
    print(f'Hi {name}!')
    print('Welcome aboard')

print('Start')
greet_user('Sena')
print("Finish")
"""
"""from mymodule import person1
def greeting(name):
mymodule.person1 = {
    "name":"John",
}
    print("Hello, " + name )"""


def e_number(start, end):
    for i in range(start, end):
        result = (1 + (1 / i)) ** i
        print(result)


def e_number_main():
    e_number(1, 12)


e_number_main()
