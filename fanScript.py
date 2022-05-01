from paramiko import SSHClient
import time

host = "Your_IP"
port = 22
username = "root"
password = "Password"
speed = 10

client = SSHClient()
client.load_host_keys('Your_Host_Keys_Location')

client.connect(host, username = username, password = password)
for x in range(8):
    
    client.exec_command("fan p "+str(x)+" max "+str(speed))
    print("Fan "+str(x+1)+" set!")
    time.sleep(1)

client.close()
