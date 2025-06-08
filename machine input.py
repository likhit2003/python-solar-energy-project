# Get electricity usage from 3 machines
m1 = float(input("Machine 1 usage (kWh): "))
m2 = float(input("Machine 2 usage (kWh): "))
m3 = float(input("Machine 3 usage (kWh): "))

# Find the machine with the highest usage
if m1 >= m2 and m1 >= m3:
    most = "Machine 1"
    usage = m1
elif m2 >= m1 and m2 >= m3:
    most = "Machine 2"
    usage = m2
else:
    most = "Machine 3"
    usage = m3

# Output result
print(f"\n{most} consumes the most electricity: {usage} kWh")
print(f"Electricity is now diverted to {most} from the solar panel.")
