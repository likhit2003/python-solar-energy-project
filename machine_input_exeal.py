import pandas as pd

# Correct path to your Excel file
path = r"C:\Users\USER\Documents\usage.xlsx"

# Load Excel data
df = pd.read_excel(path)

# Convert data into a dictionary
machines = dict(zip(df['Machine'], df['Usage']))

# Find machine with highest usage
max_machine = max(machines, key=machines.get)
max_value = machines[max_machine]

# Output result
print(f"\n{max_machine} consumes the most electricity: {max_value} kWh")
print(f"Electricity is now diverted to {max_machine} from the solar panel.")
