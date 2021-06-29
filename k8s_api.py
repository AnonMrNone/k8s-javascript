#!/usr/bin/python3
import cgi
import subprocess
print("Content-Type: text/html\n\n")
field = cgi.FieldStorage()
query = field.getvalue('q')
kubeconf = '--kubeconfig /usr/share/httpd/kubeconfig_mks_91.yaml'
#launch create run pod/deployment
if ('launch' in query) or ('create' in query) or ('run' in query):
    #pod
    if 'pod' in query:
        subq = query.split(" ")
        img = subq[-1]
        name = subq[-2]
        output = subprocess.getoutput("kubectl {0} run {1} --image={2}".format(kubeconf,name,img))
        print(output)    
    elif 'deployment' in query:      
        subq = query.split(" ")
        img = subq[-1]
        name = subq[-2]
        output = subprocess.getoutput("kubectl {0} create deployment {1} --image={2}".format(kubeconf,name,img))            
        print(output)
elif ('expose' in query):
    subq = query.split(" ")
    name = subq[-3]
    extype = subq[-2]
    port = int(subq[-1])
    output = subprocess.getoutput("kubectl {0} expose deployment {1} --type={2} --port={3}".format(kubeconf,name,extype,port))
    print(output)
elif ('scale' in query):
    subq = query.split(" ")
    resou = subq[-3]
    name = subq[-2]
    repno = int(subq[-1])
    output = subprocess.getoutput("kubectl {0} scale {1} {2} --replicas={3}".format(kubeconf,resou,name,repno))
    print(output)
elif ("clean all" in query):
    output = subprocess.getoutput("kubectl {0} delete --all all".format(kubeconf))
    print(output)
elif ("delete" in query):
    subq = query.split(" ")
    resou = subq[-2]
    name = subq[-1]
    output = subprocess.getoutput("kubectl {0} delete {1} {2}".format(kubeconf,resou,name))
    print(output)
elif ("get all" in query):
    output = subprocess.getouput("kubectl {0} get all".format(kubeconf))
    print(output)
else:
    print("Cannot process, come back later or view supported elements")

