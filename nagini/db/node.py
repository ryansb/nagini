#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: The nodes for the table that tracks contents of the database

from nagini.db.model import Model

MAX_ITEMS = 255

class Node(Model):
	def __init__(self, parent):
		self.parent = parent
		Model.__init__(self)

	def add_entry(self, ref):
		raise NotImplemented('Reference addition not implemented for this type')

	def add_node(self, prefix, uid):
		raise NotImplemented('Node addition not implemented for this type')


class HeadNode(Node):
	def __init__(self):
		self.nref = {} #References to other nodes, stored as {'prefix': node_id}
		Node.__init__(self)

	def add_node(self, prefix, uid):
		if self.parent is not None:
			self.nref[prefix] = uid
			return True
		if len(self.nref) >= MAX_ITEMS:
			self.nref.append(uid)
		else:
			pass
		return True


class RbNode(Node):
	def __init__(self, parent):
		self.objects = [] #References to objects, stored as str(id)
		self.children = []
		Node.__init__(self, parent)

	def add_node(self, uid):
		if len(self.children) < 2:
			self.children.append(uid)
		else:
			self.children[0].add_node(uid)

	def add_entry(self, uid):
		if len(self.objects) < MAX_ITEMS:
			self.objects.append(uid)
		elif len(self.children) > 0:
			self.children[0].add_entry(uid)
		else:
			nc = RbNode(self.id)
			nc_id = nc.put()
			self.children.append(nc_id)

