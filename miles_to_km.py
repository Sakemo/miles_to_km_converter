import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# Windows
windows = tk.Tk()
windows.title('Demo')
windows.geometry('300x150')

# Title
title_label = ttk.Label(master = windows, text = 'Milhas para Kilometros', font = 'Bahnschrift 18')
title_label.pack()

# Input Field
input_frame = ttk.Frame(master = windows)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Converter', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(
    master= windows, 
    text = 'Saída', 
    font = 'Bahnschrift 18', 
    textvariable = output_string)
output_label.pack(pady = 5)

# Run
windows.mainloop()