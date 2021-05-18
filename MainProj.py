from tkinter.constants import CENTER, LEFT, TOP
import turtle
from time import sleep as wait
from numpy import NaN, nan
from playsound import playsound
import csv
import pandas as pd
import mysql.connector
import tkinter as tk
#-------------------------------------------------------------

window = turtle.Screen()
window.title("TEST BUILD 0.0.1")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)
#-------------------------------------------------------------
#-- Global Cursors

global text
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.hideturtle()


#-------------------------------------------------------------
#-------------------------------------------------------------
#-- Important methods

def clrscr():
    window.clear()
    window.bgcolor("black")
    window.tracer(0)

def tyeffect(write, speed = 0.15, alignment = "left", size = 30):
    x = ""
    for char in range(0,len(write)):
        x = x + write[char]
        text.write(x, align = alignment , font = ('courier', size ,'bold'))
        wait(speed)

#-------------------------------------------------------------
#-------------------------------------------------------------
def LoadingScreen():
    clrscr()
    text.goto(0,0)


    #- Draw the pattern, can be anything 
    drawer = turtle.Pen()
    colors = ["grey","silver","black"]  #-color sequence, change for some ebic stuff
    for i in range(360):
        drawer.pencolor(colors[i % 3])
        drawer.width(i/100 + 1)
        drawer.forward(i)
        drawer.left(59)

    tyeffect("Initializing..", speed = 0.12)


#-Transitioning
    wait(2)
    clrscr()
    playsound("Assets/Next.mp3")    
    wait(0.5)
    tyeffect("Welcome User", 0.07)
    wait(1)
    clrscr()
    WelcomeScreen()

#-------------------------------------------------------------
#-------------------------------------------------------------

def WelcomeScreen():

    text.goto(-350, 150)
    tyeffect("Enter Your Details Please", speed = 0.05)
    wait(.5)
    text.goto(-350, 100)
    text.write("Username = ", align = "left", font = ("courier",20, "bold"))
    text.sety(50)
    text.write("Password = ", align = "left", font = ("courier",20, "bold"))


    UserName = turtle.textinput("User Details", "Enter your username")
    playsound("Assets/Next.mp3")
    if UserName == "" or UserName == None:
        UserName = "Nil"
    text.sety(100)
    tyeffect("Username = " + UserName, size = 20, speed = 0.02)

    Password = turtle.textinput("User Details", "Enter your password")
    playsound("Assets/Next.mp3")
    if Password == "" or Password == None:
        Password = "Nil"
    text.sety(50)
    for char in range(0,len(Password)):
        texthid = "x" * (1 + char)
    tyeffect("Password = " + texthid, speed = 0.02, size = 20)

    Users = open("Data/Userdata.csv", "r")
    dict_reader = csv.DictReader(Users)
    order = list(dict_reader)[0]
    UserDict = dict(order)

    wait(1.5)
    try:
        if UserDict[UserName] == Password:
            clrscr()
            text.goto(0,0)
            tyeffect("Access Granted", speed= 0.1)
            wait(0.7)
            clrscr()
            tyeffect("Welcome, " + UserName)
            wait(1)
            playsound("Assets/Next.mp3")    
            MainScreen()
        else: 
            clrscr()
            text.goto(0,0)
            tyeffect("Access Revoked",  speed= 0.1)
            text.sety(-50)
            tyeffect("Invalid Details",  speed= 0.1)
            wait(1)
            clrscr()
            WelcomeScreen()
    except:
        clrscr()
        text.goto(0,0)
        tyeffect("Access Revoked",  speed= 0.1)
        text.sety(-50)
        tyeffect("Invalid Details",  speed= 0.1)
        wait(1)
        clrscr()
        WelcomeScreen()

    
def TESTSCREEN(x = nan,y = nan):
    def InputAdderThingy(x , y, df):
        rowName = input("add what -- ")
        age = input("value pls thank == ")
        cness = input("once again -- ")
        df2 = pd.Series({"Names" : rowName, "Age" : age, "Cuteness" : cness})

        df = df.append(df2, ignore_index = True)
        print("--" * 30)
        print("-- New DataFrame --")
        print(df)
        df.to_csv("Data/test.csv")

    clrscr()
    text.goto(-350,0)
    tyeffect("PONG!")
    text.sety(-50)
    tyeffect("Test dataframe created, check console", speed = 0.04, size = 10)

    df = pd.read_csv("Data/test.csv", header = 0, sep = ",")
    print(df)


    addEntryButton = turtle.Turtle()
    addEntryButton.shape("square")
    addEntryButton.color('red')
    addEntryButton.shapesize(2,2)
    addEntryButton.penup()
    addEntryButton.goto(0, 0)
    addEntryButton.onclick(lambda x, y: InputAdderThingy(x , y, df))
    window.update()

def MainScreen():
    clrscr()
    text.goto(-350,200)
    tyeffect("Choose what do you want to do", speed = 0.05)

    databasesbutton = turtle.Turtle()
    databasesbutton.shape("square")
    databasesbutton.color('red')
    databasesbutton.shapesize(2,2)
    databasesbutton.penup()
    databasesbutton.goto(0, 0)
    text.goto(0,14)
    text.write("TEST", align='center', font= ["courier", 20, 'bold'])
    databasesbutton.onclick(lambda x, y: TESTSCREEN(x,y))
    window.update()
    
#-------------------------------------------------------------
#-------------------------------------------------------------

#-- Start the car vroom vroom skrrt whoosh dabslhidawhv ;-;
LoadingScreen()
window.mainloop()
