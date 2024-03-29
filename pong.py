import turtle

#Ventana del juego
vn = turtle.Screen()
vn.title("Juego Pong By Jhonny")
vn.bgcolor("black")
vn.setup(width = 800, height = 600)
vn.tracer(0)

#Primer jugador
jugador1 = turtle.Turtle()
jugador1.speed(2)
jugador1.shape("square")
jugador1.color("white")
jugador1.penup()
jugador1.goto(-350,0)
jugador1.dy = 2
jugador1.shapesize(stretch_wid=5, stretch_len = 1)

#Segundo jugador
jugador2 = turtle.Turtle()
jugador2.speed(2)
jugador2.shape("square")
jugador2.color("white")
jugador2.penup()
jugador2.goto(350,0)
jugador2.shapesize(stretch_wid=5, stretch_len = 1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 2
pelota.dy = 2

#Linea divisora
division = turtle.Turtle()
division.color("white")
division.goto(0, 400)
division.goto(0, -400)

#Marcador
marcador1 = 0
marcador2 = 0

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260) 
pen.write("Jugador-1: 0		Jugador-2: 0",align = "center", font=("Times New Roman", 24, "normal"))

#Funciones incluidas
def jugador1_up():
    y = jugador1.ycor()
    y += 50
    jugador1.sety(y)

def jugador1_down():
    y = jugador1.ycor()
    y -= 50
    jugador1.sety(y)

def jugador2_up():
    y = jugador2.ycor()
    y += 50
    jugador2.sety(y)

def jugador2_down():
    y = jugador2.ycor()
    y -= 50
    jugador2.sety(y)

#Teclado
vn.listen()
vn.onkeypress(jugador1_up, "w")
vn.onkeypress(jugador1_down, "s")
vn.onkeypress(jugador2_up, "Up")
vn.onkeypress(jugador2_down, "Down")

while True:
    vn.update()

    pelota.setx(pelota.xcor() - pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

    #Bordes de arco de anotacion
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador1 += 1
        pen.clear()
        pen.write("Jugador-1: {}		Jugador-2: {}".format(marcador1,marcador2), align = "center", font=("Times New Roman", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador2 += 1
        pen.clear()
        pen.write("Jugador-1: {}		Jugador-2: {}".format(marcador1,marcador2), align = "center", font=("Times New Roman", 24,  "normal"))

    #Colisiones (Golpes de defensa)
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugador2.ycor() + 50
            and pelota.ycor() > jugador2.ycor() - 50)):
        pelota.dx *= -1
        pelota.dy *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugador1.ycor() + 50
            and pelota.ycor() > jugador1.ycor() - 50)):
        pelota.dx *= -1
        pelota.dy *= -1