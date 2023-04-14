import turtle

maTortue = turtle.Turtle()

maTortue.getscreen().bgcolor("black")
maTortue.penup()
maTortue.goto(-200, 100)
maTortue.pendown()
maTortue.color("yellow")
maTortue.speed(25)

def etoile(tortue, taille):

	if taille <= 10:
		return
	else:
		tortue.begin_fill()
		for i in range(5):
			tortue.forward(taille)
			etoile(tortue, taille / 3)
			tortue.left(216)
			tortue.end_fill()


etoile(maTortue, 10)

turtle.done()
