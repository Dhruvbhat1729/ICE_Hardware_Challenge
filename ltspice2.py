import ltspice
import numpy as np
import matplotlib.pyplot as plt

# Define circuit parameters
battery_voltage = 4.1  # V
upper_threshold_voltage = 4.1  # V
middle_threshold_voltage = 3.9  # V
lower_threshold_voltage = 3.3 

# Calculate resistor values

 # Start with a standard value
r1 = 10e3
r3 = r1
r8 = r1

# Print resistor values
print(f"R1 = {r1/1000:.1f} kOhms")
print(f"R2 = {r2/1000:.1f} kOhms")
print(f"R3 = {r3/1000:.1f} kOhms")

# Run LTspice simulation
l = ltspice.Ltspice('schmitt_trigger(1).asc')
