import turtle

wn = turtle.Screen()
wn.bgcolor("purple")
wn.setup(width = 1000,height = 900)
heart = turtle.Turtle()# create a turtle named myturtle 

heart.penup()
heart.left(90)
heart.forward(200)
heart.right(90)
heart.pendown()
heart.color("pink")
heart.begin_fill()
heart.speed(10)
heart.shape("turtle")
heart.pensize(3)
heart.left(120)
heart.forward(100)
heart.circle(-90,180)
heart.left(120)
heart.circle(-90,180)
heart.forward(300)
heart.right(117)
heart.forward(200)
heart.end_fill()

lf = turtle.Turtle()
lf.color("white")
lf.penup()
lf.forward(-150)
lf.pendown()

lf.forward(100)
lf.forward(-100)
lf.right(90)
lf.forward(100)
lf.left(90)
lf.forward(100)
lf.forward(-100)
lf.right(90)
lf.forward(100)

lc = turtle.Turtle()
lc.color("black")
lc.pensize(4)
lc.penup()
lc.left(90)
lc.forward(100)
lc.pendown()

lc.right(90)
lc.forward(100)
lc.forward(-100)
lc.right(90)
lc.forward(200)
lc.left(90)
lc.forward(100)

la = turtle.Turtle()
la.pensize(3)
la.color("hotpink")
la.penup()
la.forward(150)
la.pendown()
la.right(105)
la.forward(200)
la.left(180)
la.forward(100)
la.right(75)
la.forward(50)
la.left(105)
la.forward(100)
la.right(180)
la.forward(200)

lt = turtle.Turtle()
lt.color("yellow")
lt.pensize(2)
lt.penup()
lt.forward(250)
lt.pendown()

lt.forward(100)
lt.forward(-50)
lt.right(90)
lt.forward(200)



wn.exitonclick()