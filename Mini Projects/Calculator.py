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
root.title("Blue Professional Calculator")
root.geometry("350x500")
root.configure(bg="#0f172a")

entry = tk.Entry(root,
                 font=("Arial",24),
                 bd=10,
                 justify="right",
                 bg="#1e293b",
                 fg="white",
                 insertbackground="white")
entry.pack(fill=tk.BOTH, pady=15)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","%","+",
    "**","C","="
]

frame = tk.Frame(root, bg="#0f172a")
frame.pack()

row = col = 0

for button in buttons:

    if button == "=":
        color = "#2563eb"
    elif button == "C":
        color = "#dc2626"
    elif button in ["+","-","*","/","%","**"]:
        color = "#3b82f6"
    else:
        color = "#334155"

    btn = tk.Button(frame, text=button,
                    font=("Arial",16),
                    width=5, height=2,
                    bg=color, fg="white",
                    bd=0,
                    activebackground="#1d4ed8")

    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
