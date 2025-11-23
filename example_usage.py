"""
Custom usage example for CO2 Analyzer
Modify this file to track your own emissions
"""

from co2_analyzer import CO2Analyzer

# Create a new analyzer
my_analyzer = CO2Analyzer()

print("🌍 Tracking My Weekly Carbon Footprint")
print("-" * 60)

# === TRANSPORTATION ===
print("\n🚗 Transportation:")
my_analyzer.add_transportation('car', 100)    # Change to your km
my_analyzer.add_transportation('bus', 30)     # Change to your km

# === ENERGY ===
print("\n⚡ Energy Usage:")
my_analyzer.add_energy('electricity', 250)    # Change to your kWh
my_analyzer.add_energy('natural_gas', 100)    # Change to your kWh

# === FOOD ===
print("\n🍔 Food:")
my_analyzer.add_food('meat', 3)               # Change to your kg
my_analyzer.add_food('vegetarian', 15)        # Change to your meals

# === RESULTS ===
my_analyzer.get_summary()
my_analyzer.visualize()
my_analyzer.save_report('my_weekly_emissions.csv')