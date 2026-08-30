from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        if code == 404:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("404.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            super().send_error(code, message, explain)

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), CustomHandler)
    print("Serving on port 8000...")
    server.serve_forever()
