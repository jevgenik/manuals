.. _motor_drivers:

=============
Motor Drivers
=============

DC motor drivers
================
is a circuit that drives the :ref:`motor <electric_motors>` with higher current than the microcontroller can provide.

.. figure:: ../../images/electronics/motor_driver_L298N.jpg
   :alt: Motor driver L298N
   :width: 400

   L298N motor driver

.. warning::
   If the motor supply voltage is up to 12V we can enable the 5V regulator and the 5V pin can be used as output, 
   for example for powering our Arduino board. But if the motor voltage is greater than 12V we must disconnect 
   the jumper because those voltages will cause damage to the onboard 5V regulator

   Also, do not supply power to both the VSS (5V-35V) and VS (5V) pins while the jumper is in place.

.. figure:: ../../images/electronics/motor_driver_and_arduino.png
   :alt: Motor driver L298N and Arduino
   :width: 100%

   L298N motor driver and Arduino

   `Interface L298N with Arduino (detailed explanation) <https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/>`_

.. _bldc_motor_drivers:

BLDC motor drivers
==================
**ESC or Electronic Speed Controller** controls the :ref:`brushless motor <bldc_motors>` movement or speed by activating the appropriate MOSFETs  
to create the rotating magnetic field so   that the motor rotates.  The higher the frequency or the quicker the ESC goes  
through   the 6 intervals, the higher the speed of the motor will be.  

.. image:: ../../images/electronics/bldc_and_esc.jpg
   :alt: BLDC motor and ESC
   :width: 700
  
.. image:: ../../images/electronics/bldc_and_arduino.png
   :alt: BLDC motor and Arduino
   :width: 700
  