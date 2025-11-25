import pandas as pd
import matplotlib.pyplot as plt

class CO2Analyzer:
    """A simple CO2 emission analyzer for personal carbon footprint"""
    
    def __init__(self):
        # Emission factors (kg CO2 per unit)
        self.emission_factors = {
            'car_km': 0.192,        # kg CO2 per km (average car)
            'bus_km': 0.089,        # kg CO2 per km
            'train_km': 0.041,      # kg CO2 per km
            'plane_km': 0.255,      # kg CO2 per km
            'electricity_kwh': 0.475,  # kg CO2 per kWh
            'natural_gas_kwh': 0.185,  # kg CO2 per kWh
            'meat_kg': 27.0,        # kg CO2 per kg (beef)
            'vegetarian_meal': 1.5  # kg CO2 per meal
        }
        
        self.emissions = []
    
    def add_transportation(self, mode, distance):
        """
        Add transportation emission
        mode: 'car', 'bus', 'train', or 'plane'
        distance: distance traveled in km
        """
        key = f"{mode}_km"
        if key in self.emission_factors:
            emission = distance * self.emission_factors[key]
            self.emissions.append({
                'category': 'Transportation',
                'type': mode.capitalize(),
                'amount': distance,
                'unit': 'km',
                'co2_kg': emission
            })
            print(f"✓ Added: {distance} km by {mode} = {emission:.2f} kg CO2")
        else:
            print(f"Error: Unknown mode '{mode}'")
    
    def add_energy(self, energy_type, amount):
        """
        Add energy consumption emission
        energy_type: 'electricity' or 'natural_gas'
        amount: energy used in kWh
        """
        key = f"{energy_type}_kwh"
        if key in self.emission_factors:
            emission = amount * self.emission_factors[key]
            self.emissions.append({
                'category': 'Energy',
                'type': energy_type.capitalize(),
                'amount': amount,
                'unit': 'kWh',
                'co2_kg': emission
            })
            print(f"✓ Added: {amount} kWh of {energy_type} = {emission:.2f} kg CO2")
        else:
            print(f"Error: Unknown energy type '{energy_type}'")
    
    def add_food(self, meal_type, quantity):
        """
        Add food emission
        meal_type: 'meat' or 'vegetarian'
        quantity: kg for meat, number of meals for vegetarian
        """
        if meal_type == 'meat':
            emission = quantity * self.emission_factors['meat_kg']
            unit = 'kg'
        elif meal_type == 'vegetarian':
            emission = quantity * self.emission_factors['vegetarian_meal']
            unit = 'meals'
        else:
            print(f"Error: Unknown meal type '{meal_type}'")
            return
        
        self.emissions.append({
            'category': 'Food',
            'type': meal_type.capitalize(),
            'amount': quantity,
            'unit': unit,
            'co2_kg': emission
        })
        print(f"✓ Added: {quantity} {unit} of {meal_type} = {emission:.2f} kg CO2")
    
    def get_total_emissions(self):
        """Calculate total CO2 emissions"""
        total = sum(item['co2_kg'] for item in self.emissions)
        return total
    
    def get_summary(self):
        """Print a summary of all emissions"""
        if not self.emissions:
            print("No emissions recorded yet!")
            return
        
        df = pd.DataFrame(self.emissions)
        
        print("\n" + "="*60)
        print("CO2 EMISSION SUMMARY")
        print("="*60)
        
        # Summary by category
        category_summary = df.groupby('category')['co2_kg'].sum()
        print("\nEmissions by Category:")
        for category, total in category_summary.items():
            print(f"  {category}: {total:.2f} kg CO2")
        
        print(f"\n{'Total CO2 Emissions:':<30} {self.get_total_emissions():.2f} kg")
        print(f"{'Equivalent to:':<30} {self.get_total_emissions()/1000:.3f} tonnes")
        print("="*60 + "\n")
    
    def visualize(self):
        """Create visualizations of emissions"""
        if not self.emissions:
            print("No emissions to visualize!")
            return
        
        df = pd.DataFrame(self.emissions)
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        # Pie chart by category
        category_totals = df.groupby('category')['co2_kg'].sum()
        ax1.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%',
                startangle=90, colors=['#ff6b6b', '#4ecdc4', '#45b7d1'])
        ax1.set_title('CO2 Emissions by Category', fontsize=14, fontweight='bold')
        
        # Bar chart by type
        type_totals = df.groupby('type')['co2_kg'].sum().sort_values(ascending=True)
        ax2.barh(type_totals.index, type_totals.values, color='#95e1d3')
        ax2.set_xlabel('CO2 Emissions (kg)', fontsize=12)
        ax2.set_title('CO2 Emissions by Type', fontsize=14, fontweight='bold')
        ax2.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def save_report(self, filename='co2_report.csv'):
        """Save emissions report to CSV file"""
        if not self.emissions:
            print("No emissions to save!")
            return
        
        df = pd.DataFrame(self.emissions)
        df.to_csv(filename, index=False)
        print(f"✓ Report saved to {filename}")


# Example usage
if __name__ == "__main__":
    print("🌍 CO2 Emission Analyzer")
    print("-" * 60)
    
    # Create analyzer instance
    analyzer = CO2Analyzer()
    
    # Add some sample data
    print("\n📊 Adding emissions data...\n")
    
    # Transportation
    analyzer.add_transportation('car', 50)      # 50 km by car
    analyzer.add_transportation('bus', 20)      # 20 km by bus
    analyzer.add_transportation('plane', 500)   # 500 km flight
    
    # Energy consumption
    analyzer.add_energy('electricity', 300)     # 300 kWh
    analyzer.add_energy('natural_gas', 150)     # 150 kWh
    
    # Food
    analyzer.add_food('meat', 2)                # 2 kg of meat
    analyzer.add_food('vegetarian', 10)         # 10 vegetarian meals
    
    # Display summary
    analyzer.get_summary()
    
    # Create visualizations
    analyzer.visualize()
    
    # Save report
    analyzer.save_report()
