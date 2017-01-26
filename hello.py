#!/usr/bin/env python
# this thing is called the "shebang"
import os, json, cgi, Cookie

form = cgi.FieldStorage()
username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ["HTTP_COOKIE"])

print "Content-Type: text/html"
if username == "michaelyeg" and password == "michaelyeg":
    print "Set-Cookie: loggedin=true"

# Need a blank line between header and content
print
print "<HTML><BODY>"
print "<H1>Hello World</H1>"
# Try http://localhost:8000/hello.py?military_id=1234567 in your browser
print "Your military ID is:"
print form.getvalue('military_id')
print "<P>Your Browser is"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
    print "Firefox!"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
    print "Chrome!"
else:
    print os.environ['HTTP_USER_AGENT']
print "<FORM method= 'POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

if "loggedin" in C:
    print "<P>Logged in: " + str(C['loggedin'].value)
else:
    print "<P>No cookie"

#print json.dumps(dict(os.environ), indent=2, sort_keys=True)