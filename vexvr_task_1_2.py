# Library imports
from vexcode import *
from math import *
from random import randint


drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()


def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!

        currentXLocation = location.position(X,MM)

        error = setpoint - currentXLocation
        k = 1
        output_speed = k*error

        if(output_speed > 100):
            output_speed = 100
        elif(output_speed < -100):
            output_speed = -100

        drivetrain.set_drive_velocity(output_speed, PERCENT)
        if( currentXLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentXLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()


        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()
    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentYLocation = location.position(Y,MM)
        
        if( currentYLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()


        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()
    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        
        currentYLocation = location.position(Y,MM)
        
        error = setpoint - currentYLocation
        k = 1
        output_speed = k*error

        if(output_speed > 100):
            output_speed = 100
        elif(output_speed < -100):
            output_speed = -100

        drivetrain.set_drive_velocity(output_speed, PERCENT)
        if(currentYLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,5)
    drivetrain.set_drive_velocity(100,PERCENT)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,5)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(400,4)
# VR threads — Do not delete
vr_thread(main())
