#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Model object, base for other DB objects like User and Message

class Model(object):
	def __init__(cls, connection):
		cls.conn = connection
		cls.type = 'model'
		cls.id = None
		pass

	def get_by_id(cls, id):
		cls.id = id
		raw = cls.conn.get(id)[0][0]
		cls.decode(raw)
		return cls

	def put(cls):
		#Should save the object, if the object doesn't have an ID yet, create one
		cls.conn.put(cls.id, cls.encode())
		return True

	def decode(cls, raw):
		#Decodes the pickled dict
		import base64
		import pickle
		decoded = base64.decodestring(raw)
		attrs = pickle.loads(decoded)
		for k, v in attrs.items():
			cls.__dict__[k] = v
		#take the keys and make them cls attributes
		#would be nice if we could take any items that are ID's and put the corresponding models in their place
		return attrs

	def encode(cls):
		import base64
		import pickle
		attrs = {}
		for k, v in cls.__dict__.items():
			if k == 'conn': continue
			attrs[k] = v
		#take all the cls attrs and make them key/value pairs in the dict
		pic = pickle.dumps(attrs)
		encoded = base64.encodestring(pic)
		return encoded


