import turtle
import math
bob = turtle.Turtle()
# so bob is the name of my object :) and it creates a turtle in the shape of an arrow on a window
'''
turtle_ is module
Turtle_is function in turtle module
function creates an object called bob

'''
#to move this turtle/arrow we need to create a method(similar to a function):)... we are requesting bob to move
'''
for i in range(3):
    bob.forward(100)
    bob.left(90)

bob.forward(100)
for i in range(3):
    bob.forward(100)
    bob.left(90)
bob.forward(100)
for i in range(3):
    bob.forward(100)
    bob.left(90)
for i in range(4):
    print("Hello")

bob.penup()
print(bob)
turtle.mainloop()
'''
'''
turtle.mainloop()
tells window to wait for me, the boss, to do sth
'''

def square(t,length):
    for i in range(4):
        t.forward(length)
        t.left(90)
def polygon(t,length,n):
    angle = 360/n
    for i in range(n):
        t.forward(length)
        t.left(angle)
def circle(t,radius):
    circumference = 2*math.pi*radius
    n = 50
    length = circumference/n
    polygon(t,n,length)
    
    
circle(bob,100)   

turtle.mainloop()   
