#!/usr/bin/env python3

from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8888

server_address = ('', PORT)
httpd = HTTPServer(server_address,SimpleHTTPRequestHandler)
httpd.serve_forever()

