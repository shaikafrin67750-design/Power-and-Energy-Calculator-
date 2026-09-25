# Power and Energy Calculator

print("===== POWER AND ENERGY CALCULATOR =====")
print("1. Calculate Power")
print("2. Calculate Energy")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    power = voltage * current

    print("\n===== RESULT =====")
    print("Power =", round(power, 2), "W")
    print("Power =", round(power / 1000, 3), "kW")

elif choice == 2:
    power = float(input("Enter power (W): "))
    time = float(input("Enter usage time (hours): "))

    energy_wh = power * time
    energy_kwh = energy_wh / 1000

    print("\n===== RESULT =====")
    print("Energy =", round(energy_wh, 2), "Wh")
    print("Energy =", round(energy_kwh, 2), "kWh")

else:
    print("Invalid choice!")