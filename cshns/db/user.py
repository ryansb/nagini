#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: User object, associated with queues

from cshns.db.model import Model

class User(Model):
	def __init__(cls, connection):
		Model.__init__(cls, connection)

	def generate_id(cls):
		from random import randint
		rand = randint(1000000000000, 9999999999999)
		cls.id = "USR-%s-%s" % (cls.name[0:3], rand)
