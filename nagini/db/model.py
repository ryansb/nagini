#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Model object, base for other DB objects like User and Message

from nagini.db import get_manager
from nagini.db.property import ReferenceProperty

class VoldKeyNotFound(Exception):
	def __init__(self, message):
		Exception.__init__(self, message)

class Model(object):
	_manager = get_manager()

	def __init__(self):
		self.id = None
		pass

	@classmethod
	def _get_by_id(cls, id, manager=None):
		import json
		import base64
		if not manager:
			manager = cls._manager
		try:
			raw = manager.get_object(id)[0][0]
			decoded = base64.decodestring(raw)
			raw_dict = json.loads(decoded)
			print raw_dict
			fqn = raw_dict['class'] #Fully Qualified Name of the class
			print fqn
			exec("from %s import %s" % ('.'.join(fqn.split('.')[:-1]), fqn.split('.')[-1:][0]))
			exec("obj = %s()" % fqn.split('.')[-1:][0])
			obj.decode(raw_dict['blob'])
			return obj
		except IndexError:
			raise VoldKeyNotFound("Couldn't find Voldemort key %s" % id)

	@classmethod
	def get_by_id(cls, ids=None):
		"""Return an object of the Model attached to the given ID

		Takes ID's either as a single strng or list of strings

		Returns a Model object or a list of model objects, depending on the
		input"""
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
		"""Delete "n object by its ID"""
		if isinstance(ids, list):
			results = [cls._delete_by_id(id) for id in ids]
			return results
		else:
			return cls._delete_by_id(ids)

	@classmethod
	def all(cls, limit=None):
		"""Return an iterable of all keys in the database"""
		#doesn't actually work
		#might eventually let people decide a max number of results they want
		return cls.manager.all()

	def delete(self):
		"""Delete this object immediately from the data store"""
		return self._delete_by_id(self.id)

	def put(self):
		"""Saves a Model object with all its attributes. If the Model has been
		altered it keeps its ID, but if the object doesn't yet have an ID it
		generates one for itself.

		Returns the ID of the story after it is saves"""
		if not self.id: self.generate_id()
		self._manager.store.put(self.id, self.encode())
		return self.id

	def generate_id(self):
		"""Generates a unique identifier to call the object up by later"""
		import uuid
		self.id = "%s-%s" % (self.__class__.__name__[:5].upper(), str(uuid.uuid4()))

	def decode(self, raw):
		"""Decodes the pickled Model object.

		Returns a dictionary of the attributes that were encoding"""
		import pickle
		attrs = pickle.loads(raw)
		for k, v in attrs.items():
			if isinstance(v, ReferenceProperty):
				self.__dict__[k] = v.decode()
			else:
				self.__dict__[k] = v
		#take the keys and make them self attributes
		#would be nice if we could take any items that are ID's and put the corresponding models in their place
		return attrs

	def encode(self):
		"""Put the entire Model into a base-64 encoded pickled version to be stored in Voldemort."""
		import json
		import base64
		import pickle
		classname = repr(self.__class__).split("'")[1]
		attrs = {}
		for k, v in self.__dict__.items():
			if issubclass(v.__class__, Model):
				attrs[k] = ReferenceProperty(v.id, v.__class__.__name__)
			else:
				attrs[k] = v
		#take all the self attrs and make them key/value pairs in the dict

		pic = pickle.dumps(attrs)
		json = json.dumps({'class': classname, 'blob': pic})
		encoded = base64.encodestring(json)
		return encoded

	def to_json(self):
		"""Dump the entire Model object into a JSON blob"""
		import json
		return json.dumps(self.__dict__)

	def pretty_print(self):
		"""Return a kinda nice-looking string version of the Model"""
		ret = "%s %s" % (self.__class__.__name__, self.id)
		for k, v in self.__dict__.items():
			ret = ret + '\n%s :\t%s' % (k, v)
		return ret
