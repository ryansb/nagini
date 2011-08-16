#!/usr/bin/python

# Copyright (c) 2011 Ryan Brown
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from setuptools import setup, find_packages

from nagini import __version__

setup(name = "nagini",
		version = __version__,
		description = "Abstraction of objects in a Voldemort database (though could be adapted for similar db types)",
		long_description="Nagini is an abstraction of key/value pairs that allows you to give them list attributes, store entire objects, etc",
		author = "Ryan Brown",
		author_email = "ryansb@csh.rit.edu",
		url = "https://",
		packages = find_packages(),
		include_package_data = True,
		package_data = {
			'': ['*.yaml', 'conf/*'],
		},
		scripts = [],
		license = 'NONE',
		platforms = 'Posix',
		classifiers = [ 'Development Status :: 3 - Alpha',
			'Intended Audience :: Developers',
			'License :: OSI Approved :: MIT License',
			'Operating System :: OS Independent',
			'Topic :: Internet',
		],
		dependency_links = [
		],
		install_requires = [
		],
	)
