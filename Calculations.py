import ltspice
import numpy as np
import matplotlib.pyplot as plt
import subprocess 

# Define circuit parameters
battery_voltage = 4.1  # V
upper_threshold_voltage = 4.1  # V
middle_threshold_voltage = 3.9  # V
lower_threshold_voltage = 3.3 
Vref = 2.5
# Calculate resistor values

 # Start with a standard value
R1 = 10e3
R3 = R1
R8 = R1

#Calculating resistor values 
R2 = (R1/((lower_threshold_voltage/Vref)-1))
print('R2', R2)    

R7 = (R8/((upper_threshold_voltage/Vref)-1))
print('R7', R7)

# Set the path to LTspice and the simulation file
ltspice_path = 'C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe'
sim_file = r'<C:\Users\admin\Desktop\CPP\Python\tl431_battery_trigger_v2.asc>'

# Launch LTspice and open the simulation file
subprocess.Popen([ltspice_path, '-b', sim_file])
