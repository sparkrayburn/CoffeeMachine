from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("My first gui program ")
window.minsize(width=500, height= 600)
window.config(padx=100, pady=200)


my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)





button = Button(text="click me ", command=button_clicked)
button.grid(column=2, row=2)

button2 = Button(text = "click ne instead", command=button_clicked)
button2.grid(column=3, row=1)


input = Entry()
input.grid(column=4, row=4)



























window.mainloop()