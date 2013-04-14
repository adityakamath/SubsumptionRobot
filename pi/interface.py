#!/usr/bin/env python
import abc

class Interface(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def consume(self):
		pass
		
	@abc.abstractmethod	
	def publish(self):
		pass
