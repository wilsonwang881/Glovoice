import httplib

conn = httplib.HTTPConnection("52.89.41.142:8080")

conn.request("POST","/login")

res = conn.getresponse()

print res.status, res.reason, res.read()

conn.request("POST","/logout")

res = conn.getresponse()

print res.status, res.reason, res.read()

conn.request("POST","/SQL")

res = conn.getresponse()

print res.status, res.reason, res.read()

