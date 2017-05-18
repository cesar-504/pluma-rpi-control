import json
import config
import  requests
import auth
r = requests.get(config.urlBase+'/api/users')
print(config.urlBase)
print(config.urlAccess)
print(config.urlExit)

login=False
print('Login:')
while(not login):
    email=input('email: ')
    password =input('contraseña: ')
    login=auth.login(email,password)




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
