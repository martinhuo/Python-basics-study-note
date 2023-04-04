# pop from list
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
print(list1.pop(2))

# remove from list
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
list1.remove(2)
print(list1)

# delete from list
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
del list1[1]
print(list1)

#append list

#insert to list

#replace element in list

#loop for list
list1 = ["ana","bnb","cnc"]
for name in list1:
    print(name.title())

#try yourself
animal_list = ["dog","cat","duck"]
for animal in animal_list:
    print("I like " + animal+"! \n")

#range function
for value in range(1,8):
    print(value)
list1 = list(range(1,8))
print(list1)

#create even number
even_number = list(range(2,15,2))
print(even_number)

#create square number
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#Statistics with list
number = [1,2,7,4,9,8,2,8,4,7,1,2,8,3,4,8,2]
print(min(number))
print(max(number))
print(sum(number))

#list comprehension

list1 = list(range(1,11))
squares = [values**2 for values in list1]
print(squares)

#or
squares = [values**2 for values in range(1,21)]
print(squares)

#Counting square:
print(list(values**2 for values in range(1,21)))

#count 1 to 1000000
list1 = list(range(1,1000001))
print(max(list1))
print(min(list1))
print(sum(list1))

#print 1 to 20 odd number
list1 = list(range(1,21,2))
for number in list1:
    print(number)

# multiples of 3
list1 = [values*3 for values in range(1,11)]
print(list1)

# first 10 cubes
list1 = [values**3 for values in range(1,11)]
for number in list1:
    print(number)

#slice of a list
#list slice��[x:y],x included��y not included
#first three elements
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
print(list1[:3])

#2 to 3 elements
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
print(list1[1:4])

#third element to the final one
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
print(list1[2:])

#print last three elements:
list1 = [1,2,6,3,5,2,7,4,2,8,4,7]
print(list1[-3:])

#use slice in loope
list_name = ['ansn','ajdn','djen','ajsjd','ajd','siej','dw','djwje']
for name in list_name[:5]:
    print("Hello, "+name.title()+"!")

#coppy list
list_name1 = ['ansn','ajdn','djen','ajsjd','ajd','siej','dw','djwje']
list_name2 = list_name1[:]
print(list_name2)

#slice exercise
name_list =  ['ansn','ajdn','djen','ajsjd','ajd','siej','dw','djwje']
print("The first three names are: "+str(name_list[:3])+".")
print("The middle names are: "+str(name_list[3:5])+".")
print("The last three names are: "+str(name_list[-3:])+".")

#tuple (immutable list)
tuple1 = (1,2,5,7,8,"tew")
print(tuple1[0])
print(tuple1)

#loope through tuple:
tuple1 = (1,2,5,7,8,"tew")
for elements in tuple1:
    print(elements)

#overwrite a tuple
tuple1 = (1,2,5,7,8,"tew")
print(tuple1)
tuple1 = (7,8,"tew")
print(tuple1)

#for ������һ��list�Ƿ�����һ��list��
student_name = ["Ben", "John", "Cathy", "Vrine", "Kline"]
student_list = ["Ben","Vrine", "Kline"]
for student in  student_name:
    for name in student_list:
        if student.lower() == name.lower():
            print("Hi "+student+", "+"congratulation!")

#inequality
answer =  7
if answer != 6:
    print("The answer " + str(answer) + " is wrong, try it again.") 

#mathmatical comparsion
age = 18
if age >= 18:
    print("You can enter the bar!")
elif age > 16:
    print("You can not enter the bar!")
elif age > 10:
    print("You are a child, please leave here")
else:
    print("!!!")

#check multiple conditions (and)
age = 18
name = "Chile"
sex = "female"
if age >= 18 and name == "Chile" and sex == "female":
    print("You can enter the bar!")

#check multiple condtions (or)
age = 17
name = "Ben"
sex = "female"
if age >= 18 or name == "Chile" or sex == "female":
    print("You can enter the bar!")

#for ������һ��Ԫ���Ƿ�����һ��list��,ʹ��in
student_list = ["Ben", "John", "Cathy", "Vrine", "Kline"]
student = "Ben"
if student  in student_list:
    print("You should come here")

