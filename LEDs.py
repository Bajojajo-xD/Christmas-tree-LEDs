import RPi.GPIO as GPIO
import time

try:
	# Configure Diodes and buttons
	workingLed = 4
	led = 13; led2 = 5; led3 = 6
	btn = 17

	# Configure GPIOs and vars
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	GPIO.setup(workingLed, GPIO.OUT)
	GPIO.output(workingLed, True)

	GPIO.setup(led, GPIO.OUT)
	GPIO.setup(led2, GPIO.OUT)
	GPIO.setup(led3, GPIO.OUT)
	GPIO.setup(btn, GPIO.IN)
	print (" ")
	print ("\rCurrent mode => 0 <=", end='\r')

	clicked = 0; btnCnt = 0

	# Main loop
	while True:

		# Detect button click
		if GPIO.input(btn) and not clicked:
			clicked = 1
			timer = 0
			btnCnt = btnCnt + 1
			print ("\rCurrent mode => " + str(btnCnt) + " <=", end='\r')

		# Detect end of one click
		if not GPIO.input(btn) and clicked:
			clicked = 0

		# Diodes off
		if btnCnt == 0:
			GPIO.output(led, False)
			GPIO.output(led2, False)
			GPIO.output(led3, False)

		# Diodes style 1
		elif btnCnt == 1:
			if timer == 0:
				GPIO.output(led, True)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 500 and timeDelta < 2000:
				GPIO.output(led2, True)
			if timeDelta >= 1000 and timeDelta < 2500:
				GPIO.output(led3, True)
			if timeDelta >= 1500:
				GPIO.output(led, False)
			if timeDelta >= 2000:
				GPIO.output(led2, False)
			if timeDelta >= 2500:
				GPIO.output(led3, False)
			if timeDelta >= 3000:
				timer = 0

		# Diodes style 2
		elif btnCnt == 2:
			if timer == 0:
				GPIO.output(led, False)
				GPIO.output(led2, False)
				GPIO.output(led3, True)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 500 and timeDelta < 2000:
				GPIO.output(led2, True)
			if timeDelta >= 1000 and timeDelta < 2500:
				GPIO.output(led, True)
			if timeDelta >= 1500:
				GPIO.output(led3, False)
			if timeDelta >= 2000:
				GPIO.output(led2, False)
			if timeDelta >= 2500:
				GPIO.output(led, False)
			if timeDelta >= 3000:
				timer = 0

		# Diodes style 3
		elif btnCnt == 3:
			if timer == 0:
				GPIO.output(led, True)
				GPIO.output(led2, False)
				GPIO.output(led3, False)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 500 and timeDelta < 2000:
				GPIO.output(led2, True)
			if timeDelta >= 1000 and timeDelta < 2500:
				GPIO.output(led3, True)
			if timeDelta >= 1500 and timeDelta < 3000:
				GPIO.output(led, False)
			if timeDelta >= 2000 and timeDelta < 3500:
				GPIO.output(led2, False)
			if timeDelta >= 2500 and timeDelta < 4000:
				GPIO.output(led3, False)
			if timeDelta >= 3000 and timeDelta < 4500:
				GPIO.output(led3, True)
			if timeDelta >= 3500 and timeDelta < 5000:
				GPIO.output(led2, True)
			if timeDelta >= 4000 and timeDelta < 5500:
				GPIO.output(led, True)
			if timeDelta >= 4500:
				GPIO.output(led3, False)
			if timeDelta >= 5000:
				GPIO.output(led2, False)
			if timeDelta >= 5500:
				GPIO.output(led, False)
			if timeDelta >= 6000:
				timer = 0

		# Diodes style 4
		elif btnCnt == 4:
			if timer == 0:
				GPIO.output(led, True)
				GPIO.output(led2, False)
				GPIO.output(led3, True)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 1000:
				GPIO.output(led, False)
				GPIO.output(led2, True)
				GPIO.output(led3, False)
			if timeDelta >= 2000:
				timer = 0

		# Diodes style 5
		elif btnCnt == 5:
			if timer == 0:
				GPIO.output(led, True)
				GPIO.output(led2, True)
				GPIO.output(led3, True)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 50:
				GPIO.output(led, False)
				GPIO.output(led2, False)
				GPIO.output(led3, False)
			if timeDelta >= 400:
				timer = 0

		# Diodes style 6
		elif btnCnt == 6:
			if timer == 0:
				GPIO.output(led, True)
				GPIO.output(led2, False)
				GPIO.output(led3, True)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 50:
				GPIO.output(led, False)
				GPIO.output(led3, False)
			if timeDelta >= 400 and timeDelta < 450:
				GPIO.output(led2, True)
			if timeDelta >= 450:
				GPIO.output(led2, False)
			if timeDelta >= 700:
				timer = 0

		# Diodes style 7
		elif btnCnt == 7:
			if timer == 0:
				GPIO.output(led, True)
				GPIO.output(led2, False)
				GPIO.output(led3, False)
				timer = time.time()
			timeDelta = (time.time() - timer) * 1000
			if timeDelta >= 100 and timeDelta < 400:
				GPIO.output(led2, True)
			if timeDelta >= 200 and timeDelta < 400:
				GPIO.output(led3, True)
			if timeDelta >= 400:
				GPIO.output(led, False)
				GPIO.output(led2, False)
				GPIO.output(led3, False)
			if timeDelta >= 700:
				timer = 0

		# Diodes always on
		elif btnCnt == 8:
			GPIO.output(led, True)
			GPIO.output(led2, True)
			GPIO.output(led3, True)

		# Go back to diodes off
		else:
			print ("\rCurrent mode => 0 <=", end='\r')
			btnCnt = 0

# Detect Ctrl + C
except KeyboardInterrupt:
	print ("\r=> STOP <= request detected, cleaning out...", end='\r')
	GPIOs = [2, 3, 4, 5, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
	for x in GPIOs:
        	GPIO.setup(x, GPIO.OUT)
        	GPIO.output(x, GPIO.LOW)
	time.sleep(1)
	GPIO.cleanup()

	print ("\rAs you requested, => STOPPED <= the program, hope you enjoyed!")
	print (" ")
