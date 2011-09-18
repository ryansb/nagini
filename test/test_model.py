#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: quick model test

import py.test
class TestNormalizer(object):
	def setup_class(self):
		"""Sets up defaults for all other tests, runs between each test function"""
		pass

	def test_get_model(self):
		from nagini.db.model import Model
		m = Model()
		m.furniture = ['couch', 'table', 'chair', 'cabinet']
		m.languages = {'python': 'whitespace', 'java': 'semicolon'}
		m.name = 'mahtestmodel'
		m.mahstuff = MahClass('aparam')
		m_id = m.put()
		n = m.get_by_id(m_id)
		assert m.furniture == n.furniture
		assert m.languages == n.languages
		assert m.name == n.name
		assert isinstance(m.mahstuff, MahClass)
		assert m.mahstuff.param == n.mahstuff.param
		assert n.mahstuff.param == 'aparam'
		n.delete()

	def test_get_user(self):
		from nagini.db.user import User
		from nagini.db.model import Model
		u = User('uname', 'testpass', 'longusername', devices=['mahserver', 'otherserver'])
		u_id = u.put()
		n = Model.get_by_id(u_id)
		assert u.name == n.name == 'uname'
		assert u.passwd == 'testpass'
		assert n.passwd == 'testpass'
		assert u.fullname == n.fullname == 'longusername'
		assert u.devices == n.devices == ['mahserver', 'otherserver']
		n.delete()

	def test_password_property(self):
		from nagini.db.property import PasswordProperty
		tpass = PasswordProperty('mahpassword')
		print str(tpass)
		assert tpass == 'mahpassword'
		assert not str(tpass) == 'mahpassword'
		assert not tpass == 'otherpassword'
		oldpass = tpass
		tpass = 'newpass'
		print tpass
		print oldpass
		assert 2==3

	def test_user_lookup(self):
		from nagini.db.query import Query
		q = Query('USER')
		u = q.next()
		assert u.name


class MahClass(object):
	def __init__(self, param):
		self.param = param
