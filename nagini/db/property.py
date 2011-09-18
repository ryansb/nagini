#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Property class. Model (and its subclasses) have properties

def prep_password(passwd):
	import hashlib
	return hashlib.sha512(passwd).hexdigest()

class Property(object):
	def __init__(self, verbose_name='', name='', default='', required=False, validator=None, choices=None):
		self.verbose_name = verbose_name
		self.name = name
		self.default = default
		self.required = required
		self.validator = validator
		self.choices = choices


class PasswordProperty(Property):
	def __init__(self, plaintext, verbose_name='', name='', default='', required=False, validator=None, choices=None):
		self._passwd = prep_password(plaintext)
		Property.__init__(self, verbose_name, name, default, required, validator, choices)

	def __eq__(self, obj):
		if self._passwd == prep_password(obj):
			return True
		return False

	def __str__(self):
		return self._passwd

	def __set__(self, obj, value):
		print 'val', value, type(value)
		print 'obj', obj, type(obj)
		obj.value = 'tits'
		return 'lslsls'
		if isinstance(value, str):
			self._passwd = prep_password(value)
		else:
			Property.__set__(self, obj, value)


class ReferenceProperty(Property):
	"""When this property is updated it actually updates an attribute of another
	object
	For example, you have a Queue and a User and a User has an associated_queues
	attribute, you would instantiate Queue with a ReferenceProperty attribute
	such that it automatically put its own id into the associated_queues
	attribute of the user"""
	def __init__(self, reference_id, reference_class):
		self.id = id
		self.reference_class = reference_class


class ReverseReferenceProperty(Property):
	"""This acts like a pointer in that when a Model has a reverse reference
	property it acts as though that whole Model is an attribute of the object
	that has the ReverseReferenceProperty
	For example, if you have a Message with a queue attribute the specified
	Queue in the database, and when decoding the Message the Queue would
	automatically be fetched and stuffed in the queue attribute.
	Note: this probably will cause a decent-sized performance hit"""
	def __init__(self, id):
		self.id = id


	def decode(self):
		#Grab the model and decode it, returning the reassembled Model instance
		from nagini.db.model import Model
		return Model.get_by_id(self.id)
