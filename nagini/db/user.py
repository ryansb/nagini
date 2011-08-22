#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: User object, associated with queues

from nagini.db.model import Model

class User(Model):
	def __init__(self, shortname, passwd, longname=None, devices=[]):
		self.name = shortname
		self.fullname = shortname
		if longname: self.fullname = longname
		self.passwd = prep_password(passwd)
		self.devices = devices
		Model.__init__(self)

	def validate(self, attempted_passwd):
		if prep_password(attempted_passwd) == self.passwd:
			return True
		return False

def prep_password(passwd):
	import hashlib
	return hashlib.sha512(passwd).hexdigest()
