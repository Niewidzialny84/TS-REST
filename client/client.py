import requests
import time

serviceAddress="http://192.168.1.100:5000/"

print("Ayaya:")
time.sleep(0.5)
myget = requests.get(serviceAddress+'')
print(myget.text)

print("4) Adding account for newAdvertiser campaign2:")
time.sleep(0.5)
mypost = requests.post(serviceAddress+'accounts', json={"accountName":"newAdvertiser:campaign2"})
print(mypost.text)

print("7) Deleting account for baner2 of newAdvertiser campaign2:")
time.sleep(0.5)
mydelete = requests.delete(serviceAddress+'accounts/newAdvertiser:campaign2/close')
print(mydelete.text)

print("11) Setting budget for newAdvertiser:")
time.sleep(0.5)
myput = requests.put(serviceAddress+'accounts/newAdvertiser/budget', json={"USD/1M":1000})
print(myput.text)
