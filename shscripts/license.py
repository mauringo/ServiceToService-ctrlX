import sys
import os
import requests
os.environ['NO_PROXY'] = '127.0.0.1' 
mytokenfile=os.environ['SNAP_DATA']+"/service-token/servicetoservicedemo/servicetoservicedemo.token"
mylicense="SWL_XCR_ENGINEERING_4H"
myfilename='licensed'

def checkLicense(license,filename, tokenfile):
    f = open(mytokenfile, "r")
    mytoken=f.readline()
    f.close()
   
    headers={
    "Accept" : "application/json",
    "Content-Type":"application/json",
    "Authorization": "Bearer "+mytoken
    }
    #print(headers) 
    url = 'https://127.0.0.1/license-manager/api/v1/license'
    myobj = {
      "name": mylicense,
      "version": "1.0"
    }
    x = requests.post(url, json = myobj,headers=headers, verify=False)
    #print(x)
    
    if x.status_code == 200:
        print(x.json()['id'])
        file = open(filename, 'w')
        file.write(x.json()['id'])
        file.close()
        #print(x.json())
        print('license released')

#To be done with real and cirtual core license
checkLicense(mylicense,myfilename,mytokenfile)