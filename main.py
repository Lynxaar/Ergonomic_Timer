import time
from tkinter import *
from tkinter import messagebox as message_window
import random

# Creates the interface object
clockWindow = Tk()
clockWindow.geometry("400x400")
clockWindow.title("Ergonomic Timer")
clockWindow.configure(background='steel blue')
clockWindow.resizable(height = False,width = False)

#Label for textboxes
seconds = Label(clockWindow, text="sec", bg="steel blue").place(x=230, y=220)
minutes = Label(clockWindow, text="mins", bg="steel blue").place(x=175, y=220)
hours = Label(clockWindow, text="hours", bg="steel blue").place(x=125, y=220)

# Declares variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

# Set strings to default value
hourString.set("00")
minuteString.set("00")
secondString.set("00")

# Gets user input
hourTextbox = Entry(clockWindow, width=3, font=("Helvtica", 20, ""), textvariable=hourString)
minuteTextbox = Entry(clockWindow, width=3, font=("Helvtica", 20, ""), textvariable=minuteString)
secondTextbox = Entry(clockWindow, width=3, font=("Helvtica", 20, ""), textvariable=secondString)

# Centers textboxes
hourTextbox.place(x=125, y=250)
minuteTextbox.place(x=175, y=250)
secondTextbox.place(x=225, y=250)

# This defines the function when Set Time is clicked
def runTimer():
   global label
# Gets the value from the user into a seconds integer and multiplies that by 3600 for hour and 60 for minutes
   try:
       clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
# If the user enters an invalid input, run an exception block
   except:
       print("Incorrect values")
# Takes the user input and returns 2 values giving the quotient in the seconds textbox
   while(clockTime > -1):
       totalMinutes, totalSeconds = divmod(clockTime, 60)

       totalHours = 0
       if(totalMinutes > 60):
           totalHours, totalMinutes = divmod(totalMinutes, 60)
# Stores the value up to two decimal places using the format() method
       hourString.set("{0:2d}".format(totalHours))
       minuteString.set("{0:2d}".format(totalMinutes))
       secondString.set("{0:2d}".format(totalSeconds))

       # Updates the interface
       clockWindow.update()
       time.sleep(1)

       # When the timer hits zero this displays 10 images with 10 text
       if(clockTime == 0):
           number = random.randint(0, 9)
           if number == 0:
               test = label.config(image=pic)
               message_window.showinfo("", "Stand up and stretch your backside!")
           elif number == 1:
               label.config(image=pic2)
               message_window.showinfo("", "Place one foot in front of the other and bend your knee. Hold the stretch for 10 seconds then relax.")
           elif number == 2:
               label.config(image=pic3)
               message_window.showinfo("", "Drop your head slowly to the right and left!")
           elif number == 3:
               label.config(image=pic4)
               message_window.showinfo("", "Extend your arm, then pull your wrist down and up with your other hand!")
           elif number == 4:
               label.config(image=pic5,)
               message_window.showinfo("", "Raise your arm and bend it at the elbow. Pull the arm towards the opposite side!")
           elif number == 5:
               label.config(image=pic6)
               message_window.showinfo("", "Extend both arms in front of you palms facing downward. Bend all fingers at the knuckles!")
           elif number == 6:
               label.config(image=pic7)
               message_window.showinfo("", "Slowly turn your head to the right and look over your shoulder. Repeat on the other side!")
           elif number == 7:
               label.config(image=pic8)
               message_window.showinfo("", "Lift one leg and cross it over the other knee. Look over your shoulder while pressing the bottom leg!")
           elif number == 8:
               label.config(image=pic9)
               message_window.showinfo("", "Stand up and reach towards the ceiling until you feel a light stretch in your sides!")
           elif number == 9:
               label.config(image=pic10)
               message_window.showinfo("", "Slowly roll your shoulders backwards and forwards in a circular motion!")

# Decreases the value of every second by one
       clockTime -= 1

# Button to run the timer
setTimeButton = Button(clockWindow, text='Set Time', bd='5', command=runTimer)
setTimeButton.place(relx=0.5, rely=0.8, anchor=CENTER)

# Variables for the pictures in the previous if statement
picframe = Frame(clockWindow, bg="red").pack()
pic = PhotoImage(file=r"D:\Downloads\Stretches\back_side stretch.PNG", height=200, width=300)
pic2 = PhotoImage(file=r"D:\Downloads\Stretches\calf_stretch.PNG", height=200, width=300)
pic3 = PhotoImage(file=r"D:\Downloads\Stretches\neck_exercise flex.PNG", height=200, width=300)
pic4 = PhotoImage(file=r"D:\Downloads\Stretches\wrist_flex exercise.PNG", height=200, width=300)
pic5 = PhotoImage(file=r"D:\Downloads\Stretches\overhead_shoulder stretch.PNG", height=200, width=300)
pic6 = PhotoImage(file=r"D:\Downloads\Stretches\extending_finger stretch.PNG", height=200, width=300)
pic7 = PhotoImage(file=r"D:\Downloads\Stretches\head_turns exercise.PNG", height=200, width=300)
pic8 = PhotoImage(file=r"D:\Downloads\Stretches\hip stretches.PNG", height=200, width=300)
pic9 = PhotoImage(file=r"D:\Downloads\Stretches\lower_back stretch.PNG", height=200, width=300)
pic10 = PhotoImage(file=r"D:\Downloads\Stretches\shoulder_roll exercise.PNG",height=200, width=300)

# Defines Label for the background
label = Label(picframe, background="steel blue")
label.pack()

# Keeps looping
clockWindow.mainloop()

