#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: The nodes for the table that tracks contents of the database

from nagini.db.model import Model

MAX_ITEMS = 255

class Node(Model):
	def __init__(self, parent):
		self.parent = parent

	def add_entry(self, ref):
		raise NotImplemented('Reference addition not implemented for this type')

	def add_node(self, prefix, uid):
		raise NotImplemented('Node addition not implemented for this type')


class HeadNode(Node):
	def __init__(self, parent):
		if self.parent == None:
			self.nref = {} #References to other nodes, stored as {'prefix': node_id}
		else:
			self.nref = []
		Node.__init__(self, parent)

	def add_node(self, prefix, uid):
		if self.parent is not None:
			self.nref[prefix] = uid
			return True
		if len(self.nref) >= MAX_ITEMS:
			self.nref.append(uid)
		else:
			pass
		return True


class SubNode(Node):
	def __init__(self, parent):
		self.oref = [] #References to objects, stored as str(id)
		self.nref = [] #list of ids of child nodes
		Node.__init__(self, parent)

	def add_node(self, uid):
		pass

	def add_entry(self, uid):
		pass
