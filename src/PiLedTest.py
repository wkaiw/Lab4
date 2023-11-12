import RPi.GPIO as GPIO
import time


try:
    while True:
        # Read the state of the switch
        switch_state = GPIO.input(switch_pin)

        if switch_state == GPIO.LOW:
            # If the switch is in the left position, blink the LED at 5 Hz
            while True:
                GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
                time.sleep(0.1)  # Delay for 100 ms (half of the 5 Hz period)
                GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
                time.sleep(0.1)  # Delay for 100 ms (half of the 5 Hz period)
        else:
            # If the switch is not in the left position, turn off the LED
            GPIO.output(led_pin, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
