
from operator import index
import turtle
import time
import random

delay = 0.1
#score variables
score = 0 
high_score = 0 

#screen setup
wn = turtle.Screen()
wn.title("Snake Game by Mennah")
wn.bgcolor("purple")
wn.setup(width=600, height=600) 
wn.tracer(0)  #Turnes of screen updates 

#snack head 
head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

#the food
food= turtle.Turtle()
colors = random.choice(['pink', 'green'])
shapes = random.choice(['triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
colors = ('pink')
shapes = ('circule')
food.penup()
food.goto(0,100)

#pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score:0  High Score:0" , align="center" , font=("Courier" , 24 , "normal"))

#functions
def go_up():
    head.direction='up'
def go_down():
    head.direction='down'
def go_left():
    head.direction='left'
def go_right():
    head.direction='right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings
wn.listen()   
wn.onkeypress(go_up , "w")    
wn.onkeypress(go_down , "s") 
wn.onkeypress(go_left , "a") 
wn.onkeypress(go_right , "d") 

#import a list
segments = []

#main game loop
while True:
    wn.update()
    #border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        colors = random.choice(['pink', 'green'])
        shapes = random.choice(['triangle', 'circle'])
    
        #hide segments
        for segment in segments:
            segments.goto(1000,1000)
        #clear segments list
        segments.clear() 

        #to reset the score
        score =0   
        # to reset the delay
        delay = 0.1 

        pen.clear()   
        pen.write("Score: {}  High Score: {} ".format(score, high_score) , align="center" , font=("Courier" , 24 , "bold"))


    #food collision    
    if head.distance(food) < 20 : 
        #Here food moves randomly 
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        #for the tail color
        new_segment.color("gray")  
        new_segment.penup()
        segments.append(new_segment)


        #shorten any-delay
        delay -= 0.001
        #increasing the score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()   
        pen.write("Score: {}  High Score: {} ".format(score, high_score) , align="center" , font=("Courier" , 24 , "bold"))    

    #move the last to the front
    for index in range (len(segments) -1 , 0 , -1 ):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto( x , y )

    #move segment zero to where the head is 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y) 

#section check

    move()

#collision with body segments
    for segment in segments:
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            colors = random.choice(['pink', 'green'])
            shapes = random.choice(['triangle', 'circle'])

            #hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            #clear segments list
            segments.clear()

            #to reset the score
            score =0   
            # to reset the delay
            delay= 0.1
            #update the score display
            pen.clear()   
            pen.write("Score: {}  High Score: {} ".format(score, high_score) , align="center" , font=("Courier" , 24 , "bold"))


    time.sleep(delay)


wn.mainloop()

