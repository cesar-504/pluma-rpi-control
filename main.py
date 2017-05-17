import json

#urlbase='pluma-api.herokuapp.com'
urlBase='localhost:8000'
urlAccess=urlBase + '/api/entries/access'
urlExit=urlBase + '/api/entries/exit'

print(urlBase)
print(urlAccess)
print(urlExit)

jsonAccess=json.dumps(
    {
        'idEntry':1,
        'idUser':1,
        'action':'access'
    }, indent=4
)

jsonExit = json.dumps(
    {
        'idEntry':1,
        'idUser':1,
        'action':'exit'
    }, indent=4
)

print(jsonAccess)
print(jsonExit)

s = '''
    {
        "idEntry":1,
        "auth":true,
       "userId":1,
        "ioId":1,
        "error":""
    }
'''
replyJson = json.loads(s)
print(replyJson)
