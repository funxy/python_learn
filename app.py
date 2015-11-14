# -*- coding: utf-8 -*-
""" tornado の勉強	
"""

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello world")

application = tornado.web.Application([
	(r"/", MainHandler),
])

if __name__ == '__main__':
	print("app run!!")
	application.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
