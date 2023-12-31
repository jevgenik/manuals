# Motor Drivers

## DC motor drivers
is a circuit that drives the [motor](electrical_motors.md) with higher current than the microcontroller can provide.

<div style="display: flex; align-items: flex-end;">  
  <img src="../../images/electronics/motor_driver_L298N.jpg" alt="Motor driver L298N" width="300">  
  &nbsp; &nbsp;  
  <img src="../../images/electronics/motor_driver_and_arduino.png" alt="Motor driver L298N and Arduino" width="690">  
</div>

## BLDC motor drivers {#bldc-motor-drivers}
**ESC or Electronic Speed Controller** controls the [brushless motor](electrical_motors.md/#bldc-motors) movement or speed by activating the appropriate MOSFETs  
to create the rotating magnetic field so   that the motor rotates.  The higher the frequency or the quicker the ESC goes  
through   the 6 intervals, the higher the speed of the motor will be.  

<div style="display: flex; align-items: flex-end;">
  <img src="../../images/electronics/bldc_and_esc.jpg" alt="BLDC motor and ESC" width="495"> 
  &nbsp; &nbsp;
  <img src="../../images/electronics/bldc_and_arduino.png" alt="BLDC motor and Arduino" width="495"> 
</div>