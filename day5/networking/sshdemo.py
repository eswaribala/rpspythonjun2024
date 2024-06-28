import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('test.rebex.net', username='demo', password='password')
except paramiko.SSHException:
    print("Connection Failed")
    quit()

stdin, stdout, stderr = ssh.exec_command("cd aspnet_client")
print(stderr)
stdin, stdout, stderr = ssh.exec_command("pwd")
print(stderr)
for line in stdout.readlines():
    print(line.strip())
ssh.close()