from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

PORT = 8000

with TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server berjalan di http://localhost:{PORT}")
    httpd.serve_forever()
