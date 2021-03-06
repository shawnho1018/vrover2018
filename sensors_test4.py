##Using Python 3.6.5

##Import the local sensors library
import sensors

##Test: check that distance measurements take place between servo rotations
##Expected result: Servo motor moves to center, prints:
##<Watch me position center, take distance.
##Distance at front:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to left, prints:
##<Watch me position left, take distance.
##Distance to left:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to right, prints:
##<Watch me position right, take distance.
##Distance at right:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
##Servo motor moves to center, prints:
##<Watch me position center, take distance.
##Distance at front:
##Front Sensor Distance Measurement in Progress
#xx.xx cm>
print("\n\nStarting Test: sensors_test4\n\n")
sensors.pan_check_distance_1()

##Troubleshooting:
