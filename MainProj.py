import turtle
from time import sleep as wait
from playsound import playsound
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
text.ht()

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

    drawer = turtle.Pen()
    colors = ["grey","silver","black"]
    for i in range(360):
        drawer.pencolor(colors[i % 3])
        drawer.width(i/100 + 1)
        drawer.forward(i)
        drawer.left(59)

    tyeffect("Initializing..", speed = 0.12)


    wait(2)
    clrscr()
    playsound("Assets/Next.mp3")    
    wait(0.5)
    WelcomeScreen()

#-------------------------------------------------------------
#-------------------------------------------------------------

def WelcomeScreen():

    tyeffect("Welcome User", 0.07)
    wait(1)
    clrscr()

    text.goto(-350, 150)
    tyeffect("Enter Your Details Please", speed = 0.05)

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
    texthid = ""
    for char in range(0,len(Password)):
        texthid = "x" * char


    tyeffect("Password = " + texthid, speed = 0.02, size = 20)

#-------------------------------------------------------------
#-------------------------------------------------------------

LoadingScreen()
