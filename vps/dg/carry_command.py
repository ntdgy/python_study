import http.server
import subprocess
import send
import socket
import datetime

class HTTPServerV6(http.server.HTTPServer):
    address_family = socket.AF_INET6

host = ('::', 8889)
Token = '0400d4fb-0ac6-4e1b-b045-1cd188e4d45b'

class RequestHandlerImpl(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == '/0400d4fb-0ac6-4e1b-b045-1cd188e4d45b/send'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            subprocess.call('/usr/bin/python3 /root/bandwidth/send.py', shell=True)
            message = message + '\n' + 'send Susseccfully'
            send.sendMessage(message)
            self.wfile.write(b'Success')
            return
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
            return

    def do_POST(self):
        if(self.path == '/0400d4fb-0ac6-4e1b-b045-1cd188e4d45b/send'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            subprocess.call('/usr/bin/python3 /root/bandwidth/send.py', shell=True)
            message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = message + '\n' + 'send Susseccfully'
            send.sendMessage(message)
            self.wfile.write(b'Success')
            return
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
            return

httpd = HTTPServerV6(host, RequestHandlerImpl)
httpd.serve_forever()