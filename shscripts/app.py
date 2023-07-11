from flask import Flask, redirect, render_template, request, session, url_for, Response
from werkzeug.serving import run_simple
from jwcrypto import jwt, jwk
import json
import platform
import time
import subprocess
import os 
import sys

app = Flask(__name__, static_url_path='')


def retrieveAndPrintToken():
    ##Creating the file location
    snapDataFolder=os.environ['SNAP_DATA']
    snapName=os.environ['SNAP_INSTANCE_NAME']
    TokenFIle=snapDataFolder+'/service-token/'+snapName+'/'+snapName+'.token'
    app = Flask(__name__, static_url_path='')
    string="My token is here: "+TokenFIle + '\n\n'
    
    #read file
    f = open(TokenFIle, "r")
    myfile=f.read()
    string=string+'it contains:\n'+myfile+'\n\n'
    
    
    #decoding JWT
    ET = jwt.JWT(jwt=myfile, expected_type="JWT")
    
    string=string+'with the following informations:\n'+str(ET)
    return string

print(retrieveAndPrintToken())

########## serving functions

@app.route('/servicetoservicedemo')
def token():
   
    return retrieveAndPrintToken()
    #return app.send_static_file('index.html')


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 9876, app)