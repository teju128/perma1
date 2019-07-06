
import socket
import Jetson.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


host= '127.0.0.1'
port= 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((host, port))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('connected by',addr)
		while True:
			data = conn.recv(1024)			
			if not data:
				conn.sendall(b"not received")
				break
			conn.sendall(b"received")


x=255
y=0

motorenable = 162

motor1f = 38
motor1b = 511


motor2f = 219
motor2b = 186

motor3f = 63
motor3b = 8

motor4f = 11
motor4b = 37

motor5f = 184
motor5b = 510

motor6f = 19
motor6b = 20

rotationalenable = 36
motor7f = 163
motor7b = 187

motor8f = 9
motor8b = 10

GPIO.output(motor1f,GPIO.LOW)
GPIO.output(motor1b,GPIO.LOW)
GPIO.output(motor2f,GPIO.LOW)
GPIO.output(motor2b,GPIO.LOW)
GPIO.output(motor3f,GPIO.LOW)
GPIO.output(motor3b,GPIO.LOW)
GPIO.output(motor4f,GPIO.LOW)
GPIO.output(motor4b,GPIO.LOW)
GPIO.output(motor5f,GPIO.LOW)
GPIO.output(motor5b,GPIO.LOW)
GPIO.output(motor6f,GPIO.LOW)
GPIO.output(motor6b,GPIO.LOW)
GPIO.output(motor7f,GPIO.LOW)
GPIO.output(motor7b,GPIO.LOW)
GPIO.output(motor8f,GPIO.LOW)
GPIO.output(motor8b,GPIO.LOW)
GPIO.output(motorenable,GPIO.LOW)
GPIO.output(rotationalenable,GPIO.LOW)

while True:

	host= '127.0.0.1'
	port= 65432

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((host, port))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('connected by',addr)
			while True:
				val = conn.recv(1024)			
				if not val:
					conn.sendall(b"not received")
					break
				conn.sendall(b"received")

	GPIO.output(motorenable,GPIO.HIGH)

	#moving forward

	if(forward == 255):
		GPIO.output(motor1f,GPIO.HIGH)
		GPIO.output(motor1b,GPIO.LOW)
		GPIO.output(motor6f,GPIO.HIGH)
		GPIO.output(motor6b,GPIO.LOW)
		sleep(0.2)


	#moving backward
	if(moveback == 255):
		GPIO.output(motor1f,GPIO.LOW)
		GPIO.output(motor1b,GPIO.HIGH)
		GPIO.output(motor6f,GPIO.LOW)
		GPIO.output(motor6b,GPIO.HIGH)
		sleep(0.2)
	#moving sidewards

	#moving right
	if(right1 == 255):
		GPIO.output(rotationalenable,GPIO.HIGH)
		GPIO.output(motor7f,GPIO.HIGH)
		GPIO.output(motor7b,GPIO.LOW)
		sleep(0.2)

  	if(right2 == 255):
		GPIO.output(rotationalenable,GPIO.HIGH)
		GPIO.output(motor8f,GPIO.HIGH)
		GPIO.output(motor8b,GPIO.LOW)
		sleep(0.2)

	#moving left
	if(left1 == 255):
		GPIO.output(rotationalenable,GPIO.HIGH)
		GPIO.output(motor7f,GPIO.LOW)
		GPIO.output(motor7b,GPIO.HIGH)
		sleep(0.2)

	if(left2 == 255):
		GPIO.output(rotationalenable,GPIO.HIGH)
		GPIO.output(motor8f,GPIO.LOW)
		GPIO.output(motor8b,GPIO.HIGH)
		sleep(0.2)

    #links
	
	if(link1up == 255):
		GPIO.output(motor2f,GPIO.HIGH)
		GPIO.output(motor2b,GPIO.LOW)
		sleep(0.2)
	elif(link1down == 255):	
		GPIO.output(motor2f,GPIO.LOW)	
		GPIO.output(motor2b,GPIO.HIGH)
		sleep(0.2)
	elif(link2up == 255):	
		GPIO.output(motor3f,GPIO.HIGH)
		GPIO.output(motor3b,GPIO.LOW)
		sleep(0.2)
	elif(link2down == 255):	
		GPIO.output(motor3f,GPIO.LOW)
		GPIO.output(motor3b,GPIO.HIGH)
		sleep(0.2)
	elif(link3up == 255):
		GPIO.output(motor4f,GPIO.HIGH)	
		GPIO.output(motor4b,GPIO.LOW)
		sleep(0.2)
	elif(link3down == 255):
		GPIO.output(motor4f,GPIO.LOW)
		GPIO.output(motor4b,GPIO.HIGH)
		sleep(0.2)
    	elif(link4up == 255):
		GPIO.output(motor5f,GPIO.HIGH)	
		GPIO.output(motor5b,GPIO.LOW)
		sleep(0.2)
	elif(link4down == 255):
		GPIO.output(motor5f,GPIO.LOW)
		GPIO.output(motor5b,GPIO.HIGH)
		sleep(0.2)