#for ������not in
student_list = ["Ben", "John", "Cathy", "Vrine", "Kline"]
student = "Gigen"
if student  not in student_list:
    print("You should not come here")

#for ������һ��list�Ƿ�����һ��list��,ʹ��in
student_name = ["Ben", "John", "Cathy", "Vrine", "Kline"]
student_list = ["Ben","Vrine", "Kline"]
for student in  student_name:
    if student in student_list:
         print("Hi "+student+", "+"congratulation!")

#Boolean Expression
car = "BMW"
print("Is this car an Audi? "+"\nI predict true")
print(car == "Audi")

#omitting else 
age = 18
if age >= 18:
    print("You can enter the bar!")
elif age > 16:
    print("You can not enter the bar!")
elif age > 10:
    print("You are a child, please leave here")
elif age <= 10:
    print("!!!")

#check age
age = 35
if age < 2:
    print("you are a baby")
elif age < 4:
    print("you are a toddler")
elif age < 13:
    print("you are a kind")
elif age < 20:
    print("you are a teenager")
elif age < 65:
    print("you are a adult")
elif age > 65:
    print("you are a elder")

#application of if
required_toppings = ["mushrooms", "green peppers", "extra cheese"]
for toppings in required_toppings:
    print("Adding " + toppings + ". ")
print("Finished the piza!")

#checking  whether a list is empty
list1 = []
if list1:
    print(list1)
else:
    print("the list of empty")

#check user name
current_username = ["Ben", "Ann", "Gien", "Kile", "Curry", "Lens"]
new_username = ['Cathy','Ben']
for username in new_username:
    if username in current_username:
        print("Sorry, "+ username + " is not avaliable.")
    else:
        print(username + " is now registered!")

