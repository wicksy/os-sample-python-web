# Hello World using gunicorn WSGI HTTP server
#
def application(environ, start_response):
  data = b"Hello, World!\n"
  start_response("200 OK", [
    ("Content-Type", "text/plain"),
    ("Content-Length", str(len(data)))
  ])
  return iter([data])
