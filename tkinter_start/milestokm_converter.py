from tkinter import *

def convert():
    x= int(input.get())
    converted_value = x*1.60934
    print(converted_value)
    label3.config(text=converted_value)



window = Tk()
window.title("Miles to km converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


label1 = Label(text="Enter miles")
label1.grid(column=0, row=0)
label1.config(padx=5, pady=5)
label2 = Label(text="Kilometers")
label2.grid(column=0, row=4)


input = Entry(width=10)
input.grid(column=2, row=0)
label3 = Label(text="0")
label3.grid(column=2, row=4)

button = Button(text="Convert", command=convert)
button.grid(column=2, row=5)



























window.mainloop()