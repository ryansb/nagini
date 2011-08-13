#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Message object, associated with a queue

from cshns.db.model import Model

class Message(Model):
	def __init__(cls, queue, user, connection):
		Model.__init__(cls, connection)

	def generate_id(cls):
		from random import randint
		rand = randint(1000000000000, 9999999999999)
		cls.id = "MSG-%s-%s" % (cls.queue.name[0:3], rand)
