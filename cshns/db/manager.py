#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: The manager for the database connection
from voldemort import StoreClient

class DarkMaster(object):
	def __init__(self, db_user, db_passwd, db_store, db_hosts):
		"""Description: Init method for the database connection manager
			:param db_user: The username for the database
			:type str:

			:param db_passwd: Password
			:type str:

			:param db_store: The name of the store you need to connect to
			:type str:

			:param db_hosts: A list of db hosts and the ports they run the database on
			:type list: List of host/port tuples like this:
				[('127.0.0.1', '6666'), ('192.168.100.105', '6666')]
			"""
		self.db_user = db_user
		self.db_passwd = db_passwd
		self.db_store = db_store
		self.db_hosts = db_hosts
		self._store = None


	@property
	def store(self):
		if self._store is None:
			self._connect()
		return self._store

	def _connect(self):
		args = (self.db_store, self.db_hosts)
		self._store = StoreClient(args)

	def get_object(self, id):
		return self.store.get(id)[0][0]
