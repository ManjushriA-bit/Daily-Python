import tkinter as tk

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, round(result, 2))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


root = tk.Tk()
root.title("Light Minimal Calculator")
root.geometry("350x500")
root.configure(bg="#f5f7fa")

entry = tk.Entry(root,
                 font=("Arial",24),
                 bd=5,
                 justify="right",
                 bg="white",
                 fg="black")
entry.pack(fill=tk.BOTH, pady=15)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","%","+",
    "**","C","="
]

frame = tk.Frame(root, bg="#f5f7fa")
frame.pack()

row = col = 0

for button in buttons:

    if button == "=":
        color = "#22c55e"
    elif button == "C":
        color = "#ef4444"
    elif button in ["+","-","*","/","%","**"]:
        color = "#38bdf8"
    else:
        color = "#e2e8f0"

    btn = tk.Button(frame, text=button,
                    font=("Arial",16),
                    width=5, height=2,
                    bg=color, fg="black",
                    bd=0,
                    activebackground="#cbd5e1")

    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
