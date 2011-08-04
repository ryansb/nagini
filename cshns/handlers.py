#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: The botoweb handlers for both simple client and the server interface
import cshns
import base64
import logging
from cshns.auth import DummyAuthorizer
from botoweb.exceptions import Unauthorized
from botoweb.appserver.handlers import RequestHandler

log = logging.getLogger("CSHNS")


class CSHNSServer(RequestHandler):
	"""
	The server interface, for submitting messages to and administering queues,
	as well as getting information about available queues
	"""
	allowed_methods = ['head', 'get', 'put', 'post', 'options']
	def __init__(cls, env, config):
		RequestHandler.__init__(cls, env, config)
		cls.log = logging.getLogger("CSHNS-Server")
		cls.queue = None
		cls.auth = DummyAuthorizer()

	def __call__(cls, request, response, obj_id=None):
		"""Override this to require an authentication token
		to be sent.
		Etag: hmac-sha256 of the request body and secret auth-token

		This is a custom authentication method, not really a user
		at all, just for clients to authenticate themselves
		with us.
		"""
		auth_token = request.headers.get("Etag")
		if auth_token:
			if not cls.validate(auth_token, request.body):
				raise Unauthorized("You are not authorized to access this service")
		elif request.headers.get("Authorization"):
			auth_token = request.headers.get("Authorization")
			if not cls.validate(auth_token, request.body):
				raise Unauthorized("You are not authorized to access this service")
		else:
			raise Unauthorized("You must provide either an Etag signature or basic authentication")
		return RequestHandler.__call__(cls, request, response, obj_id)

	def validate(cls, auth_token, body):
		"""Validate this request"""
		return True
		if auth_token.startswith("HMAC"):
			uname = base64.decodestring(auth_token.split(' ')[1])
			passwd = auth_token.split(' ')[2]
			cls.user = cshns.auth.User.get_by_name(uname)
			if cls.auth.authorize(cls.user, passwd):
				cls.log.info('Authentication successful for %s' % uname)
				return True
			cls.log.info('Authentication failed for %s' % uname)
			return False

	def _head(cls, request, response, id=None):
		"""Do shit"""
		response.status = 200
		response.body = "OK"
		return response

	def _get(cls, request, response, id=None):
		"""Do shit"""
		response.status = 200
		response.body = "OK"
		return response

	def _put(cls, request, response, id=None):
		"""Do shit"""
		response.status = 200
		response.body = "OK"
		return response

	def _post(cls, request, response, id=None):
		"""Do shit"""
		response.status = 200
		response.body = "OK"
		return response

	def _options(cls, request, response, id=None):
		"""Do shit"""
		response.status = 200
		response.body = "OK"
		return response


class SimpleClient(RequestHandler):
	"""
	A simple CSHNS client intended for testing and example purposes only
	"""
	allowed_methods = ['head', 'get', 'put', 'post']
	def __init__(cls, env, config):
		RequestHandler.__init__(cls, env, config)
		cls.log = logging.getLogger("CSHNS-Client")

	def _head(cls, request, response, id=None):
		"""Do shit"""
		cls.log.info("Received HEAD request %s" % request)
		response.status = 200
		response.body = "OK"
		return response

	def _get(cls, request, response, id=None):
		"""Do shit"""
		cls.log.info("Received GET request %s" % request)
		response.status = 200
		response.body = "OK"
		return response

	def _put(cls, request, response, id=None):
		"""Do shit"""
		cls.log.info("Received PUT request %s" % request)
		response.status = 200
		response.body = "OK"
		return response

	def _post(cls, request, response, id=None):
		"""Do shit"""
		cls.log.info("Received POST request %s" % request)
		response.status = 200
		response.body = "OK"
		return response

