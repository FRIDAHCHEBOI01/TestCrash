import turtle                   # allows us to use the turtles library 

wn = turtle.Screen()            # creates a graphics window 
wn.bgcolor("black")
heart = turtle.Turtle()# create a turtle named myturtle 

heart.penup()
heart.left(90)
heart.forward(200)
heart.right(90)
heart.pendown()
heart.color("red")
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

      
                               # 'circle', 'square', 'triangle', 'classic' 


wn.exitonclick()                # Closes program when user clicks in the window 