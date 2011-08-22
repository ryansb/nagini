#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Message object, associated with a queue

from nagini.db.model import Model

class Message(Model):
	def __init__(cls, queue, user):
		Model.__init__(cls)
