#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Message object, associated with a queue

from cshns.db.model import Model

class Message(Model):
	def __init__(cls):
		Model.__init__(cls)
