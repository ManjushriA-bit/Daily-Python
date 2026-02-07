import tkinter as tk

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, round(result, 2))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Cannot divide by 0")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, button_text)


# Main window
root = tk.Tk()
root.title("Advanced Python Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry box
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=15)

# Buttons layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "%", "+",
    "**", "C", "="
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    btn = tk.Button(frame,
                    text=button,
                    font=("Arial", 16),
                    width=5,
                    height=2)

    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
