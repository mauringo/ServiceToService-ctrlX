import sys
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mytokenfile=os.environ['SNAP_DATA']+"/service-token/servicetoservicedemo/servicetoservicedemo.token"
mylicense="SWL_XCR_ENGINEERING_4H"
mylicensefile="licensed"

f = open(mytokenfile, "r")
mytoken=f.readline()
f.close()
#print(mytoken) 

if (os.path.isfile(mylicensefile)):
    
    idf = open(mylicensefile, "r")
    myid=idf.readline()
    idf.close()
    import requests
    os.environ['NO_PROXY'] = '127.0.0.1' 
    
    headers={
    "Accept" : "application/json",
    "Content-Type":"application/json",
    "Authorization": "Bearer "+mytoken
    }
    #print(headers) 
    url = 'https://127.0.0.1/license-manager/api/v1/license/'+myid
    print(url)
    x = requests.delete(url,headers=headers, verify=False)
    print(x)
    if x.status_code == 204:
        os.remove(mylicensefile)
        print('license removed')
    