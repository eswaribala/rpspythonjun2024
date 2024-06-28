import sys
import chilkat

ssh = chilkat.CkSsh()

#  Connect to an SSH server:
success = ssh.Connect("192.168.1.209",22)
if (success != True):
    print(ssh.lastErrorText())
    sys.exit()

#  Am I connected?
connected = ssh.get_IsConnected()
print("connected = " + str(connected))

#  Disconnect.
ssh.Disconnect()

#  Am I still connected?
connected = ssh.get_IsConnected()
print("connected = " + str(connected))