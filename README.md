# ICE_Hardware_Challenge

Circuit parameters are defined first such as input frequency, amplitude, and cutoff frequency. Values of capacitors and resistors are calculated. 

Next, we run the LTspice simulation by creating an instance of the Ltspice class and specifying the required parameters using the set_parameter() method. Then call the run() method to run the simulation and obtain the output waveform data.

Finally, we extract the simulation data using the get_time() and get_data() methods of the Ltspice object, and plot the output waveform using the plot() function from the matplotlib library.

Note that you will need to create an LTspice schematic file named differentiator.asc that contains the differentiator circuit, and place it in the same directory as the Python script. The schematic file should have a voltage source named Vin as the input, and a voltage output named Vout as the output. You should also include a .param statement for each parameter that is used in the circuit, and reference these parameters in the component values. For example, the value of resistor R1 in the schematic file should be specified as R1 {R1}, where {R1} is the name of the parameter that is set in the Python script using the set_parameter() method.
