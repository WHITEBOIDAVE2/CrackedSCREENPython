def square( t, distance ):
    for times in range(3):
        t.forward(100)
        t.left(90)

def triangle( t, distance ):
    for times in range(3):
        t.forward(100)
        t.left(120)

def polygon( t, distance, side ):
    angle = 360/side
    for times in range(side):
        t.forward(distance)
        t.left(angle)

def pentagon( t, distance, side ):
    angle = 360/side
    for times in range(side):
        t.forward(distance)
        t.left(angle)

def move(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
