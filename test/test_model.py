#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: quick model test
from nagini.db.model import Model
m = Model.get_by_id('firstval')
n = Model()
n.testing = 'this is a test'
n.furniture = ['couch', 'recliner']
n.put()

#Queue test
from nagini.db.user import User
u = User()
