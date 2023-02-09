import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        
        # Cria os widgets
        self.label = tk.Label(master, text="Insira sua expressão matemática abaixo")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        self.entry = tk.Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=1, column=0, columnspan=10, padx=10, pady=10)
        
        self.button_1 = tk.Button(master, text="1", padx=30, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(master, text="2", padx=30, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(master, text="3", padx=30, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(master, text="4", padx=30, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(master, text="5", padx=30, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(master, text="6", padx=30, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(master, text="7", padx=30, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(master, text="8", padx=30, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(master, text="9", padx=30, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(master, text="0", padx=30, pady=20, command=lambda: self.button_click(0))
        self.button_add = tk.Button(master, text="+", padx=30, pady=20, command=lambda: self.button_click("+"))
        self.button_equal = tk.Button(master, text="=", padx=91, pady=20, command=self.button_equal)
        self.button_clear = tk.Button(master, text="⌫", padx=90, pady=20, command=self.button_clear)
        
        # Coloca os widgets na tela
        self.button_1.grid(row=2, column=0)
        self.button_2.grid(row=2, column=1)
        self.button_3.grid(row=2, column=2)
        
        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)
        
        self.button_7.grid(row=4, column=0)
        self.button_8.grid(row=4, column=1)
        self.button_9.grid(row=4, column=2)
        
        self.button_0.grid(row=5, column=0)
        self.button_clear.grid(row=5, column=1, columnspan=2)
        self.button_add.grid(row=6, column=0)
        self.button_equal.grid(row=6, column=1, columnspan=2)
        
    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(number))
    
    def button_clear(self):
        self.entry.delete(0, tk.END)
        
    def button_equal(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        
        try:
            self.entry.insert(0, eval(current))
        except:
            self.entry.insert(0, "Error")
            
root = tk.Tk()
calc = Calculator(root)
root.mainloop()