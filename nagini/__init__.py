#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Nagini
__version__ = 0.0
DB_SERVERS = [("127.0.0.1", 6666)]
MESSAGE_STORE = "test"
CONFIG_LOCATION = '/home/ryansb/code/cshns/cshns/conf/db.yaml'

def read_config():
	import os
	import yaml
	"""Read the config file stored in the location defined in nagini/__init__"""
	config_path = os.path.abspath(__file__)
	config_path.replace('__init__.py', 'keys.txt')
	with open(CONFIG_LOCATION, 'rb') as config:

		config_values = yaml.load(config.read())
		config.close()
		return config_values

