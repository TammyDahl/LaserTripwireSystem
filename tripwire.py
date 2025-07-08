import RPi.GPIO as GPIO
import time
import requests

LDR_PIN = 4  # GPIO pin connected to the LDR
IFTTT_URL = "https://maker.ifttt.com/trigger/motion_detected/with/key/QGj2DX35Oj4usMahlU0BE"

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

no_signal_count = 0  # Tracks no-signal duration
max_no_signal_time = 5  # Max allowed no-signal time (seconds)
last_notification_time = 0  # Timestamp of last notification
notification_interval = 10  # Minimum time between notifications (seconds)

try:
    print("Starting LDR monitoring...")

    while True:
        pin_state = GPIO.input(LDR_PIN)  # Read LDR state

        if pin_state == GPIO.HIGH:  # Light detected
            print("LDR is detecting light!")
            no_signal_count = 0
        elif pin_state == GPIO.LOW:  # Darkness detected
            print("LDR is in the dark!")
            no_signal_count = 0

            # Send notification if interval has elapsed
            if time.time() - last_notification_time > notification_interval:
                print("Triggering IFTTT Webhook...")
                response = requests.post(IFTTT_URL)
                if response.status_code == 200:
                    print("Trigger sent successfully!")
                else:
                    print(f"Failed to send notification: {response.status_code}")
                last_notification_time = time.time()

        else:
            print("Unknown GPIO state!")  # Handle unexpected state

        no_signal_count += 1
        # Alert if no signal exceeds max allowed time
        if no_signal_count > (max_no_signal_time / 0.1):
            print("WARNING: No input detected for over 5 seconds!")
            no_signal_count = 0

        time.sleep(0.1)  # Monitoring frequency delay

except KeyboardInterrupt:
    print("Program stopped by user.")
finally:
    GPIO.cleanup()  # Clean up GPIO resources

