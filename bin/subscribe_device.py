#!/usr/bin/env python
# -*- coding; utf-8 -*-
# Author: Ryan Brown
# Description: Subscribes your device to a CSHNS server you specify

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-u", "--user", help="Your username", dest="username", default=None)
parser.add_option("-p", "--password", help="Your password", dest="password", default=None)
parser.add_option("-s", "--server", help="The url of the CSHNS server you're trying to subscribe to", dest="server", default=None)
parser.add_option("-q", "--queue", help="Identifier of the queue you're subscribing to", dest="queue", default=None)

(options, args) = parser.parse_args()
passwd = options.password
uname = options.username
server = options.server
queue = options.queue

if not (passwd and uname and server and queue ): exit()
