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
