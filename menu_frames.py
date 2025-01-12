from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x800")
root.iconbitmap('')

# Define a menue
my_menu = Menu(root)
root.config(menu=my_menu)

def fake_command():
	pass

def new():
	hide_menu_frames()
	file_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

def cut():
	hide_menu_frames()
	edit_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

def hide_menu_frames():
	file_frame.grid_forget()
	edit_frame.grid_forget()

# Create Menu Items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create anouther submenu Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=fake_command)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=fake_command)

# Create Help Menu
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=fake_command)

'''
show_button = Button(root, text="Show", command=show)
hide_button = Button(root, text="Hide", command=hide)

show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)
'''

# File Menu Frame
file_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
#file_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

file_frame_label = Label(file_frame, text="File Frame", font=("Helvetica", 20))
file_frame_label.pack(pady=20,padx=20)

# Edit Menu Frame
edit_frame = Frame(root, width=200, height=200, bd=5, bg="blue", relief="sunken")
#file_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

edit_frame_label = Label(edit_frame, text="Cut Frame", font=("Helvetica", 20))
edit_frame_label.pack(pady=20,padx=20)


root.mainloop()

