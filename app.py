# -*- coding: utf-8 -*-
""" tornado の勉強	
"""
import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

if __name__ == '__main__':
	app = tornado.web.Application([
		(r"/", MainHandler),
	],
	template_path = os.path.join(os.getcwd(), "templates"),
	static_path = os.path.join(os.getcwd(), "static"),
	)
	app.listen(8888)
	print("app run!!")
	tornado.ioloop.IOLoop.instance().start()
