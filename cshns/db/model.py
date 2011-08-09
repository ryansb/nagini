#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Model object, base for other DB objects like User and Message

class Model(object):
	def __init__(cls):
		pass

	@classmethod
	def get_by_id(cls, id):
		raise NotImplementedError, "Not yet supported"

