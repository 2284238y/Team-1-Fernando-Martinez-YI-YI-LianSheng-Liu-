# Intelligent Blind System

[List of Changes]

Automatically controlled curtains that can rise and fall. The Intelligent blind system should be controled by using a Raspberry Pi. This system has three different control modes, they are shown below:

- Photo sensitive control

- Time control

- User interface control

# System Block Diagram

<img width="1166" alt="2018-04-12 22 46 52" src="https://user-images.githubusercontent.com/37375752/38706002-85e27a24-3ea3-11e8-862f-baba51e45647.png">

# System Flow Chart

![flow chart](https://user-images.githubusercontent.com/37375752/38773667-6776914e-404a-11e8-9d80-2cdd4ab1935c.png)

# Components

* Photo resistor
  
<img width="184" alt="2018-04-12 23 20 01" src="https://user-images.githubusercontent.com/37375752/38708106-89ce6aa4-3eac-11e8-9d23-d1b493c00c54.png">

At the same time, we also designed the PCB of the light sensor.For the light sensor of PCB, OPT3001DNPR is used here.
The PCB files for the light sensor can be found in the hardware(PCB) folder. 

* Motor

The motor PCB board can be found in the hardware(PCB) folder. The components used:

Motor: 719RE380
Motor Controller: L293D

The motor PCB should be controlled using the GPIO pins on the raspberry Pi.

* Battery: Adafruit Micro Lipo

<img width="284" alt="2018-04-12 23 46 14" src="https://user-images.githubusercontent.com/37375752/38708085-703bbb64-3eac-11e8-86c0-1710b2c9dc02.png">

* Elegoo uno R3

<img width="373" alt="2018-04-12 23 21 59" src="https://user-images.githubusercontent.com/37375752/38708101-81ec97c0-3eac-11e8-9d2b-134c1e324407.png">

More details about the hardware design and software design can be found in the [wiki](https://github.com/2284238y/Team-1-Fernando-Martinez-YI-YI-LianSheng-Liu-/wiki)

* Proximity Sensor

The PCB files for the proximity sensor can be found in the hardware(PCB) folder. 

The proximity sensor used: APDS-9960

A suggested I2C switch: PCA9543 or a multiplier should be used (TODO).

# Social media engagement

  Twitter: @InteBliSym [Intelligent Blind System](https://twitter.com/InteBliSym)
