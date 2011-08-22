#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Contains database-related objects including the Model, User, and Message objects
from nagini import read_config
from nagini.db.manager import DarkMaster

def get_manager():
	"""Creates and returns an instance of DarkMaster (connection manager)
	"""
	config_values = read_config()
	db_user = config_values['db_user']
	db_passwd = config_values['db_passwd']
	db_store = config_values['db_store']
	db_hosts = config_values['db_hosts']
	return DarkMaster(db_user, db_passwd, db_store, db_hosts)
