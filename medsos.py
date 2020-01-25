import paramiko
import  time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.168.26.1', port=22, username='admin', password='')

print('Berhasil Login \n')

stdin, stdout, stderr = ssh_client.exec_command('ip firewall layer7-protocol add name=https regexp=("facebook.com|youtube.com|detik.com|instagram.com|kompas.com")')
stdin, stdout, stderr = ssh_client.exec_command('ip firewall filter add chain=forward protocol=tcp layer7-protocol=https action=drop')
time.sleep(1)

stdin, stdout, stderr = ssh_client.exec_command('ip firewall layer7-protocol print')
stdin, stdout, stderr = ssh_client.exec_command('ip firewall filter print')

output = stdout.readlines()

print('\n'.join(output))

ssh_client.close()
