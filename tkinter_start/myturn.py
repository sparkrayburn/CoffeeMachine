from tkinter import *


window = Tk()
window.title("Widget sample")
window.minsize(width=500, height=600)

label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()



def buttons():
    print("DO something")


button = Button(text="click me", command=buttons)
button.pack()


entry = Entry()
entry.insert(END, string="some text to begin with")
entry.pack()




text = Text(height=5, width=30)
text.focus()
text.insert(END, "You can write anything here ")
print(text.get(1.0, END))
text.pack()



def spinbox():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


def check_button_used():
    print(checked_state.get())
checked_state = IntVar()
check_button = Checkbutton(text= "Is on?", variable=checked_state, command=check_button_used)
checked_state.get()
check_button.pack()

def radio_button_used():
    print(radio_state.get())

radio_state = IntVar()
radio_button1 = Radiobutton(text= "option", variable=radio_state, command=radio_button_used)
radio_button2 = Radiobutton(text= "option2", variable=radio_state, command=radio_button_used)
radio_button1.pack()
radio_button2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Mango", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


































window.mainloop()