##Using Python 3.6.5

##Import the local sensors library
import sensors

##Test: check that the front sensor is correctly wired and functional
##Expected result: prints:
##<Front Distance Measurement in Progress
## xx.xx cm>
print("\n\nStarting Test: sensors_test1\n\n")
front_distance = sensors.front_distance()

##Troubleshooting:

## Error 1:
## <Traceback (most recent call last):
## File "sensors_test.py", line 22, in <module>
## print sensors.front_distance(), "cm"
## File "/home/pi/vforum2018/sensors.py", line 53, in front_distance
## pulse_duration = pulse_end - pulse_start>
## Cause: Theory: The sensor fails to trigger OR Theory: The sensor triggers before the RPi has a chance to capture the pre-trigger state
## Testing: The error appears randomly only on the front sensor (not on the rear sensor) with a frequency of approximately 1 in 3 attempts. Likely to be a faulty sensor or faulty connection
## Resolution: Replace front sensor for production. OR see comment in sensors.py "Give the sensor time to come online" - increase tf in time.sleep(tf)
