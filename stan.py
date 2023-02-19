import turtle

wn = turtle.Screen()
wn.bgcolor("DarkGoldenRod")
 
stan = turtle.Turtle()
stan.color("lightcoral")
stan.shape("square")

dist = 5
stan.up()

while dist <=100:
    stan.speed(10)
    stan.stamp()
    stan.forward(dist)
    stan.left(20)
    dist += 1

stan.forward(50)

lovu = turtle.Turtle()
lovu.shape("turtle")
lovu.up()
lovu.stamp()
#repeat the below 10 times 
#go forward50
#reverse50
#turn right36



for i in range(10):    
    lovu.forward(50)
    lovu.stamp()
    lovu.forward(-50)
    lovu.right(40)
    
for i in range(10):    
    lovu.forward(100)
    lovu.stamp()
    lovu.forward(-100)
    lovu.right(40)
    
for i in range(10):    
    lovu.forward(150)
    lovu.stamp()
    lovu.forward(-150)
    lovu.right(40)
for i in range(10):    
    lovu.forward(200)
    lovu.stamp()
    lovu.forward(200)
    lovu.right(40)
for i in range(10):    
    lovu.forward(250)
    lovu.stamp()
    lovu.forward(250)
    lovu.right(40)    
    
wn.exitonclick()
