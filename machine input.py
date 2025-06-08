
machine1 = float(input("Enter electricity used by Machine 1 (in kWh): "))
machine2 = float(input("Enter electricity used by Machine 2 (in kWh): "))
machine3 = float(input("Enter electricity used by Machine 3 (in kWh): "))

machines = {
    "Machine 1": machine1,
    "Machine 2": machine2,
    "Machine 3": machine3
}

max_machine = max(machines, key=machines.get)
max_value = machines[max_machine]

print(f"\n{max_machine} consumes the most electricity: {max_value} kWh")
print(f"Electricity is now diverted to {max_machine} from the solar panel.")