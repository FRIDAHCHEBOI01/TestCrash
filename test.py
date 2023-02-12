import math
#strings, int and float are immutable ie. 
string1 = "Fridah Cheboi"
print(string1.__len__())
# What did you say classes are?
# I have learnt something really interesting today
print(string1.index("F")) #gives value error when character is not found
print(string1.find("K")) #returns value error when character in not found
print(string1[1])
print(string1[0:5])#Slicing does not include the end index
string2 = string1.replace("F","B")
number1 = 10
float1 = 0.1
bool = True 
bool2 = False 

#lists are immutable ie. values can be changed on the same variable
list1 = [1,2,3,4,5]
me = ["Brilliant","Blessed","Brave","Breaking even"]
print(me[0:2])
me.append("Great")
me.extend(["Awesome","Best of all time!!!"])
print(me)
list1.insert(0, "There's me")
print(list1)
#dictionaries
map1 = {"a":"Zero", "b":"One", "c":"Two", "d":"Three"}
print(map1["a"])

#A tuple is immutable
tuple1 = (1,2,3,4,5,6)

#type conversion
entry = int(input("Please enter number"))
print(entry + 5)

#Order of operations
#Division: To find the total number 0f hours, minutes and seconds in 50000 seconds
num = 50000
hours  = num//3600
rem = num%3600
minutes = rem// 360
seconds = rem%360
print(hours, minutes, seconds)
#Decision making: if, elif, else 
