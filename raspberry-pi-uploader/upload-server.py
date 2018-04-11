#!/usr/bin/python3
from bottle import get, post, request, run
from subprocess import call

@get('/')
def index():
    return "<html><body><h1>Upload Server</h1><form method=\"post\"><textarea name=\"content\" cols=\"50\" rows=\"30\"></textarea><br /><input type\"password\" name=\"pass\" placeholder=\"Password\" autocomplete=\"off\" /><br /><input type=\"submit\" name=\"Odeslat\" /></form></body></html>"

@post('/')
def save():
    filename = '/home/pi/krouzek-zs-volyne/script.py'

    if request.forms.get('pass') != 'password':
        return "<html><meta http-equiv=\"refresh\" content=\"3;url=.\"><body><h1>Wrong password</h1></body></html>"

    content = request.forms.get('content')
    if content:
        with open(filename, 'w') as f:
            f.write(str(content))
            f.write('\n')
        call(['/usr/bin/python3', filename])
    return "<html><meta http-equiv=\"refresh\" content=\"3;url=.\"><body><h1>Ok</h1></body></html>"

run(host='0.0.0.0', port=3000, debug=True)
