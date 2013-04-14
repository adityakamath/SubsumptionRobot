#!/usr/bin/env python
import serial
import time
from interface import Interface

class SerialInterface(Interface):
	
	def __init__(self):
		# Configure the Serial port
		self.ser = serial.Serial(port='/dev/ttyUSB1',
									baudrate=9600,
									parity=serial.PARITY_ODD,
									stopbits=serial.STOPBITS_TWO,
									bytesize=serial.SEVENBITS
								)
		self.from_arduino = ''		
								
	def consume(self):
		
		self.ser.open()
		
		if not self.ser.isOpen()
			raise Exception("Serial port isn't open")
			
		# read some messages
		while 1:
			time.sleep(1)
			self.from_arduino = ''
			while ser.inWaiting() > 0:
				self.from_arduino += ser.read(1)
			
			if self.from_arduino != '':
				
				# Put the messages on the queue 
				# TODO
				# Clear the buffer down
				self.from_arduino = ''
				
		
		
	def publish(self, message):
		
		self.ser.write(message + '\r\n')
	
	
	
	
