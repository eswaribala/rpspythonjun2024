import os
myCmd = 'ls -la'
os.system(myCmd)
myCmd = os.popen('ls -la').read()
print(myCmd)

import subprocess
subprocess.call("ls")
#popen takes sequence of commands
p = subprocess.Popen(["echo", "Hi Valeo"], stdout=subprocess.PIPE)

print (p.communicate())

iplist=["127.0.0.1","8.8.8.8"]
for ip in iplist:
    p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)
    # the stdout=subprocess.PIPE will hide the output of the ping command
    p.wait()
    if p.poll():
        print (ip+" is down")
    else:
        print (ip+" is up")

result = []
process = subprocess.Popen('dir',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE )
for line in process.stdout:
    result.append(line)
errcode = process.returncode
for line in result:
    print(line)