#ordinal number in a list
list1 = list(range(1,21))
for number in list1:
    if (number - (number//10)) == 1:
        print("This is the " + str(number) +"st "+ "number.")
    elif (number - (number//10)) == 2:
        print("This is the " + str(number) +"nd "+ "number.")
    elif (number - (number//10)) == 3:
        print("This is the " + str(number) +"rd "+ "number.")
    else: 
        print("This is the " + str(number) +"th "+ "number.")

#a simple dictionary
alien = {'color':'green', 'height':'5cm'}
print(alien['color'])

#add new key-value pair
alien = {'color':'green', 'height':'5cm'}
alien['x_position'] = 20
alien['y_position'] = 30
print(alien)

#add  key-value pair to an empty dictionary
alien = {}
alien['color'] = 'green'
alien['height'] = '5cm'
alien['x_position'] = 20
alien['y_position'] = 30
print(alien)

#modify values
alien = {'color':'green', 'height':'5cm'}
alien['color'] = 'yellow'
print(alien)

#change position of the alien
alien = {'color':'green', 'height':'5cm', 'x_position':20, 'y_position':30, 'speed':'medium'}
if alien['speed'] == "medium":
    position_increment = 10
elif alien['speed'] == "slow":
    position_increment =5
elif alien['speed'] == "fast":
    position_increment = 15
alien["x_position"] = alien["x_position"] + position_increment
print(alien["x_position"])

#remove key values
alien = {'color':'green', 'height':'5cm', 'x_position':20, 'y_position':30, 'speed':'medium'}
del alien["speed"]
print(alien)

#phonenumber collection
collection = {
    "Ben":"172838292", 
    "Ann":"132838292", 
    "John":"1723438292", 
    "Keli":"172834292", 
    "Peter":"152838292"
}
print(collection["John"])

#make a python dictionary
python_dictionary = {
    "string":"�ַ���",
    "intr":"��ֵ",
    "float":"������",
    "list":"�б�",
    "dictionary":"�ֵ�",
    }
print("string: "+python_dictionary["string"])

#looping through dictionary
user_system = {
    "Bendede":"172838292", 
    "Annaa":"132838292", 
    "John123":"1723438292", 
    "Keli":"172834292", 
    "Peter2":"152838292"
}
for user, password in user_system.items():
    print("Username: " +  user + "\nPassword: " + password)

#looping through all keys
user_system = {
    "Bendede":"172838292", 
    "Annaa":"132838292", 
    "John123":"1723438292", 
    "Keli":"172834292", 
    "Peter2":"152838292"
}
for user in user_system.keys():
    print(user)

#looping through all values
user_system = {
    "Bendede":"172838292", 
    "Annaa":"132838292", 
    "John123":"1723438292", 
    "Keli":"172834292", 
    "Peter2":"152838292"
}
for password in user_system.values():
    print(password)

#polling system
name_list = ["Ben","Ann","John","Keli","Peter","Elid"]
collection = {
    "Ben":"apple", 
    "Ann":"banana", 
    "John":"cherry", 
    "Keli":"peach", 
    "Peter":"lemon"
}
for name in name_list:
    if name not in collection.keys():
        print(name+", please take the poll!")

#Looping through keys in order
collection = {
    "Ben":"apple", 
    "Ann":"banana", 
    "John":"cherry", 
    "Keli":"peach", 
    "Peter":"lemon"
}
for name in sorted(collection.keys()):
    print(name+", thank you for taking the poll!")

#Looping through values:
collection = {
    "Ben":"apple", 
    "Ann":"banana", 
    "John":"cherry", 
    "Keli":"peach", 
    "Peter":"lemon"
}
print("Those are all fruite mentioned: ")
for fruit in collection.values():
    print(fruit)

#Looping through values in order:
collection = {
    "Ben":"apple", 
    "Ann":"banana", 
    "Keli":"peach", 
    "John":"cherry", 
    "Peter":"lemon"
}
print("Those are all fruite mentioned: ")
for fruit in sorted(collection.values()):
    print(fruit)

#exclude repeated value: eg find all typoes of foods mentioed (no repetition)
collection = {
    "Ben":"apple", 
    "Ann":"banana", 
    "Keli":"peach", 
    "Cath":"apple", 
    "Pene":"banana", 
    "Kil":"peach", 
    "John":"cherry", 
    "Peter":"lemon"
}
print("Those are all fruite mentioned: ")
for fruit in sorted(set(collection.values())):
    print(fruit)

#�ֵ��������ظ��� key,  ��ѯʱvalue���Ⱥ�һ��
collection = {
    "Ben":"banana", 
    "Ben":"apple", 
    "Ben":"peach"
}
print(collection['Ben'])

#poll system
favourite_lanuguage = {
    'jen':'python',
    'ben':'c',
    'john':'c++',
    'phil':'java',
    }
new = ["phil","david","alex"]
for name in new:
    if name not in favourite_lanuguage.keys():
        print("Hi "+name.title()+", please take the poll!")

#create a list of dictionary 
alien_0 = {'color':'green', 'points':'20'}
alien_1 = {'color':'yellow', 'points':'15'}
alien_2 = {'color':'red', 'points':'10'}
aliens = [alien_0, alien_1, alien_2]
for aliens in aliens:
    print(aliens)

#set number of dictionaries through list
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points':'20', 'speed':'fast'}
    aliens.append(new_alien)
# loop dictionary in list
for alien in aliens[0:10]:
    if alien['color']=="green":
        alien['color']="yellow"
        alien['speed']="medium"
        alien['points']=15
for alien in aliens:
    print(alien)

#a list in a dictionary
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese','pineapple'],
 }
print("Thank you for ordering a pizza with a "+ pizza["crust"] +" curst, and with follwing toppings:")
for toppings in pizza["toppings"]:
    print(toppings)

#a dictionary in a dictionary
user = {
    "Ben":{"real name": 'Peter Shame', 'location':'Newyork','age':'25'},
    "Peter":{"real name": 'Hushsi Kili', 'location':'Unknown','age':'20'},
    "John":{"real name": 'Pan John', 'location':'Atlanta','age':'18'}
    }
for username, userinfo in user.items():
    print(username + "\n"+ "\t"+"Real name: "+userinfo['real name']
          +"\n"+ "\t"+"Location: "+userinfo['location']+"\n"+ "\t"+"Age: "+userinfo['age'])
    print("\n")

#input����
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#personalize message
prompt = "If you tell us who you are, we can personalize the messages you see." + "\nWhat is your name?"
name = input(prompt)
print("Hi, "+name.title()+"!")

#using int() to accept numerical input
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You can enter the bar!")
else:
    print("Sorry, please leave")

#distinguish between odd and even number, %������modulo operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# �ַ���ת����,����ת����
print(float("0.2129"))
print(int(0.123))

#while loop 
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#letting user to choose when to quit
message = ""
while message.lower() != "quit":
    message = input("what do you want the computer to repeat?")
    print(message)

#quit due to one condition
message = ""
while message.lower() != "quit":
    message = input("what do you want the computer to repeat?")
    if message.lower() != "quit":
       print(message)

#add flag, quit due to several conditions
active = True
while active:
    message = input("what do you want the computer to repeat?")
    if message != "quit":
        print(message)
    else: 
        active = False

#using break to exit a loop 
while True:
    message = input("what do you want the computer to repeat?")
    if message != "quit":
        print(message)
    else: 
        break

#use continue in the loop (back to the begining of the loop)
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #back to current_number += 1 wihtout printing
    print(current_number)

#pizza topping
topping = input("What topping do you want")
if topping.lower() != "no":
    print("Add " + topping + " to your pizza!")
    active = True
    while active:
        topping = input("What other topping do you want?")
        if topping.lower() == "no":
            active = False
        else:
            print("Add " + topping + " to your pizza!")
    print("Thank you for your order!")
else:
    print("Thank you for your order!")

#pizza topping (using break)
topping = input("What topping do you want")
if topping.lower() != "no":
    print("Add " + topping + " to your pizza!")
    while True:
        topping = input("What other topping do you want?")
        if topping.lower() == "no":
            break
        else:
            print("Add " + topping + " to your pizza!")
    print("Thank you for your order!")
else:
    print("Thank you for your order!")

#while loop through a list
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#remove specific values (all)  from the list
pets = ['dog', 'cat', 'dog', 'goldfish','cat','cat', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary using while loop
responses = {}
poll_active = True
while poll_active:
    name = input("What is your name?")
    preference = input("what is your favoured food?")
    responses[name] = preference
    repeat = input("Has all people done the poll?")
    if repeat.lower() == "yes":
        poll_active = False
print(responses)

#define a function
def greet_user(username):
    print("Hello, "+username.title()+"!")

#positional argument (order matter)
def describe_pet(animal_type, pet_name):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#keyword argument (order does not matter)
def describe_pet(animal_type, pet_name):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name = "Ben", animal_type="Dog")

#default value, when one parameter is not entered, it will take the dedfault value
def describe_pet(pet_name, animal_type='dog'):
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet( "Ben")

#return a value
def get_formatted_name(first_name, last_name):
    full_name = first_name.title() +" "+ last_name.title()
    return full_name
print(get_formatted_name("Yuhao", "Huo"))

#Making an argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
print( get_formatted_name('john', 'hooker'))

#Return a dictionary
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
print(build_person('jimi', 'hendrix', age=27))

#using a function with a while loop
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("enter q to quit")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    if f_name == "q" or f_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#passing list (use a list as the input)
def greet_users(names):
    for name in names:
        print("Hello, " + name.title() + "!")
usernames = ['Ben', 'John', 'Tom']
greet_users(usernames)

#modifiying a list in a function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Preventing a Function from Modifying a List
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)

#take arbitary arguments 
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

#mix posittional and arbitary arguments
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#use arbitary keyword argument
def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(build_profile('albert', 'einstein', location='princeton', field='physics'))

#save function in the same directory then import it (pizza include several functions)
import pizza

#import a specific function
module_name.function_name()
from pizza import make_pizza as mp

#Importing all functions in a module
from pizza import *
from module_name import *

#class (initalize һ����˫�»���)
class Users():

    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname

    def summary(self):
        print("Name: " + self.fname.title() + " "+ self.lname.title())

    def greeting(self):
        print("Hi, " + self.fname.title() + " "+ self.lname.title() + "!" )

user1 = Users("Ben","Li")
user1.summary()
user1.greeting()

#setting a default value for an attribute
class Users():

    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
        self.level = "primary user"

    def summary(self):
        print("Name: " + self.fname.title() + " "+ self.lname.title() + "\nLevel: " + "primary user")

    def greeting(self):
        print("Hi, " + self.fname.title() + " "+ self.lname.title() + "!" )

user1 = Users("Ben","Li")
user1.summary()
user1.greeting()

#modifying an attributes value through a method
class Car():
    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age
        self.meter = 0

    def updatemeter (self, meter):
        if meter < self.meter:
            print("You can't roll back an odometer!")
        else:
            self.meter = meter
            print("update " + str(meter))

#create a child class
class Car():
    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age
        self.meter = 0

    def updatemeter (self, meter):
        if meter < self.meter:
            print("You can't roll back an odometer!")
        else:
            self.meter = meter
            print("update " + str(meter))

    def describecar (self):
        print(self.brand, self.model, self.age, self.meter)

class Electriccar(Car):
    def __init__(self, brand, model, age, battery):
        super().__init__(brand, model, age)
        self.battery = battery

    def batteryage (self):
        print(self.battery)

mycar = Electriccar("Tesla", "modelx", 2,3)

#use class in class
class Car():

    def __init__(self, brand, model, age):
        self.brand = brand
        self.model = model
        self.age = age
        self.meter = 0

    def updatemeter (self, meter):
        if meter < self.meter:
            print("You can't roll back an odometer!")
        else:
            self.meter = meter
            print("update " + str(meter))

    def describecar (self):
        print(self.brand, self.model, self.age, self.meter)

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = self.battery_size*80
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class Electriccar(Car):

    def __init__(self, brand, model, age, batterysize):
        super().__init__(brand, model, age)
        self.battery = Battery(batterysize)

    def batteryage (self):
        print(self.battery)

mycar = Electriccar("Tesla", "modelx", 2,3)

#open function open a file and retun it as a class, with ensures that the file will be closed after operation
with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents)

#relative path(the folder where the file locate should be in the same directory as the python file)
with open(r'C:\Users\huohh\Desktop\file1\pi.txt') as file_object:
    contents = file_object.read()
    print(contents)

#read lines of txt (will have extra space lines \n)
with open(r'C:\Users\huohh\Desktop\file1\pi.txt') as file_object:
    for line in file_object:
        print(line)

#rstrip to eliminate space lines
with open(r'C:\Users\huohh\Desktop\file1\pi.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#store lines as a list
with open(r'C:\Users\huohh\Desktop\file1\pi.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#store lines as a stirng
with open(r'C:\Users\huohh\Desktop\file1\pi.txt') as file_object:
    lines = file_object.readlines()

content = ''

for line in lines:
    content += line.strip()
print(content)

#create an empty file and wite in it
with open(r'C:\Users\huohh\Desktop\file1\try.txt', 'w') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

#if error may occur, write a try-except block!
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#make a calculator
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = print(int(first_number) / int(second_number))
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

#handle file not found error
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    print(content)

#fail silently
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    pass
else:
    print(content)

#storing data in json 
import json
numbers = [2, 3, 5, 7, 11, 13]
filepath = r'C:\Users\huohh\Desktop\file1\number.json'
with open(filepath, 'w') as f_obj:
    json.dump(numbers, f_obj)

#open json file
import json
filepath = r'C:\Users\huohh\Desktop\file1\number.json'
with open(filepath) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

#save user input data
import json
username = input("What is your name? ")
filename = r'C:\Users\huohh\Desktop\file1\username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
print("We'll remember you when you come back, " + username + "!")

#read user input data
import json
filename = r'C:\Users\huohh\Desktop\file1\username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

#welcome back!
import json
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

#refactroing code
import json
filename = 'username.json'

def find_stored_username():
    with open(filename) as f_obj:
        username = json.load(f_obj)

def ask_for_username():
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")

def greet_user():
    try:
        find_stored_username()
    except FileNotFoundError:
        ask_for_username()
    else:
        print("Welcome back, " + username + "!")

greet_user()

#test code
'''assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list'''
