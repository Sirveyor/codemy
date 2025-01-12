from tkinter import *

root = Tk()
root.title("Hello, World!")
root.geometry("400x400")
root.iconbitmap()

# Create toppings function
def toppings():
	toppings_label = Label(root, text=v.get().capitalize())
	toppings_label.pack(pady=10)
#
v = StringVar()



my_check = Checkbutton(root, text="Pepperoni", variable=v,
	onvalue="pepperoni", offvalue="no_pepperoni")
my_check.deselect()
my_check.pack()

my_button = Button(root, text="Select Toppings", command=toppings)
my_button.pack(pady=10)



root.mainloop()