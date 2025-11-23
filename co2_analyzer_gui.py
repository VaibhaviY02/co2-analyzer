import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from co2_analyzer import CO2Analyzer

class CO2AnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 CO2 Emission Analyzer")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Create analyzer instance
        self.analyzer = CO2Analyzer()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill='x', pady=(0, 10))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="🌍 CO2 Emission Analyzer", 
                              font=('Arial', 20, 'bold'), bg='#2c3e50', fg='white')
        title_label.pack(pady=15)
        
        # Main container
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left panel - Input forms
        left_panel = tk.Frame(main_container, bg='white', relief='raised', bd=2)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Right panel - Results
        right_panel = tk.Frame(main_container, bg='white', relief='raised', bd=2)
        right_panel.pack(side='right', fill='both', expand=True)
        
        # === LEFT PANEL CONTENT ===
        self.create_input_section(left_panel)
        
        # === RIGHT PANEL CONTENT ===
        self.create_results_section(right_panel)
        
    def create_input_section(self, parent):
        # Notebook for tabs
        notebook = ttk.Notebook(parent)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Transportation Tab
        transport_frame = tk.Frame(notebook, bg='white')
        notebook.add(transport_frame, text='🚗 Transportation')
        self.create_transportation_form(transport_frame)
        
        # Energy Tab
        energy_frame = tk.Frame(notebook, bg='white')
        notebook.add(energy_frame, text='⚡ Energy')
        self.create_energy_form(energy_frame)
        
        # Food Tab
        food_frame = tk.Frame(notebook, bg='white')
        notebook.add(food_frame, text='🍔 Food')
        self.create_food_form(food_frame)
        
    def create_transportation_form(self, parent):
        tk.Label(parent, text="Transportation Mode:", font=('Arial', 10, 'bold'),
                bg='white').pack(anchor='w', padx=20, pady=(20, 5))
        
        self.transport_mode = ttk.Combobox(parent, values=['car', 'bus', 'train', 'plane'],
                                          state='readonly', width=30)
        self.transport_mode.pack(padx=20, pady=5)
        self.transport_mode.set('car')
        
        tk.Label(parent, text="Distance (km):", font=('Arial', 10, 'bold'),
                bg='white').pack(anchor='w', padx=20, pady=(15, 5))
        
        self.transport_distance = tk.Entry(parent, width=32, font=('Arial', 10))
        self.transport_distance.pack(padx=20, pady=5)
        
        add_btn = tk.Button(parent, text="Add Transportation", 
                           command=self.add_transportation,
                           bg='#3498db', fg='white', font=('Arial', 10, 'bold'),
                           relief='flat', cursor='hand2', padx=20, pady=10)
        add_btn.pack(pady=20)
        
        # Info label
        info_text = """
        Emission Factors:
        • Car: 0.192 kg CO2/km
        • Bus: 0.089 kg CO2/km
        • Train: 0.041 kg CO2/km
        • Plane: 0.255 kg CO2/km
        """
        tk.Label(parent, text=info_text, font=('Arial', 8), 
                bg='#ecf0f1', fg='#7f8c8d', justify='left',
                relief='sunken', padx=10, pady=10).pack(fill='x', padx=20, pady=10)
        
    def create_energy_form(self, parent):
        tk.Label(parent, text="Energy Type:", font=('Arial', 10, 'bold'),
                bg='white').pack(anchor='w', padx=20, pady=(20, 5))
        
        self.energy_type = ttk.Combobox(parent, values=['electricity', 'natural_gas'],
                                       state='readonly', width=30)
        self.energy_type.pack(padx=20, pady=5)
        self.energy_type.set('electricity')
        
        tk.Label(parent, text="Amount (kWh):", font=('Arial', 10, 'bold'),
                bg='white').pack(anchor='w', padx=20, pady=(15, 5))
        
        self.energy_amount = tk.Entry(parent, width=32, font=('Arial', 10))
        self.energy_amount.pack(padx=20, pady=5)
        
        add_btn = tk.Button(parent, text="Add Energy Usage", 
                           command=self.add_energy,
                           bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'),
                           relief='flat', cursor='hand2', padx=20, pady=10)
        add_btn.pack(pady=20)
        
        # Info label
        info_text = """
        Emission Factors:
        • Electricity: 0.475 kg CO2/kWh
        • Natural Gas: 0.185 kg CO2/kWh
        """
        tk.Label(parent, text=info_text, font=('Arial', 8), 
                bg='#ecf0f1', fg='#7f8c8d', justify='left',
                relief='sunken', padx=10, pady=10).pack(fill='x', padx=20, pady=10)
        
    def create_food_form(self, parent):
        tk.Label(parent, text="Meal Type:", font=('Arial', 10, 'bold'),
                bg='white').pack(anchor='w', padx=20, pady=(20, 5))
        
        self.food_type = ttk.Combobox(parent, values=['meat', 'vegetarian'],
                                     state='readonly', width=30)
        self.food_type.pack(padx=20, pady=5)
        self.food_type.set('meat')
        
        tk.Label(parent, text="Quantity (kg for meat, meals for veg):", 
                font=('Arial', 10, 'bold'), bg='white').pack(anchor='w', padx=20, pady=(15, 5))
        
        self.food_quantity = tk.Entry(parent, width=32, font=('Arial', 10))
        self.food_quantity.pack(padx=20, pady=5)
        
        add_btn = tk.Button(parent, text="Add Food Emission", 
                           command=self.add_food,
                           bg='#2ecc71', fg='white', font=('Arial', 10, 'bold'),
                           relief='flat', cursor='hand2', padx=20, pady=10)
        add_btn.pack(pady=20)
        
        # Info label
        info_text = """
        Emission Factors:
        • Meat (beef): 27.0 kg CO2/kg
        • Vegetarian meal: 1.5 kg CO2/meal
        """
        tk.Label(parent, text=info_text, font=('Arial', 8), 
                bg='#ecf0f1', fg='#7f8c8d', justify='left',
                relief='sunken', padx=10, pady=10).pack(fill='x', padx=20, pady=10)
        
    def create_results_section(self, parent):
        # Title
        tk.Label(parent, text="Results & Analytics", font=('Arial', 14, 'bold'),
                bg='white', fg='#2c3e50').pack(pady=15)
        
        # Total emissions display
        self.total_frame = tk.Frame(parent, bg='#3498db', relief='raised', bd=2)
        self.total_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(self.total_frame, text="Total CO2 Emissions", 
                font=('Arial', 10, 'bold'), bg='#3498db', fg='white').pack(pady=(10, 5))
        
        self.total_label = tk.Label(self.total_frame, text="0.00 kg", 
                                    font=('Arial', 24, 'bold'), bg='#3498db', fg='white')
        self.total_label.pack(pady=(0, 10))
        
        # Emissions list
        tk.Label(parent, text="Emission Entries:", font=('Arial', 10, 'bold'),
                bg='white').pack(anchor='w', padx=20, pady=(10, 5))
        
        # Scrollable frame for entries
        list_frame = tk.Frame(parent, bg='white')
        list_frame.pack(fill='both', expand=True, padx=20, pady=5)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.emissions_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                           font=('Courier', 9), bg='#ecf0f1',
                                           relief='sunken', bd=2)
        self.emissions_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.emissions_listbox.yview)
        
        # Buttons
        button_frame = tk.Frame(parent, bg='white')
        button_frame.pack(fill='x', padx=20, pady=15)
        
        tk.Button(button_frame, text="📊 Visualize", command=self.visualize,
                 bg='#9b59b6', fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', cursor='hand2').pack(side='left', padx=5, pady=5, expand=True, fill='x')
        
        tk.Button(button_frame, text="💾 Save Report", command=self.save_report,
                 bg='#16a085', fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', cursor='hand2').pack(side='left', padx=5, pady=5, expand=True, fill='x')
        
        tk.Button(button_frame, text="🗑️ Clear All", command=self.clear_all,
                 bg='#e67e22', fg='white', font=('Arial', 9, 'bold'),
                 relief='flat', cursor='hand2').pack(side='left', padx=5, pady=5, expand=True, fill='x')
        
    def add_transportation(self):
        try:
            mode = self.transport_mode.get()
            distance = float(self.transport_distance.get())
            
            if distance <= 0:
                messagebox.showerror("Error", "Distance must be greater than 0")
                return
            
            self.analyzer.add_transportation(mode, distance)
            self.update_display()
            self.transport_distance.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added {distance} km by {mode}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for distance")
    
    def add_energy(self):
        try:
            energy_type = self.energy_type.get()
            amount = float(self.energy_amount.get())
            
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0")
                return
            
            self.analyzer.add_energy(energy_type, amount)
            self.update_display()
            self.energy_amount.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added {amount} kWh of {energy_type}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for amount")
    
    def add_food(self):
        try:
            food_type = self.food_type.get()
            quantity = float(self.food_quantity.get())
            
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be greater than 0")
                return
            
            self.analyzer.add_food(food_type, quantity)
            self.update_display()
            self.food_quantity.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added {quantity} of {food_type}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for quantity")
    
    def update_display(self):
        # Update total
        total = self.analyzer.get_total_emissions()
        self.total_label.config(text=f"{total:.2f} kg")
        
        # Update list
        self.emissions_listbox.delete(0, tk.END)
        for item in self.analyzer.emissions:
            entry = f"{item['category']:12} | {item['type']:12} | {item['amount']:6.1f} {item['unit']:5} | {item['co2_kg']:8.2f} kg CO2"
            self.emissions_listbox.insert(tk.END, entry)
    
    def visualize(self):
        if not self.analyzer.emissions:
            messagebox.showwarning("Warning", "No emissions data to visualize!")
            return
        
        self.analyzer.visualize()
    
    def save_report(self):
        if not self.analyzer.emissions:
            messagebox.showwarning("Warning", "No emissions data to save!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile="co2_emissions_report.csv"
        )
        
        if filename:
            self.analyzer.save_report(filename)
            messagebox.showinfo("Success", f"Report saved to {filename}")
    
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all data?"):
            self.analyzer = CO2Analyzer()
            self.update_display()
            messagebox.showinfo("Cleared", "All emission data has been cleared")


def main():
    try:
        root = tk.Tk()
        
        # Force window to appear on top
        root.lift()
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)
        
        # Center the window on screen
        root.update_idletasks()
        width = 900
        height = 700
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Create the app
        app = CO2AnalyzerGUI(root)
        
        print("✓ GUI window should now be visible!")
        print("If you still don't see it, check your taskbar or press Alt+Tab")
        
        # Start the GUI loop
        root.mainloop()
        
    except Exception as e:
        print(f"Error creating GUI: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Starting CO2 Analyzer GUI...")
    main()