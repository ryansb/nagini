#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Model object, base for other DB objects like User and Message

from cshns.db import get_manager


class Model(object):
	id = None
	_manager = get_manager()

	def __init__(cls):
		cls.type = 'model'
		cls.id = None
		pass

	#def get_by_id(cls, id):
		#cls.id = id
		#raw = cls.conn.get(id)[0][0]
		#cls.decode(raw)
		#return cls

	@classmethod
	def _get_by_id(cls, id, manager=None):
		if not manager:
			manager = cls._manager
		return manager.get_object(id)

	@classmethod
	def get_by_id(cls, ids=None):
		if isinstance(ids, list):
			objs = [cls._get_by_id(id) for id in ids]
			return objs
		else:
			raw = cls._get_by_id(ids)
			obj = Model()
			obj.decode(raw[0][0])
			return obj

	def put(cls):
		#Should save the object, if the object doesn't have an ID yet, create one
		if not cls.id: cls.generate_id(cls)
		cls.conn.put(cls.id, cls.encode())
		return True

	def generate_id(cls):
		from random import randint
		rand = randint(1000000000000, 9999999999999)
		cls.id = "MOD-%s" % rand

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


