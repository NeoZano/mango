from http.server import BaseHTTPRequestHandler
from lib.file_to_show import show_page
from http.server import HTTPServer
from urls import urls_list

class server(BaseHTTPRequestHandler):
  def version_string(request):
    return("Norse 0.0.1")
  def log_message(self, format, *args):
        return
  def do_GET(self):
        
        self.send_response(200)

        for url in urls_list:
            if url[0] == self.path:
                  http_response = url[1](self)
             
            else:
                file = show_page(self.path)
                http_response = file[0]
                self.send_header('Content-type',file[1])


        self.end_headers()
        self.wfile.write(bytes(http_response, "utf8"))
        return

def run_server(ip='127.0.0.1',port=8080):
  print("\n-- Norse version 0.1 Alpha --\n\n")
  print('Starting server on ip '+ip+' and port '+str(port) + " ...")
  server_address = (ip, port)
  httpd = HTTPServer(server_address, server)
  print('Server is now running ...\n\n')
  httpd.serve_forever()