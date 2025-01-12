from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Hello, World!")
root.geometry("400x400")
root.iconbitmap("")

# Create Click Function
def clicked():
	global my_label2
	my_label2 = Label(root, text=f"You entered {e.get()}")
	my_label2.pack()

# Hide function
def hide():
	my_label2.pack_forget()
	#my_label2.destroy

# Show function
def show():
	my_label2.pack()
	
# Add Images
'''
my_image = Image.open("good.jpg")
my_image = ImageTk.PhotoImage(my_image)

image_label = Label(root, image=my_image, height=40, width=400)
image_label.pack()
'''


# Create labels
my_label = Label(root, text='Enter Your Name: ',font=("helvetica", 22))
my_label.pack()

# Create Entry Widget Input Box
e = Entry(root, width=300, font=("helvetica", 22))
e.pack(pady=20)

# Create Buttons
my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="Show", command=show)
show_button.pack(pady=20)







root.mainloop()

