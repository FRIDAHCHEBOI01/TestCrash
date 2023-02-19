import turtle

color = input('''Please enter one of the following preferred background colors:
AliceBlue, AntiqueWhite, Aqua, Aquamarine, Azure, Beige, Biege, Bisque, BlanchedAlmond,
BlueViolet, CadetBlue, Chartruese, Chocolate, CornflowerBlue, Coral, Crimson, Cyan, DarkCyan,
DarkGoldenRod, DarkGray, DarkKhaki, DarkOliveGreen, DarkOrange, DarkOrchid,Darkred, Darksalmon,
Darkseagreen, Darkslate blue, darkslategrey, DarkTurquoise, Deep pink, Deep blue sky, Dimgray,
Dodgerblue, Firebrick, floralwhite, gold, goldenrod, gray, greenyellow,indianred, ivory, lavender,
khaki, lemonchiffon, lightcoral, lightblue, lightcoral, lightcyan, lightsalmon, lightseagreen,
lightpink, orange, orangered, orchid, palevioletred, peru, pink, plum, rebeccapurple, powderblue,
rosybrown, saddle brown, royalblue, thistle, teal, tan \n''')
''' Modules are object oriented'''
wn = turtle.Screen()
wn.bgcolor(color)

fridah = turtle.Turtle()
fridah.price = "Worth her weight in gold:)" # Fridah is an instance of a class, fridah.price is an instance variable 

i=1
while i<5:
    fridah.forward(25)
    fridah.penup()
    fridah.forward(25)
    fridah.pendown()
    fridah.forward(25)
    i+=1
    
devota = turtle.Turtle()
devota.begin_fill()
devota.color("royalblue")
devota.forward(100)
devota.left(90)
devota.forward(100)
devota.left(90)
devota.forward(100)
devota.left(90)
devota.forward(100)
devota.left(90)
devota.forward(100)
devota.end_fill()


cheboi = turtle.Turtle()
cheboi.color("gold")
cheboi.up()
cheboi.goto(100,100)
for i in range(3):
    cheboi.stamp()
    cheboi.forward(50)
    

wn.exitonclick()