import turtle as t
import random as rd

t.bgcolor('pink')

kachua = t.Turtle()
kachua.shape('turtle')
kachua.speed(0)
kachua.penup()
kachua.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,16),(2,15))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press space to start', align='center', font = ('Arial',18,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
	left_wall = -t.window_width()/2
	right_wall = t.window_width()/2
	top_wall= t.window_height()/2
	bottom_wall= -t.window_height()/2
	(x,y) = kachua.pos()
	outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
	return outside

def place_leaf():
	leaf.hideturtle()
	leaf.setx(rd.randint(-200,200))
	leaf.sety(rd.randint(-200,200))
	leaf.showturtle()

def game_over():
	kachua.color('yellow')
	leaf.color('yellow')
	t.penup()
	t.hideturtle()
	t.write("GAME OVER !", align = 'center', font = ('Arial',30,'normal'))


def display_score(current_score):
	score_turtle.clear()
	score_turtle.penup()
	x = (t.window_width()/2) -50
	y = (t.window_height()/2) -50
	score_turtle.setpos(x,y)
	score_turtle.write(str(current_score), align = 'right', font = ('Arial',40,'bold'))

def start_game():
	global game_started
	if game_started:
		return
	game_started = True
	score = 0
	text_turtle.clear()

	kachua_speed = 2
	kachua_length = 3
	kachua_width = 1
	kachua.shapesize(1,kachua_length,1)
	kachua.showturtle()
	display_score(score)
	place_leaf()

	while True:
		kachua.forward(kachua_speed)
		if kachua.distance(leaf) < 20:
			place_leaf()
			kachua_length = kachua_length + 1
			kachua.shapesize(kachua_width,kachua_length,1)
			kachua_speed = kachua_speed +1
			kachua_width = kachua_width + 1
			score = score + 10
			display_score(score)
		if outside_window():
			game_over()
			break


def move_up():
    if kachua.heading() == 0 or kachua.heading() == 180:
        kachua.setheading(90)

def move_down():
    if kachua.heading() == 0 or kachua.heading() == 180:
        kachua.setheading(270)

def move_left():
    if kachua.heading() == 90 or kachua.heading() == 270:
        kachua.setheading(180)

def move_right():
    if kachua.heading() == 90 or kachua.heading() == 270:
        kachua.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()
