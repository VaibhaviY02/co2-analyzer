import tkinter as tk
from tkinter import messagebox, filedialog
from co2_analyzer import CO2Analyzer

class SimpleCO2GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CO2 Emission Analyzer")

        self.analyzer = CO2Analyzer()

        # Input fields
        tk.Label(root, text="Transport Mode (car/bus/train/plane):").pack()
        self.transport_mode = tk.Entry(root)
        self.transport_mode.pack()

        tk.Label(root, text="Transport Distance (km):").pack()
        self.transport_distance = tk.Entry(root)
        self.transport_distance.pack()

        tk.Button(root, text="Add Transportation", command=self.add_transport).pack(pady=5)

        tk.Label(root, text="Energy Type (electricity/gas):").pack()
        self.energy_type = tk.Entry(root)
        self.energy_type.pack()

        tk.Label(root, text="Energy Amount (kWh):").pack()
        self.energy_amount = tk.Entry(root)
        self.energy_amount.pack()

        tk.Button(root, text="Add Energy", command=self.add_energy).pack(pady=5)

        tk.Label(root, text="Food Type (meat/vegetarian):").pack()
        self.food_type = tk.Entry(root)
        self.food_type.pack()

        tk.Label(root, text="Food Quantity:").pack()
        self.food_quantity = tk.Entry(root)
        self.food_quantity.pack()

        tk.Button(root, text="Add Food", command=self.add_food).pack(pady=5)

        # Show total
        tk.Label(root, text="Total Emissions:").pack()
        self.total_label = tk.Label(root, text="0 kg")
        self.total_label.pack()

        # Listbox
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        # Buttons
        tk.Button(root, text="Visualize", command=self.visualize).pack(side="left", padx=5)
        tk.Button(root, text="Save Report", command=self.save_report).pack(side="left", padx=5)
        tk.Button(root, text="Clear All", command=self.clear_all).pack(side="left", padx=5)

    def add_transport(self):
        try:
            mode = self.transport_mode.get()
            distance = float(self.transport_distance.get())
            self.analyzer.add_transportation(mode, distance)
            self.update_display()
        except:
            messagebox.showerror("Error", "Enter valid transport values")

    def add_energy(self):
        try:
            etype = self.energy_type.get()
            amount = float(self.energy_amount.get())
            self.analyzer.add_energy(etype, amount)
            self.update_display()
        except:
            messagebox.showerror("Error", "Enter valid energy values")

    def add_food(self):
        try:
            ftype = self.food_type.get()
            qty = float(self.food_quantity.get())
            self.analyzer.add_food(ftype, qty)
            self.update_display()
        except:
            messagebox.showerror("Error", "Enter valid food values")

    def update_display(self):
        total = self.analyzer.get_total_emissions()
        self.total_label.config(text=f"{total:.2f} kg")

        self.listbox.delete(0, tk.END)
        for item in self.analyzer.emissions:
            self.listbox.insert(tk.END, str(item))

    def visualize(self):
        if self.analyzer.emissions:
            self.analyzer.visualize()
        else:
            messagebox.showwarning("Warning", "No data")

    def save_report(self):
        if not self.analyzer.emissions:
            messagebox.showwarning("Warning", "No data")
            return
        
        file = filedialog.asksaveasfilename(defaultextension=".csv")
        if file:
            self.analyzer.save_report(file)
            messagebox.showinfo("Saved", "Report saved")

    def clear_all(self):
        self.analyzer = CO2Analyzer()
        self.update_display()


def main():
    root = tk.Tk()
    app = SimpleCO2GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
