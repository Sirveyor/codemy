from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap()

#Create radio function

def radio():
	if v.get() == "one":
		my_label = Label(root, text="You Clicked Radio Button One!")
	else:
		my_label = Label(root, text="You Clicked Radio Button Two!")

	my_label.pack(pady=10)

# Radio Buttons
v = StringVar()
v.set("two") # on widows this will set the default radio button

rbutton_1 = Radiobutton(root, text="One", variable=v, value="one")
rbutton_2 = Radiobutton(root, text="Two", variable=v, value="tow",)
rbutton_1.pack(pady=10)
rbutton_2.pack(padx=10)
rbutton_2.select() #used on mac to set the default radio button

my_button = Button(root, text="Click me", command=radio)
my_button.pack(pady=20)

root.mainloop()