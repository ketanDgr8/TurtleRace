import random
from turtle import Turtle, Screen
from random import randint

t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")

t=Turtle()

screen = Screen()
screen.setup(500, 400)


t.left(90)
t.penup()
t.goto(-210,-200)
t.pendown()
t.forward(400)


t.left(180)
t.penup()
t.goto(210,200)
t.pendown()
t.forward(400)

user_bet = screen.textinput(title="Make your Bet Sumaira", prompt="Which Turtle will Win? Enter Colour")
t1.color(user_bet)
user_bet = screen.textinput(title="Make your Bet Sadhika", prompt="Which Turtle will Win? Enter Colour")
t2.color(user_bet)
user_bet = screen.textinput(title="Make your Bet Rudra", prompt="Which Turtle will Win? Enter Colour")
t3.color(user_bet)
user_bet = screen.textinput(title="Make your Bet Ketan", prompt="Which Turtle will Win? Enter Colour")
t4.color(user_bet)
user_bet = screen.textinput(title="Make your Bet Jyoti", prompt="Which Turtle will Win? Enter Colour")
t5.color(user_bet)

t1.penup()
t1.goto(-240, 80)
t1.write("Sumaira")

t2.penup()
t2.goto(-240, 180)
t2.write("Sadhika")

t3.penup()
t3.goto(-240, -80)
t3.write("Rudra")

t4.penup()
t4.goto(-240, -180)
t4.write("ketan")

t5.penup()
t5.goto(-240, 0)
t5.write("Jyoti")


move_forward = True

while move_forward is True:
    t1.forward(random.randint(1,30))
    t2.forward(random.randint(1,30))
    t3.forward(random.randint(1,30))
    t4.forward(random.randint(1,30))
    t5.forward(random.randint(1, 30))


    if t1.xcor() >= 210:
        screen.title("Sumaira Wins")
        move_forward=False
    elif t2.xcor() >= 210:
        screen.title("Sadhika Wins")
        move_forward = False
    elif t3.xcor() >= 210:
        screen.title("Rudra Wins")
        move_forward = False
    elif t4.xcor() >= 210:
        screen.title("Ketan Wins")
        move_forward = False
    elif t5.xcor() >= 210:
        screen.title("Jyoti Wins")
        move_forward = False



screen.exitonclick()
