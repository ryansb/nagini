#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: User object, associated with queues

from cshns.db.model import Model

class User(Model):
	def __init__(self, shortname, passwd, longname=None, devices=[]):
		self.name = shortname
		self.fullname = shortname
		if longname: self.fullname = longname
		self.passwd = prep_password(passwd)
		self.devices = devices
		Model.__init__(self)

	def generate_id(cls):
		from random import randint
		rand = randint(1000000000000, 9999999999999)
		cls.id = "USR-%s-%s" % (cls.name[0:3], rand)

def prep_password(passwd):
	import hashlib
	return hashlib.sha512(passwd).hexdigest()

