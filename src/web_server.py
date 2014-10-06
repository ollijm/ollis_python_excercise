__author__ = 'olli'

import SimpleHTTPServer
import SocketServer
import validator

conf = None


class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Construct a server response.
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(self._html())
        return

    @staticmethod
    def _html():
        html = "<!DOCTYPE html><html><body><h1>Olli's Web Page Monitor</h1><ul>\n"

        for web_page in conf.web_pages:
            if validator.validate_web_page(web_page):
                status = "OK"
            else:
                status = "FAIL"
            html += "<li><strong>{0}</strong>: {1}</li>\n".format(status, web_page)
        html += "</ul></body></html>"
        return html


def start():
    server = SocketServer.TCPServer(('0.0.0.0', 8080), MyHandler)
    print "WEB SERVER STARTS NOW"
    server.serve_forever()