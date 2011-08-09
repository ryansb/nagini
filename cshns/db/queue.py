#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Queue object, contains messages, has users

from cshns.db.model import Model

class Queue(Model):
	def __init__(cls):
		Model.__init__(cls)
