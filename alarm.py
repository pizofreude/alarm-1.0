# Import necessaries libraries
# to build alarm clock.
from tkinter import *
import tkinter as tk
import datetime
import time as tm
import winsound

# Create while loop with a Boolean function True 
# which makes the program automatic to work.
def alarm(set_alarm_timer):
    while True:
        tm.sleep(1)
        current_time = datetime.datetime.now()  # Get current time as a whole.
        now = current_time.strftime("%H:%M:%S")  # Convert current_time to H:M:S.
        date = current_time.strftime("%d/%m/%Y")  # Convert current_time to d:m:Y.
        print("The Set Date is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Hiya! Waky, waky!")
            for i in range(7):
                winsound.Beep(500,900)
            break
        if now >= set_alarm_timer:
            break
    return
            
def actual_time():
    # f-string format with {} for expression to evaluate.
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def digital_clock_date():
    current_time = tm.strftime('%H:%M:%S')
    current_date = tm.strftime('%d/%m/%Y')
    show_time['text'] = current_time
    show_date['text'] = current_date
    show_time.after(200,digital_clock_date)  # show_time.after is a SystemEvent after 200ms.
    show_date.after(500000,digital_clock_date)  # show_date.after is a SystemEvent after 500000ms.

# Function to reset alarm input.
def reset():
    hour.set("")
    min.set("")
    sec.set("")

# Function to exit window.
def exit():
    clock.destroy()

# Creating GUI using tkinter.
clock = Tk()
clock.iconbitmap(r"Vexels-Office-Alarm-clock.ico")
clock.title("My First Alarm Clock")
clock.geometry("600x270")
clock.resizable(0,0)
time_format = Label(clock, text="24 hour time format", fg="cyan", bg="grey", font="Arialblack").place(x=200, y=240)
add_time = Label(clock, text="Hour   Min   Sec", font=("Arial",18)).place(x=145,y=20)
set_the_alarm = Label(clock, text="Set the Alarm: ", fg='cyan', bg="grey", relief="solid", font=("Arial", 10, "bold")).place(x=20, y=63.5)
set_copyright = Label(clock, text='by Pizofreude™', font = 'arial 8 bold').pack()
# Show current time and date.
current_time = tm.strftime('%H:%M:%S')
current_date = tm.strftime('%d/%m/%Y')
show_time = tk.Label(clock, font='arial 12', fg='black', text=current_time)
show_date = tk.Label(clock, font='arial 12', fg='black', text=current_date)
show_time.place(x=165*2.75,y=118)
show_date.place(x=165*2.692,y=118+25)

# Variables to initialize the actual_time().
hour = StringVar()
min = StringVar()
sec = StringVar()

# Input time from user via alarm GUI.
hour_time = Entry(clock, textvariable = hour, font=("ArialBlack",18,"bold"), bg = "lightgrey", width=20,).place(x=150, y=60)
min_time = Entry(clock, textvariable = min, font=("ArialBlack",18,"bold"), bg = "lightgrey", width=20,).place(x=210, y=60)
sec_time = Entry(clock, textvariable = sec, font=("ArialBlack",18,"bold"), bg = "lightgrey", width=20,).place(x=270, y=60)

# Alarm button confirmation for user.
submit_button = Button(clock, text="Set Alarm", font=("ArialBlack",18), fg="black", bg="lightgrey", width=15, command=actual_time).place(x=165, y=120)
exit_button = Button(clock, text="Exit", font=("ArialBlack",14), fg="black", bg="orangered", width=13, command=exit).place(x=195, y=180)
reset_button = Button(clock, text="Reset", font=("ArialBlack",14), fg="black", bg="lightgreen", width=13, command=reset).place(x=195*2, y=180)
# output_message = Entry(clock, font = 'arial 10 bold', textvariable = alarm_output, bg ='ghost white', width=23, ).place(x=10, y=180 )

# Execution window.
digital_clock_date()
clock.mainloop()