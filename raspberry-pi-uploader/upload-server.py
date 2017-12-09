#!/usr/bin/python3
from bottle import get, post, request, run
from subprocess import call

@get('/')
def index():
    return "<html><body><h1>Upload Server</h1><form method=\"post\"><textarea name=\"content\" cols=\"50\" rows=\"30\"></textarea><input type=\"submit\" name=\"Odeslat\" /></form></body></html>"

@post('/')
def save():
    filename = '/home/pi/krouzek-zs-volyne/script.py'
    content = request.forms.get('content')
    if content:
        with open(filename, 'w') as f:
            f.write(str(content))
            f.write('\n')
        call(['/usr/bin/python3', filename])
    return "<html><meta http-equiv=\"refresh\" content=\"3;url=.\"><body><h1>Ok</h1></body></html>"

run(host='0.0.0.0', port=3000, debug=True)
