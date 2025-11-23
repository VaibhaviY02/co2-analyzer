# VITyarthi-Python-Project-CSE1021 
# PROJECT - CO2 emission analyser

A simple Python tool to track and analyze your personal carbon footprint.

## Installation

1. Make sure you have Python 3.7+ installed
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the example:
```bash
python co2_analyzer.py
```

### Track your own emissions:
```bash
python example_usage.py
```

### Use in your own scripts:
```python
from co2_analyzer import CO2Analyzer

analyzer = CO2Analyzer()
analyzer.add_transportation('car', 50)
analyzer.add_energy('electricity', 300)
analyzer.get_summary()
analyzer.visualize()
```

## Features

- Track transportation emissions (car, bus, train, plane)
- Monitor energy usage (electricity, natural gas)
- Calculate food-related emissions
- Visualize your carbon footprint
- Export reports to CSV

## Emission Factors

The analyzer uses standard emission factors:
- Car: 0.192 kg CO2/km
- Bus: 0.089 kg CO2/km
- Electricity: 0.475 kg CO2/kWh
- And more...

## Future Enhancements

- Add more categories (waste, water)
- Monthly tracking
- Comparison with averages

- Reduction recommendations
