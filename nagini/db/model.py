#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Model object, base for other DB objects like User and Message

from nagini.db import get_manager

class VoldKeyNotFound(Exception):
	def __init__(self, message):
		Exception.__init__(self, message)

class Model(object):
	_manager = get_manager()

	def __init__(self):
		self.type = 'model'
		self.id = None
		pass

	@classmethod
	def _get_by_id(cls, id, manager=None):
		if not manager:
			manager = cls._manager
		raw =  manager.get_object(id)
		try:
			obj = Model()
			obj.decode(raw[0][0])
			return obj
		except IndexError:
			raise VoldKeyNotFound("Couldn't find Voldemort key %s" % id)

	@classmethod
	def get_by_id(cls, ids=None):
		if isinstance(ids, list):
			objs = [cls._get_by_id(id) for id in ids]
			return objs
		else:
			obj = cls._get_by_id(ids)
			return obj

	@classmethod
	def _delete_by_id(cls, id, manager=None):
		if not manager:
			manager = cls._manager
		return manager.delete(id)

	@classmethod
	def delete_by_id(cls, ids):
		if isinstance(ids, list):
			results = [cls._delete_by_id(id) for id in ids]
			return results
		else:
			return cls._delete_by_id(ids)

	@classmethod
	def all(cls, limit=None):
		#doesn't actually work
		#might eventually let people decide a max number of results they want
		return cls.manager.all()

	def delete(self):
		return self._delete_by_id(self.id)

	def put(self):
		#Should save the object, if the object doesn't have an ID yet, create one
		if not self.id: self.generate_id()
		self._manager.store.put(self.id, self.encode())
		return self.id

	def generate_id(self):
		from random import randint
		rand = randint(1000000000000, 9999999999999)
		self.id = "MOD-%s" % rand

	def decode(self, raw):
		#Decodes the pickled dict
		import base64
		import pickle
		decoded = base64.decodestring(raw)
		attrs = pickle.loads(decoded)
		for k, v in attrs.items():
			self.__dict__[k] = v
		#take the keys and make them self attributes
		#would be nice if we could take any items that are ID's and put the corresponding models in their place
		return attrs

	def encode(self):
		import base64
		import pickle
		attrs = {}
		for k, v in self.__dict__.items():
			if k == 'conn': continue
			attrs[k] = v
		#take all the self attrs and make them key/value pairs in the dict
		pic = pickle.dumps(attrs)
		encoded = base64.encodestring(pic)
		return encoded

	def to_json(self):
		import json
		return json.dumps(self.__dict__)

	def pretty_print(self):
		ret = "Object %s" % self.id
		for k, v in self.__dict__.items():
			ret = ret + '\n%s :\t%s' % (k, v)
		return ret
