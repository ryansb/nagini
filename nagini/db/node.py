#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: The nodes for the table that tracks contents of the database

from nagini.db.model import Model

class Node(Model):
	def __init__(self, parent):
		self.parent = parent

	def add_entry(self, ref):
		self._ref.append(ref)


class HeadNode(Node):
	def __init__(self, parent):
		self.nref = {} #References to other nodes, stored as {'prefix': node_id}
		Node.__init__(self, parent)

	def add_node():
		pass


class SubNode(Node):
	def __init__(self, parent):
		self.oref = [] #References to objects, stored as str(id)
		Node.__init__(self, parent)
