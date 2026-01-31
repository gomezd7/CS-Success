# Final Project
# CS 111, Hayes & Reckinger
# Deicy Gomez & Avril Arroyo

import turtle
import random
import time

global score
global character
global charNotSelected
global answer
global bNotSelected
global levelSelected
score = 0
    
# funtion to choose character 
def choose(x, y):
    global charNotSelected
    global char_str
    if x < 0:
        char_str = "girl.gif"
    else:
        char_str = "boy.gif"
    charNotSelected = False

def choose_answer(x, y):
    global bNotSelected
    global answer
    global score
    if x < 0:
        answer = "yes"
        score += 1
    else:
        answer = "no"
    bNotSelected = False

    answer += str(score)

#function to check if building is clicked 
def building_click2(x,y):
    global levelSelected
    for building in building_list:
        if building.distance(x,y) < 30:
            return True
    return False

def building_click(x,y):
    global levelSelected
    levelSelected = building_click2(x,y)
   
#function to add buttons 
def add_buttons():
    buttons = ["yes.gif", "no.gif"]
    buttons_list = []
    x = -100
    for i in range(2):
        turtle.addshape(buttons[i])
        b = turtle.Turtle()
        b.hideturtle()
        buttons_list.append(b)
        b.shape(buttons[i])
        b.penup()
        b.goto(x, -200)
        b.showturtle()
        x = x + 200
    return b

#background images for level 
def level_background(level):
    bg_list = ["1question1.gif", "1question2.gif", "2question1.gif", "2question2.gif", "3question1.gif", "3question2.gif", "4question1.gif", "4question2.gif", "5question1.gif", "5question2.gif"]
    count = 1
    first = f"{level}question{count}.gif"
    count += 1
    second = f"{level}question{count}.gif"
    return first, second

#function to hide the character 
def hide_character():
    character.hideturtle()

# function to play the level 
def play_level(level):
    global char_str
    global bNotSelected
    global button
    global score

 #clear screen and set up the bg 
    s.clearscreen()
    turtle.hideturtle()
    screen = turtle.getscreen()
    screen.setup(683+10, 512+10)
    first, second = level_background(level)
    screen.bgpic(first)
    button = add_buttons()
    bNotSelected = True

 #button click to choose an answer 
    while bNotSelected:
        button.onclick(choose_answer)
    # clear the button 
    button.clear()
    button.hideturtle()
    s.clearscreen()
    s.update()
    # Set up the bg 
    screen.bgpic(second)
    button = add_buttons()
    bNotSelected = True
    while bNotSelected:
        button.onclick(choose_answer)
    button.clear()
    button.hideturtle()
    s.clearscreen()
    s.update()   

#movement of character 
def up():
    global character
    character.setheading(90)
    character.forward(10)

def down():
    global character
    character.setheading(270)
    character.forward(10)

def left():
    global character
    character.setheading(180)
    character.forward(10)

def right():
    global character
    character.setheading(0)
    character.forward(10)

######################################################
#  SCREEN 1 - welcome page
######################################################
#sets up screen
s =turtle.Screen()
s.title("Welcome Screen")
s.setup(683 + 10,512 + 10)
s.bgcolor("white")
s.bgpic("welcome.gif")
s.update()
time.sleep(3)

######################################################
#  SCREEN 2 - instructions page
######################################################
s.bgpic("instructions_page.gif")
s.update()
time.sleep(15)
s.clearscreen()

######################################################
#  SCREEN 3 - character choice
######################################################

#set up turtles
characters = ["girl.gif", "boy.gif"]
turtles = []
text = turtle.Turtle()

s.clearscreen()
s.bgpic("choose_char_screen.gif")

text.penup()
text.hideturtle()
text.goto(0, 100)
text.color("white")
text.write("Choose your character!", False, align='center', font=('Oswald', 30, 'bold'))
x = -50
turtle.tracer(False)
for i in range(0, len(characters)):
    turtle.addshape(characters[i])
    c = turtle.Turtle()
    turtles.append(c)
    c.shape(characters[i])
    c.penup()
    c.goto(x, -20)
    x = int(x) + 170
turtle.tracer(True)

s.listen()
charNotSelected = True
while charNotSelected:
    turtles[0].onclick(choose)
    turtles[1].onclick(choose)

s.clearscreen()

######################################################
#  SCREEN 4 - map screen
######################################################
buildings = ["ses.gif", "sele.gif", "sce.gif", "library.gif", "seo.gif"]
coor_list = [(0, -190), (200, -30), (200, 150), (-200, 150), (-200, -10)]
building_list = []

turtle.tracer(False)

#building set up 
for i in range(0, len(buildings)):
    turtle.addshape(buildings[i])
    bd = turtle.Turtle()
    building_list.append(bd)
    bd.shape(buildings[i])
    bd.hideturtle()
    bd.penup()
for i in range(0, len(building_list)):
    bd.penup()
    x,y = coor_list[i]
    building_list[i].goto(x,y)

turtle.tracer(True)
######################################################
#  SCREEN 5 - levels and map screen
######################################################
s.bgpic("backgroundmain.gif")

character = turtle.Turtle()
character.shape(char_str)
character.penup()
character.goto(-250, -160)
s.listen()
s.onkey(up, "Up") 
s.onkey(down, "Down")
s.onkey(left, "Left")
s.onkey(right, "Right")

# playing each level
for level in range(1,6):
    levelSelected = True
    s.listen()
    s.onkey(up, "Up") 
    s.onkey(down, "Down")
    s.onkey(left, "Left")
    s.onkey(right, "Right")
    s.onscreenclick(building_click)

    #waiting for the level to complete 
    while levelSelected:
        s.update()

    #characters last position 
    last_position = character.pos()
    character.hideturtle()
    play_level(level)
    s.bgpic("backgroundmain.gif")
    character = turtle.Turtle()
    character.shape(char_str)
    character.penup()
    character.goto(last_position)
    character.showturtle()
    s.listen()
    s.onkey(up, "Up") 
    s.onkey(down, "Down")
    s.onkey(left, "Left")
    s.onkey(right, "Right")  
    s.onscreenclick(building_click)

#hides character before results 
hide_character()

#user results
if score>=5:
    s.bgpic("successful.gif")  
else:
    s.bgpic("notsuccessful.gif")
    s.update()

turtle.hideturtle()
# turtle.mainloop()
