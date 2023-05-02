import os

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 9000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        with open(os.getcwd()+"\\site\\index.html") as index_html:
         message = "Hello, World! Here is a GET response"
         print(os.getcwd()+"\\site\\index.html")
         # print(index_html.read())
         self.wfile.write(bytes(index_html.read(), "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

if __name__ == "__main__":
    webServer = HTTPServer((HOST, PORT), MyServer)
    print("Server started http://%s:%s" % (HOST, PORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")