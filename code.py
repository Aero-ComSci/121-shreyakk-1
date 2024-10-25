# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
from turtle import Screen
import random as rand
wn = Screen()
wn.screensize(canvwidth=800, canvheight=800)
wn.bgcolor('red')
#-----game configuration----
circolor = 'lightpink'
circshape = 'turtle'
global score
score = 0 
timer = 30
timer_up = False
counter_interval = 1000
font_setup = ("Arial", 20, "normal")
#-----initialize turtle-----
t= trtl.Turtle()
t.shape(circshape)
t.fillcolor(circolor)
t.shapesize(3)
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
counter.penup()
counter.goto(10,300)
counter.pendown()
#-----game functions--------
def spot_clicked(x, y):
    global timer, timer_up
    if timer_up == False: 
        change_position()
        updatescore()
        countdown()
    else: 
       countdown()
       t.hideturtle()
    
    

t.onclick(spot_clicked)
def change_position():
    new_xpos = rand.randint(0,400)
    new_ypos = rand.randint(0,400)
    t.penup()
    t.goto(new_xpos, new_ypos)
    t.pendown()
    t.shapesize(rand.randint(1,10))
def updatescore():
    score_writer.clear()
    global score 
    score+=1
    score_writer.write(score,font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("game over!", font=font_setup)
    timer_up = True
  else:
    counter.write("time left: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
    


#-----events----------------

wn.mainloop()
