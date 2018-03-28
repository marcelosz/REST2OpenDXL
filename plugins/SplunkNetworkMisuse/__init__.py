#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Marcelo Souza"
__license__ = "GPL"

import cherrypy

@cherrypy.expose
class SplunkNetworkMisuse(object):

    @cherrypy.tools.accept(media='text/plain')

    def POST(self, length=8):
        print("Request Headers: ", cherrypy.request.headers)
        #body = cherrypy.request.body.read()
        print("Request Body: ", cherrypy.request.body.read())
        return "OK"
        
def init():
  conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'request.method_with_bodies': True,
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
  }
  cherrypy.tree.mount(SplunkNetworkMisuse(), '/webhooks/splunk/network-misuse', conf)