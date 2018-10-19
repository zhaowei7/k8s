#!/usr/bin/env python
#encoding=utf8
import sys
from jinja2 import Template
 
#template
def RenderTemplate(name="",version="",replicas_num="",namespace=""):
    if namespace == "dev":
        with open('/srv/example/jenkins-jinjia/temp-deployment/template', "r") as f:
            print(Template(f.read()).render(name=name,version=version,replicas_num=replicas_num,namespace=namespace))
 
#value
d = {}
jenkinsfile="/tmp/{0}jenkins".format(sys.argv[1])
with open(jenkinsfile,'r') as f:
    for line in f:
        (k,v) = line.split(':')
        if k == '':
            d[str(k)] = ""
        else:
            d[str(k)] = v.replace('\n','')
 
RenderTemplate(**d)
