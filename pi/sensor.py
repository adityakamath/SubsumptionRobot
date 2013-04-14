#!/usr/bin/env python
import abc

# consumes messages from a sensor (from an interface, e.g. rs-232)
# and then publishes the message

class Sensor(object):
	__metaclass__ = abc.ABCMeta

	def publish(self):
		pass
		
	def consume(self):	
		pass
		
