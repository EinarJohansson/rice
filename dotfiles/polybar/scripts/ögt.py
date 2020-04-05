import requests
from datetime import datetime

URL = '''https://rest.ostgotatrafiken.se/journey/Find?
startId=1062&
endId=3&
startType=stop&
endType=stop&
startLl=58.608141%2C16.244183&
endLl=58.585197%2C16.189671&
startName=Hyttgatan&
endName=S%C3%B6der+Tull&
date=&
time=&
direction=0&
span=default&
traffictypes=0&
changetime=0&
priority=0&
walk=false
'''.replace('\n', '')

<<<<<<< HEAD
def get(URL):
    try:
        r = requests.get(url = URL)
        data = r.json() 
    except:
        return 'Refresh'
    nu = datetime.now().time()

    for avgång in data['Journeys']:
        tid = avgång['Departure']
        tid = datetime.strptime(tid[-8:], '%H:%M:%S').time()

        if tid > nu:
            return str(tid)[:-3]

if __name__ == '__main__':
    print(get(URL))
=======
try:
    r = requests.get(url = URL)
    data = r.json() 
except:
    print('Error')
    exit()

nu = datetime.now().time()

for avgång in data['Journeys']:
    tid = avgång['Departure']
    tid = datetime.strptime(tid[-8:], '%H:%M:%S').time()

    if tid > nu:
        print(str(tid)[:-3])
        exit()
>>>>>>> 3b34b6b52b435d1df3ca7fd78ef6342eb44ff1d5
