from http.server import HTTPServer, SimpleHTTPRequestHandler

from config.configuration import API_IP, API_PORT

# TODO expand
Handler = SimpleHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=Handler):
    server_address = (API_IP, API_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
