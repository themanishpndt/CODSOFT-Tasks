import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks and update the display
def on_button_click(value):
    current_text = display.get()
    if value == "C":
        display.set("")
    elif value == "=":
        try:
            result = str(eval(current_text))
            display.set(result)
        except Exception:
            display.set("Error")
    else:
        display.set(current_text + value)

# Function to handle key presses and simulate button press-down effect
def on_key_press(event):
    key_map = {
        '7': button_7, '8': button_8, '9': button_9, '/': button_div,
        '4': button_4, '5': button_5, '6': button_6, '*': button_mul,
        '1': button_1, '2': button_2, '3': button_3, '-': button_sub,
        'C': button_clear, '0': button_0, '=': button_eq, '+': button_add
    }
    
    valid_keys = "0123456789+-*/C="
    if event.char in valid_keys:
        # Trigger the button press visual effect
        button = key_map.get(event.char)
        if button:
            button.config(relief="sunken")  # Temporarily show the button pressed down
            window.after(100, lambda b=button: b.config(relief="raised"))  # Restore after 100ms
        on_button_click(event.char)
    elif event.keysym == "Return":
        button_eq.config(relief="sunken")
        window.after(100, lambda b=button_eq: b.config(relief="raised"))
        on_button_click("=")
    elif event.keysym == "BackSpace":
        current_text = display.get()
        display.set(current_text[:-1])  # Remove last character on Backspace

# Create the main window
window = tk.Tk()
window.title("Rectangle Calculator")
window.geometry("400x500")  # Rectangular window size
window.configure(bg="#f7f7f7")  # Light background for the window

# Create a display widget to show numbers and results
display = tk.StringVar()
display_label = tk.Label(window, textvariable=display, font=("Arial", 24), bg="#ffffff", fg="#333333", anchor="e", bd=10, relief="sunken")
display_label.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=20, sticky="we")

# Define buttons for the calculator with updated light colors
buttons = [
    ('7', "#aed581"), ('8', "#aed581"), ('9', "#aed581"), ('/', "#ffb74d"),
    ('4', "#aed581"), ('5', "#aed581"), ('6', "#aed581"), ('*', "#ffb74d"),
    ('1', "#aed581"), ('2', "#aed581"), ('3', "#aed581"), ('-', "#ffb74d"),
    ('C', "#ef9a9a"), ('0', "#aed581"), ('=', "#64b5f6"), ('+', "#ffb74d")
]

# Create button widgets and map them to variables
button_7 = tk.Button(window, text="7", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('7'))
button_8 = tk.Button(window, text="8", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('8'))
button_9 = tk.Button(window, text="9", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('9'))
button_div = tk.Button(window, text="/", bg="#ffb74d", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('/'))

button_4 = tk.Button(window, text="4", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('4'))
button_5 = tk.Button(window, text="5", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('5'))
button_6 = tk.Button(window, text="6", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('6'))
button_mul = tk.Button(window, text="*", bg="#ffb74d", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('*'))

button_1 = tk.Button(window, text="1", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('1'))
button_2 = tk.Button(window, text="2", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('2'))
button_3 = tk.Button(window, text="3", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('3'))
button_sub = tk.Button(window, text="-", bg="#ffb74d", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('-'))

button_clear = tk.Button(window, text="C", bg="#ef9a9a", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('C'))
button_0 = tk.Button(window, text="0", bg="#aed581", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('0'))
button_eq = tk.Button(window, text="=", bg="#64b5f6", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('='))
button_add = tk.Button(window, text="+", bg="#ffb74d", fg="white", font=("Arial", 18), bd=5, relief="raised", width=10, height=4, command=lambda: on_button_click('+'))

# Place buttons on the grid
buttons_grid = [
    [button_7, button_8, button_9, button_div],
    [button_4, button_5, button_6, button_mul],
    [button_1, button_2, button_3, button_sub],
    [button_clear, button_0, button_eq, button_add]
]

for row_idx, row in enumerate(buttons_grid, start=1):
    for col_idx, button in enumerate(row):
        button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)

# Make columns and rows resizable
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i, weight=1)

# Bind keyboard events to the window
window.bind("<Key>", on_key_press)

# Start the main loop
window.mainloop()
