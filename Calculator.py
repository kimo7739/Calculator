import tkinter

buttonvalues = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

rightsymbols = ["÷", "x", "-", "+", "="]
topsymbols = ["AC", "+/-", "%"]

colorlightgray = "#D4D4D2"
colorblack = "#1C1C1C"
colordarkgray = "#505050"
colororange = "#FF9500"
colorwhite = "white"

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)
    
def button_clicked(value):
    global rightsymbols, topsymbols, label, A, B, operator

    if value in rightsymbols:
        if value == "=":
            if A is not None and operator is not None :
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()

        elif value in "+-x÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in topsymbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
        elif operator == "√":
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zero_decimal(result)      
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
 

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=colorblack,
    foreground=colorwhite,
    anchor="e",
)

label.grid(row=0, column=0, columnspan=4, sticky="we")

row_count = len(buttonvalues)
column_count = len(buttonvalues[0])

for row in range(row_count):
    for column in range(column_count):
        value = buttonvalues[row][column]

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=4,
            height=2,
            command=lambda value=value: button_clicked(value)
        )
        if value in topsymbols:
            button.config(foreground=colorblack, background=colorlightgray)

        elif value in rightsymbols:
             button.config(foreground=colorwhite, background=colororange)

        else:
         button.config(foreground=colorwhite, background=colordarkgray)
        button.grid(row=row+1, column=column, sticky="nsew")

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

for i in range(6):
    frame.grid_rowconfigure(i, weight=1)

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()