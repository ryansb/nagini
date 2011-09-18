#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: User object, associated with queues

from nagini.db.model import Model
from nagini.db.property import PasswordProperty

class User(Model):
	def __init__(self, shortname='', passwd='', longname=None, devices=[]):
		self.name = shortname
		self.fullname = shortname
		if longname: self.fullname = longname
		self.passwd = PasswordProperty(passwd)
		self.devices = devices
		Model.__init__(self)
