print("Hello")
language="Python"

## String formating using .format
print("I am working on {language}".format(language=language))

## String formatting usong f string:
print(f"I am currently working on {language}")

##String method
var= "Hello all"
print(var.capitalize())

print(var.swapcase())
print(var.replace("all", "everyone"))
print(var.count("Hello i am python"))
print(var.split())
print(var.find("l"))
print(var.isalnum())


## Creating and working on list
lis=[1,2,3,4,5,6,7]
lis.remove(3)
print(lis)

new=lis.reverse()
print("execute")
print(new)
lis.append("Number")
print(lis)

dic={"Name":"Pratik",
     "Last_name":"Borse",
     "contact":9387629836}
print(dic)

print(dic.get("Name"))
dic["Name"]="Sahil"
print(dic)


dic["Address"]="New Mumbai"
print(dic) 

def sum(num1,num2=2):
    add=num1 + num2
    return add

print(sum(12,12))
print(sum(12))
print(sum(20,20))


#def sum(num1,num2):
#    add=num1 + num2
#    return add
#print(sum(12,12))


add=lambda a,b: a+b
print(add(2,2))
print("Hello")

x=8
y=20
if x>y:
    print(x)
else:
    print("x is less than y")


########################################
if x>2:
    if x<10:
        print(f"x is greater than 2 and less than or equal to {x}")
else:
    print("x is greater than 8 ")


person=["Pratik","Harshit","Sanket"]
for person in person:
    print(f"Person Name is { person}")

number=0
while number<5:
    print(f"Number is {number}")
    number += 1 


## importing modules

import datetime
from datetime import date

today=date.today()
print(today)

import time
from time import time

curr_time=time()
print(curr_time)

import json
key_val='{"F_Name":"Pratik","L_Name":"Borse","Designation":"Engg"}'
user=json.loads(key_val)
print(user)

