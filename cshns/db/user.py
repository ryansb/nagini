#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: User object, associated with queues

from cshns.db.model import Model

class User(Model):
	def __init__(cls):
		Model.__init__(cls)
