import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

# Entry box
entry = tk.Entry(root, width=20, font="lucida 20 bold", borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons (digits and operators)
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row_val = 1
col_val = 0

for btn_text in buttons:
    b = tk.Button(root, text=btn_text, font="lucida 15 bold", height=2, width=5)

    # Define what each button does (without external function)
    if btn_text == "=":
        b.config(command=lambda e=entry: e.insert(tk.END, f" = {eval(e.get())}"))
    elif btn_text == "C":
        b.config(command=lambda e=entry: e.delete(0, tk.END))
    else:
        b.config(command=lambda val=btn_text, e=entry: e.insert(tk.END, val))

    b.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
