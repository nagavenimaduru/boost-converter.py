```python
# Boost Converter Calculator
# Calculates output voltage, duty cycle, and output power

print("=== BOOST CONVERTER CALCULATOR ===")

# Input values
Vin = float(input("Enter input voltage (V): "))
duty_cycle = float(input("Enter duty cycle (%): "))
load_current = float(input("Enter load current (A): "))

# Convert duty cycle from percentage to decimal
D = duty_cycle / 100

# Check valid duty cycle
if D >= 1 or D < 0:
    print("Error: Duty cycle must be between 0% and 100%.")
else:
    # Ideal boost converter equation
    # Vout = Vin / (1 - D)
    Vout = Vin / (1 - D)

    # Output power
    Pout = Vout * load_current

    # Input current (ideal converter)
    Iin = Pout / Vin

    print("\n=== RESULTS ===")
    print(f"Input Voltage      : {Vin:.2f} V")
    print(f"Duty Cycle         : {duty_cycle:.2f} %")
    print(f"Output Voltage     : {Vout:.2f} V")
    print(f"Load Current       : {load_current:.2f} A")
    print(f"Output Power       : {Pout:.2f} W")
    print(f"Input Current      : {Iin:.2f} A")
```
