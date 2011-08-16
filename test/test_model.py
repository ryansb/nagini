#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: 
from nagini.db.model import Model
from voldemort import StoreClient
c = StoreClient('test', [('127.0.0.1', 6666)])
m = Model(c)
m.get_by_id('firstval')


#quick model test
from nagini.db.model import Model; m = Model.get_by_id('firstval')
n = Model()
n.testing = 'this is a test'
n.furniture = ['couch', 'recliner']
n.put()

#Queue test
from nagini.db.user import User
u = User()
