
from tkinter import *
import ctypes
import random
import tkinter
 
# Setup
root = Tk()
root.title('Type Speed Test')

# Setting the starting window dimensions
root.geometry('700x700')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")
# For a sharper window
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def resetWritingLabels():
    # Text List
    possibleTexts = [
        'Пес-одиночка Счастливчик вырывается из Западни-дома для бездомных собак, когда начинается ужасное землетрясение.В разрушенном и обезлюдевшем городн он  встречает бывших домашних псов, оставленных хозяевами на гибель без еды.',
        'Счастливчик и Альфа - вожак Дикой стаи - наконец достигают в отношениях хрупкого согласия, однако Альфа однозначно дает понять, что некоторых собак он никогда ни за что не признает и не сделает их членами своей стаи. Стая вновь отправляется в путь в поисках нового безопасного дома как можно дальше от Сада Свирепых Псов и ее вожака стаи.Но опасность подстерегает повсюду.Когда путешественники  встречают других собак, выживших после землетрясения , смерть вновь подбирается в Счастливчику и его друзьям.Вожак новой стаи, безумный кровожадный пес Ужас.',
        'После того как, Альфа-полуволк предал свою стаю, а его место заняла Лапочка, у дикой стаи наконец-то появилась возможность вздохнуть спокойно и начать новую жинзнь на новой территории, но опасности продолжают преследовать друзей.В пустой город возвращаются люди, а в скалах рядом с дикими собаками, покинув прежнее логово, поселяется свирепая стая.Не успевают собаки придумать, как противостоять врагам, бескрайнее оезро в гневе обрушивается на берег после землетрясения,грозя уничтожить все живоею'
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()
    splitPoint = 0
    # This is where the text is that is already written
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Here is the text which will be written
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # this label shows the user how much time has gone by
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amountWords = len(labelLeft.cget('text').split(' '))

    # Destroy all unwanted widgets.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()
    
        # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    # Destry result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

        # re-setup writing labels.
    resetWritingLabels()

def addSecond():
    # Add a second to the counter.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        root.after(1000, addSecond)

def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass

# This will start the Test
resetWritingLabels()

# Start the mainloop
root.mainloop()