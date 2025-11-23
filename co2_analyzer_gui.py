import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from co2_analyzer import CO2Analyzer

class CO2AnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CO2 Emission Analyzer")
        self.root.geometry("1000x650")
        
        self.analyzer = CO2Analyzer()
        self.setup_ui()
        
    def setup_ui(self):
        # header
        header = tk.Frame(self.root, bg='#34495e', height=70)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text="CO2 Emission Analyzer", 
                font=('Helvetica', 22, 'bold'), 
                bg='#34495e', fg='white').pack(pady=20)
        
        # main area
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=15, pady=15)
        
        # input section (left)
        input_frame = tk.Frame(container, bg='#ecf0f1', relief='groove', bd=3)
        input_frame.pack(side='left', fill='both', expand=True, padx=(0, 8))
        
        # results section (right)
        results_frame = tk.Frame(container, bg='#ecf0f1', relief='groove', bd=3)
        results_frame.pack(side='right', fill='both', expand=True, padx=(8, 0))
        
        self.build_input_area(input_frame)
        self.build_results_area(results_frame)
        
    def build_input_area(self, parent):
        tk.Label(parent, text="Add Emissions", font=('Helvetica', 14, 'bold'),
                bg='#ecf0f1').pack(pady=12)
        
        tabs = ttk.Notebook(parent)
        tabs.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # transportation
        t_frame = tk.Frame(tabs, bg='white')
        tabs.add(t_frame, text='Transportation')
        
        tk.Label(t_frame, text="Mode:", bg='white', 
                font=('Helvetica', 10)).grid(row=0, column=0, sticky='w', padx=25, pady=(25, 8))
        self.trans_mode = ttk.Combobox(t_frame, 
                                       values=['car', 'bus', 'train', 'plane'], 
                                       state='readonly', width=28)
        self.trans_mode.grid(row=0, column=1, padx=25, pady=(25, 8))
        self.trans_mode.current(0)
        
        tk.Label(t_frame, text="Distance (km):", bg='white', 
                font=('Helvetica', 10)).grid(row=1, column=0, sticky='w', padx=25, pady=8)
        self.trans_dist = tk.Entry(t_frame, width=30, font=('Helvetica', 10))
        self.trans_dist.grid(row=1, column=1, padx=25, pady=8)
        
        tk.Button(t_frame, text="Add Entry", command=self.add_transport,
                 bg='#3498db', fg='white', font=('Helvetica', 10, 'bold'),
                 padx=25, pady=8, cursor='hand2').grid(row=2, column=0, columnspan=2, pady=20)
        
        info = tk.Text(t_frame, height=6, width=45, bg='#f8f9fa', 
                      font=('Courier', 8), relief='flat', wrap='word')
        info.grid(row=3, column=0, columnspan=2, padx=25, pady=(10, 20))
        info.insert('1.0', "Emission factors:\n"
                          "  Car:   0.192 kg CO2/km\n"
                          "  Bus:   0.089 kg CO2/km\n"
                          "  Train: 0.041 kg CO2/km\n"
                          "  Plane: 0.255 kg CO2/km")
        info.config(state='disabled')
        
        # energy
        e_frame = tk.Frame(tabs, bg='white')
        tabs.add(e_frame, text='Energy')
        
        tk.Label(e_frame, text="Type:", bg='white', 
                font=('Helvetica', 10)).grid(row=0, column=0, sticky='w', padx=25, pady=(25, 8))
        self.energy_type = ttk.Combobox(e_frame, 
                                       values=['electricity', 'natural_gas'], 
                                       state='readonly', width=28)
        self.energy_type.grid(row=0, column=1, padx=25, pady=(25, 8))
        self.energy_type.current(0)
        
        tk.Label(e_frame, text="Amount (kWh):", bg='white', 
                font=('Helvetica', 10)).grid(row=1, column=0, sticky='w', padx=25, pady=8)
        self.energy_amt = tk.Entry(e_frame, width=30, font=('Helvetica', 10))
        self.energy_amt.grid(row=1, column=1, padx=25, pady=8)
        
        tk.Button(e_frame, text="Add Entry", command=self.add_energy,
                 bg='#e74c3c', fg='white', font=('Helvetica', 10, 'bold'),
                 padx=25, pady=8, cursor='hand2').grid(row=2, column=0, columnspan=2, pady=20)
        
        info2 = tk.Text(e_frame, height=5, width=45, bg='#f8f9fa', 
                       font=('Courier', 8), relief='flat', wrap='word')
        info2.grid(row=3, column=0, columnspan=2, padx=25, pady=(10, 20))
        info2.insert('1.0', "Emission factors:\n"
                           "  Electricity:  0.475 kg CO2/kWh\n"
                           "  Natural Gas:  0.185 kg CO2/kWh")
        info2.config(state='disabled')
        
        # food
        f_frame = tk.Frame(tabs, bg='white')
        tabs.add(f_frame, text='Food')
        
        tk.Label(f_frame, text="Type:", bg='white', 
                font=('Helvetica', 10)).grid(row=0, column=0, sticky='w', padx=25, pady=(25, 8))
        self.food_type = ttk.Combobox(f_frame, 
                                     values=['meat', 'vegetarian'], 
                                     state='readonly', width=28)
        self.food_type.grid(row=0, column=1, padx=25, pady=(25, 8))
        self.food_type.current(0)
        
        tk.Label(f_frame, text="Quantity:", bg='white', 
                font=('Helvetica', 10)).grid(row=1, column=0, sticky='w', padx=25, pady=8)
        self.food_qty = tk.Entry(f_frame, width=30, font=('Helvetica', 10))
        self.food_qty.grid(row=1, column=1, padx=25, pady=8)
        
        tk.Label(f_frame, text="(kg for meat, meals for veg)", 
                bg='white', font=('Helvetica', 8), fg='gray').grid(row=2, column=0, 
                                                                    columnspan=2, pady=(0, 8))
        
        tk.Button(f_frame, text="Add Entry", command=self.add_food,
                 bg='#27ae60', fg='white', font=('Helvetica', 10, 'bold'),
                 padx=25, pady=8, cursor='hand2').grid(row=3, column=0, columnspan=2, pady=20)
        
        info3 = tk.Text(f_frame, height=5, width=45, bg='#f8f9fa', 
                       font=('Courier', 8), relief='flat', wrap='word')
        info3.grid(row=4, column=0, columnspan=2, padx=25, pady=(10, 20))
        info3.insert('1.0', "Emission factors:\n"
                           "  Meat (beef):      27.0 kg CO2/kg\n"
                           "  Vegetarian meal:   1.5 kg CO2/meal")
        info3.config(state='disabled')
        
    def build_results_area(self, parent):
        tk.Label(parent, text="Results", font=('Helvetica', 14, 'bold'),
                bg='#ecf0f1').pack(pady=12)
        
        # total display
        total_box = tk.Frame(parent, bg='#2ecc71', relief='raised', bd=3, height=90)
        total_box.pack(fill='x', padx=15, pady=10)
        total_box.pack_propagate(False)
        
        tk.Label(total_box, text="Total Emissions", 
                font=('Helvetica', 11, 'bold'), 
                bg='#2ecc71', fg='white').pack(pady=(12, 3))
        
        self.total_display = tk.Label(total_box, text="0.00 kg CO2", 
                                      font=('Helvetica', 20, 'bold'), 
                                      bg='#2ecc71', fg='white')
        self.total_display.pack()
        
        # entries list
        tk.Label(parent, text="All Entries:", bg='#ecf0f1', 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', padx=15, pady=(12, 5))
        
        list_container = tk.Frame(parent)
        list_container.pack(fill='both', expand=True, padx=15, pady=5)
        
        scroll = tk.Scrollbar(list_container)
        scroll.pack(side='right', fill='y')
        
        self.entries_list = tk.Listbox(list_container, 
                                       yscrollcommand=scroll.set,
                                       font=('Courier', 9), 
                                       bg='white',
                                       selectmode='single')
        self.entries_list.pack(side='left', fill='both', expand=True)
        scroll.config(command=self.entries_list.yview)
        
        # buttons
        btn_frame = tk.Frame(parent, bg='#ecf0f1')
        btn_frame.pack(fill='x', padx=15, pady=15)
        
        tk.Button(btn_frame, text="Show Charts", command=self.show_viz,
                 bg='#9b59b6', fg='white', font=('Helvetica', 9, 'bold'),
                 cursor='hand2', padx=10, pady=6).pack(side='left', padx=3, fill='x', expand=True)
        
        tk.Button(btn_frame, text="Save CSV", command=self.save_csv,
                 bg='#16a085', fg='white', font=('Helvetica', 9, 'bold'),
                 cursor='hand2', padx=10, pady=6).pack(side='left', padx=3, fill='x', expand=True)
        
        tk.Button(btn_frame, text="Clear", command=self.clear_data,
                 bg='#e67e22', fg='white', font=('Helvetica', 9, 'bold'),
                 cursor='hand2', padx=10, pady=6).pack(side='left', padx=3, fill='x', expand=True)
        
    def add_transport(self):
        try:
            mode = self.trans_mode.get()
            dist = float(self.trans_dist.get())
            
            if dist <= 0:
                messagebox.showerror("Invalid Input", "Distance must be positive")
                return
            
            self.analyzer.add_transportation(mode, dist)
            self.refresh_display()
            self.trans_dist.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def add_energy(self):
        try:
            etype = self.energy_type.get()
            amt = float(self.energy_amt.get())
            
            if amt <= 0:
                messagebox.showerror("Invalid Input", "Amount must be positive")
                return
            
            self.analyzer.add_energy(etype, amt)
            self.refresh_display()
            self.energy_amt.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def add_food(self):
        try:
            ftype = self.food_type.get()
            qty = float(self.food_qty.get())
            
            if qty <= 0:
                messagebox.showerror("Invalid Input", "Quantity must be positive")
                return
            
            self.analyzer.add_food(ftype, qty)
            self.refresh_display()
            self.food_qty.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def refresh_display(self):
        total = self.analyzer.get_total_emissions()
        self.total_display.config(text=f"{total:.2f} kg CO2")
        
        self.entries_list.delete(0, tk.END)
        for item in self.analyzer.emissions:
            line = f"{item['category']:<13} {item['type']:<13} {item['amount']:>7.1f} {item['unit']:<5} = {item['co2_kg']:>8.2f} kg"
            self.entries_list.insert(tk.END, line)
    
    def show_viz(self):
        if not self.analyzer.emissions:
            messagebox.showwarning("No Data", "Add some emissions first")
            return
        self.analyzer.visualize()
    
    def save_csv(self):
        if not self.analyzer.emissions:
            messagebox.showwarning("No Data", "Nothing to save")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filepath:
            self.analyzer.save_report(filepath)
            messagebox.showinfo("Saved", f"Report saved successfully")
    
    def clear_data(self):
        if messagebox.askyesno("Confirm", "Clear all data?"):
            self.analyzer = CO2Analyzer()
            self.refresh_display()


if __name__ == "__main__":
    root = tk.Tk()
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    app = CO2AnalyzerGUI(root)
    root.mainloop()
