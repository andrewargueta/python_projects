import tkinter
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black','Yellow', 'Orange','Gray', 'Purple', 'Brown']
score = 0

timeleft = 30

gameStarted = False

random_text = 0

random_foreground = 0
startCountdown = False

def startGame(event):
    global gameStarted
    global startCountdown
    if not gameStarted:
        startCountdown = True
        countdown()
        gameStarted = True

    else:
        nextColor()

def reset(event):
    global timeleft
    global gameStarted
    global score
    timeleft = 30
    gameStarted = False
    startCountdown = False
    score = 0
    label.config(foreground='White', text='Game Over')
    timeLabel.config(text ="Time left: " + str(timeleft) )
    scoreLabel.config(text="Press 'Return' key to start")

def nextColor():
    global score
    global timeleft
    global random_text
    global random_foreground
    if timeleft > 0:

        input.focus_set()

        if colors[random_foreground].lower() == 'gray':
            if input.get().lower() == "grey" or input.get().lower() == "gray":
                score += 1
            else:
                score += 0
        elif input.get().lower() == colors[random_foreground].lower():
            score += 1
        else:
            score += 0


        input.delete(0, tkinter.END)

        random_text= random.randint(0, len(colors) - 1)
        random_foreground = random.randint(0, len(colors) - 1)

        label.config(foreground=str(colors[random_foreground]), text=str(colors[random_text]))


        scoreLabel.config(text="Score: " + str(score))










def countdown():
    global timeleft
    global startCountdown
    if startCoundown == True:
        if timeleft > 0:
            timeleft -= 1
            timeLabel.config(text="Time left: "   + str(timeleft))
            timeLabel.after(1000, countdown)
        else:
            label.config(foreground='Black', text='Game Over')




gameWindow = tkinter.Tk()


gameWindow.title("COLOR GAME")


gameWindow.geometry("375x200")


instructions = tkinter.Label(gameWindow, text="Type in the color of the word!",
                             font=('Helvetica', 12))
instructions.pack()


scoreLabel = tkinter.Label(gameWindow, text="Press 'Return' key to start",
                           font=('Helvetica', 12))
scoreLabel.pack()


timeLabel = tkinter.Label(gameWindow, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

label = tkinter.Label(gameWindow, font=('Helvetica', 60))
label.pack()


input = tkinter.Entry(gameWindow)



gameWindow.bind('<Return>', startGame)

input.pack()

input.focus_set()

enterButton = tkinter.Button(gameWindow, text = "Enter",  command = lambda:  startGame(None))
enterButton.pack()
resetButton = tkinter.Button(gameWindow, text = "Reset",  command = lambda:  reset(None))
resetButton.pack()

gameWindow.mainloop()

