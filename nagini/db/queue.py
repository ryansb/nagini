#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Queue object, contains messages, has users

from nagini.db.model import Model

class Queue(Model):
	def __init__(cls):
		Model.__init__(cls)

	def generate_id(cls):
		from random import randint
		rand = randint(1000000000000, 9999999999999)
		cls.id = "QUE-%s-%s" % (cls.name[0:3], rand)
