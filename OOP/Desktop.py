import tkinter as tk
from tkinter import messagebox
root= tk.Tk()

root.title("Tkinter Demo App ")
root.geometry("350x200")

def show_message():
    messagebox.showinfo("Hello", "Welcome to your first Tkinter App!! ")
label= tk.Label(root,text= "My First App!! ", font=("Cosmic Scans",20))
label.pack(pady=40)

button=tk.Button(root,text="Click Me! ", command= show_message)
button.pack()
root.mainloop()
