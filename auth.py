import config
import requests
_jwt=""

def login(email,passw):  
    j ={
        'email':email,
        'password':passw, 
    }
    r = requests.post(config.urlLogin,json=j)
    if r.status_code == requests.codes.ok:
        print('login exitoso')
        _jwt = r.json()['jwt']
        return True
    elif r.status_code == 403 or r.status_code == 401 :
        print('error al iniciar sesión, intente de nuevo.')
    else:
        print('error '+ str(r.status_code))
    return False
             
def logout():
    _jwt=""
def jwt():
    return _jwt
def authStr():
    'Bearer ' + _jwt
