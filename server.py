import SimpleHTTPServer
import SocketServer

# https://docs.python.org/2/library/simplehttpserver.html

PORT = 9001

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()