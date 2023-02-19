import turtle

wn = turtle.Screen()
wn.bgcolor("teal")

melody = turtle.Turtle()
melody.color("thistle")
melody.shape("classic") #can be a triangle, circle, square, classic, arrow, or turtle even blank

melody.up()
melody.goto(10,100)
melody.backward(100)
melody.stamp()

owadd = turtle.Turtle()
owadd.color("darkorange")
owadd.speed(10) # 1=slowest to 10=very fast, 0=no animation

owadd.penup()
owadd.forward(-100)
owadd.pendown()
owadd.dot()
owadd.left(90)
owadd.penup()
owadd.forward(100)
owadd.pendown()
print(owadd.position)
print(owadd.heading)



wn.exitonclick()