#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Property class. Model (and its subclasses) have properties

class Property(object):
	def __init__(cls, value):
		cls.value = value
		pass

class StringProperty(Property):
	def __init__(cls):
		Property.__init__(cls)

class ListProperty(Property):
	def __init__(cls):
		Property.__init__(cls)

