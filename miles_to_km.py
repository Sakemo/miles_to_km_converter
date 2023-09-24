import tkinter as tk
from ttkbootstrap import Style

class MilhasParaKilometrosConverter:
    def __init__(self, root):
        self.root = root
        self.root.title('Conversor de Milhas para Quilômetros')
        self.root.geometry('300x150')
        
        self.style = Style(theme='darkly')
        
        self.create_widgets()

    def convert(self):
        mile_input = self.entry_int.get()
        km_output = mile_input * 1.61
        self.output_string.set(f'{mile_input} milhas são {km_output:.2f} quilômetros')

    def create_widgets(self):
        title_label = tk.Label(
            master=self.root,
            text='Milhas para Quilômetros',
            font='Bahnschrift 18',
        )
        title_label.pack()

        input_frame = tk.Frame(master=self.root)
        self.entry_int = tk.DoubleVar()
        entry = tk.Entry(
            master=input_frame,
            textvariable=self.entry_int,
        )
        button = tk.Button(
            master=input_frame,
            text='Converter',
            command=self.convert,
        )
        entry.pack(side='left', padx=10)
        button.pack(side='left')
        input_frame.pack(pady=10)

        self.output_string = tk.StringVar()
        output_label = tk.Label(
            master=self.root,
            text='Saída',
            font='Bahnschrift 18',
            textvariable=self.output_string,
        )
        output_label.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    converter_app = MilhasParaKilometrosConverter(root)
    root.mainloop()
