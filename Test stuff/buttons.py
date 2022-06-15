import tkinter as tk

window = tk.Tk()
counter = 1
button_count = 0
total = 0
calc_mode = "+"


def button_identifier(event):
    widget_data = event.widget
    widget_data = str(widget_data).strip(".!frame")
    widget_data = widget_data.strip(".!button")
    if not widget_data:
        widget_data = 1
    print(f'You pressed button {widget_data}')
    button_counter(widget_data)


def button_counter(number):
    global button_count
    global total
    button_count += 1
    label["text"] = f'Buttons pressed:\n{button_count}'

    if calc_mode == "+":
        total += int(number)
    if calc_mode == "-":
        total -= int(number)
    if calc_mode == "/":
        total /= int(number)
    if calc_mode == "*":
        total *= int(number)
    label2["text"] = f'Total number:\n{total}'


def calcMode(event):
    global calc_mode
    widget_data = event.widget
    widget_data = str(widget_data).strip(".!frame")
    widget_data = widget_data.strip(".!button")
    print(widget_data)
    if int(widget_data) == 10:
        calc_mode = "+"
    if int(widget_data) == 11:
        calc_mode = "-"
    if int(widget_data) == 12:
        calc_mode = "/"
    if int(widget_data) == 13:
        calc_mode = "*"


for x in range(3):
    window.columnconfigure(x, weight=1, minsize=75)
    window.rowconfigure(x, weight=1, minsize=50)

    for z in range(3):
        frame = tk.Frame(master=window, width=75, height=100)
        frame.grid(row=x, column=z, padx=10, pady=10)
        button = tk.Button(master=frame, text=counter, relief=tk.RAISED, borderwidth=5, width=10, height=5,
                           bg="purple")

        button.bind("<Button-1>", button_identifier)

        button.pack(fill=tk.BOTH)
        counter += 1

plus = tk.Frame(master=window, width=75, height=100)
plus.grid(row=0, column=3, padx=10, pady=10)
button = tk.Button(master=plus, text="+", relief=tk.RAISED, borderwidth=5, width=10, height=5,
                   bg="purple", )
button.bind("<Button-1>", calcMode)
button.pack()

minus = tk.Frame(master=window, width=75, height=100)
minus.grid(row=1, column=3, padx=10, pady=10)
button = tk.Button(master=minus, text="-", relief=tk.RAISED, borderwidth=5, width=10, height=5,
                   bg="purple", )
button.bind("<Button-1>", calcMode)
button.pack()

divide = tk.Frame(master=window, width=75, height=100)
divide.grid(row=2, column=3, padx=10, pady=10)
button = tk.Button(master=divide, text="/", relief=tk.RAISED, borderwidth=5, width=10, height=5,
                   bg="purple", )
button.bind("<Button-1>", calcMode)
button.pack()

multiply = tk.Frame(master=window, width=75, height=100)
multiply.grid(row=3, column=3, padx=10, pady=10)
button = tk.Button(master=multiply, text="*", relief=tk.RAISED, borderwidth=5, width=10, height=5,
                   bg="purple", )
button.bind("<Button-1>", calcMode)
button.pack()

frame = tk.Frame(master=window, width=75, height=100)
frame.grid(row=3, column=1)

label = tk.Label(text=f'Buttons pressed:\n{button_count}', fg="green", master=frame)
label.pack()

frame = tk.Frame(master=window, width=75, height=100)
frame.grid(row=3, column=2)
label2 = tk.Label(text=f'Total number:\n{total}', fg="green", master=frame, )
label2.pack()

window.mainloop()
