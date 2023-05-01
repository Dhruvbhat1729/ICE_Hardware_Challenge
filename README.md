# ICE_Hardware_Challenge

## Introduction to Opamps 
Operational amplifiers are high-gain electronic device that amplifies the difference between two input signals. Op-amps are widely used in many electronic applications because of their versatility, high gain, and ease of use.

Op-amps have two input pins (inverting and non-inverting) and one output pin. The output of the op-amp is proportional to the difference between the voltages at its two input pins, with a gain determined by the op-amp's internal circuitry.

 <img src = "https://github.com/Dhruvbhat1729/ICE_Hardware_Challenge/blob/main/opamps.png" alt = "Opamps" width = "20%" /> </br>

Opamps can be used in both linear and non linear applications. 
- Linear applications include amplifiers, filters, voltage regulators and signal conditioners. 
- Non linear applications include Schmitt Triggers, comparators and oscillators. 

## Circuit Design

<img src = "https://github.com/Dhruvbhat1729/ICE_Hardware_Challenge/blob/main/spice_schematic.PNG" alt = "LT Spice Schematic" width = "60%" /> </br>

The circuit shown above uses the TL341 device as a comparator, with the reference voltage set to the desired trigger threshold. The voltage on the reference (REF) pin can be adjusted by setting the value of the resistor branch, which is formed by R1 and R2 to create a potential divider circuit. The formula for calculating the voltage on the REF pin is Vref = Vcc x R2 / (R1 + R2), where Vcc is the supply voltage.

This circuit is both accurate and low-cost, thanks to the accuracy and low cost of modern resistors. The TL431 is an adjustable shunt voltage reference that can take an input voltage and produce a regulated output voltage based on the device's characteristics. The TL431's internal reference voltage is 2.5V, which is used as the reference voltage for this circuit.

Overall, this circuit provides an adjustable voltage reference that can be used in various applications that require a regulated voltage source. By adjusting the value of R1 and R2, the output voltage of the circuit can be easily set to the desired value.

## Software Requirements

- Python
- LtSpice library

## Set Up
 
### Environment Setup
- Set up a python environment. 
- Install LtSpice library.
        ```
        pip install ltspice
        ``` <br>
        
 ### LTspice setup
1. Download [TL431.asy](https://github.com/Dhruvbhat1729/ICE_Hardware_Challenge/blob/main/TL431_8inch.asy) file. <br>
2. Copy the downloaded file and go to the directory where LtSpice is installed, locate sym folder inside LtSpic and paste the file.
   Eg: C:\Program Files\LTC\LTspiceXVII\lib\sym. <br>
3. Download [TL431.cir](https://github.com/Dhruvbhat1729/ICE_Hardware_Challenge/blob/main/TL431.cir). <br>
4. Once TL431.cir is downloaded click on the file and open it on LtSpice. <br>
5. Right click on rge [highlighted text](https://github.com/Dhruvbhat1729/ICE_Hardware_Challenge/blob/main/createsymbol.PNG) in TL431.cir and create a symbol. <br>
6. Go to components and choose TL431. <br>

### Running LTspice file 

- Change the voltage and observe the current accross the LED's. <br>
- Observe the current accross LED1 and LED2. <br>
- If the voltage is beyond the range (3.3>v<3.9), we observe that LED1 conducts. <br>
- Check with voltage <4.1V. Both LED1 and LED2 conducts. 
- In case the circuit does not work, close the files and open them again. 

### Launching LTspice on python

- Open the python file. Give the right path and run the code. 

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
