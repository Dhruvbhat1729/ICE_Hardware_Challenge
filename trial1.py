import ltspice
import numpy as np
import matplotlib.pyplot as plt
# Define circuit parameters
battery_voltage = 4.1  # V
upper_threshold_voltage = 4.1  # V
lower_threshold_voltage = 3.9  # V
supply_voltage = 9  # V
hysteresis_voltage = 0.2  # V
input_impedance = 1e6  # Ohms

# Calculate resistor values
vdiv = 0.8
r2 = 10e3  # Start with a standard value
r1 = 4 * r2
r3 = r2

# Check input impedance
input_voltage = (upper_threshold_voltage + lower_threshold_voltage) / 2
input_current = input_voltage / input_impedance
input_voltage_drop = input_current * r2
if input_voltage_drop > input_voltage / 10:
    print("Warning: input impedance is too low")

# Print resistor values
print(f"R1 = {r1/1000:.1f} kOhms")
print(f"R2 = {r2/1000:.1f} kOhms")
print(f"R3 = {r3/1000:.1f} kOhms")

# Run LTspice simulation
l = ltspice.Ltspice('schmitt_trigger(1).asc')
l.set_parameter("V_battery", battery_voltage)
l.set_parameter("V_upper", upper_threshold_voltage)
l.set_parameter("V_lower", lower_threshold_voltage)
l.set_parameter("V_supply", supply_voltage)
l.set_parameter("Vdiv", vdiv)
l.set_parameter("R2", r2)
l.set_parameter("R3", r3)
l.run()

# Extract simulation data
time = l.get_time()
voltage = l.get_data('V(out)')

# Plot simulation data
plt.plot(time, voltage)
plt.xlabel('Time (s)')
plt.ylabel('Output Voltage (V)')
plt.show()
