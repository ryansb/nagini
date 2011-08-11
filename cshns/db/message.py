#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Message object, associated with a queue

from cshns.db.model import Model

class Message(Model):
	def __init__(cls, queue, user, connection):
		Model.__init__(cls, connection)

	@classmethod
	def put(cls):
		#Should save the object, if the object doesn't have an ID yet, create one
		if not cls.id:
			from random import randint
			rand = randint(1000000000000, 9999999999999)
			cls.id = "MSG-%s-%s" % (cls.queue.name[0:3], rand)
		raise NotImplementedError, "Not yet supported"
