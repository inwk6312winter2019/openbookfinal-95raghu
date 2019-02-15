from apicem import *
import requests
import json
  def get_net_device_count():

device = []
try:
    
    resp = get(api="network-device")
    status = resp.status_code
    response_json = resp.json()
    device = response_json["response"]

    
except:
    print ("Something wrong, cannot get network device information")
    sys.exit()

if status != 200:
    print (resp.text)
    sys.exit()

if device == [] :  
    print ("No network device found !")
    sys.exit()

device_list = []
i=0
for item in device:
    i+=1
    device_list.append([i,item["hostname"],item["managementIpAddress"],item["type"],item["instanceUuid"]])

print (tabulate(device_list, headers=['number','hostname','ip','type'],tablefmt="rst"))

get_net_device_count()
