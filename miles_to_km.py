import tkinter as tk
from ttkbootstrap import Style, ttk

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Milhas para Km')
        self.root.geometry('300x150')
        
        self.style = Style(theme='darkly')
        
        self.create_widgets()

    def convert(self):
        mile_input = self.entry_int.get()
        km_output = mile_input * 1.61
        self.output_string.set(km_output)

    def create_widgets(self):
        title_label = ttk.Label(self.root, text='Milhas para Kilometros', font='Bahnschrift 18')
        title_label.pack()

        input_frame = ttk.Frame(self.root)
        self.entry_int = tk.IntVar()
        entry = ttk.Entry(input_frame, textvariable=self.entry_int)
        button = ttk.Button(input_frame, text='Converter', command=self.convert)
        entry.pack(side='left', padx=10)
        button.pack(side='left')
        input_frame.pack(pady=10)

        self.output_string = tk.StringVar()
        output_label = ttk.Label(self.root, text='Saída', font='Bahnschrift 18', textvariable=self.output_string)
        output_label.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
