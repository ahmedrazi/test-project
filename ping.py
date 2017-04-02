import subprocess
import ipaddress
hosts=ipaddress.ip_network('10.0.0.0/24')
for node in hosts:
    subprocess.call(['ping',node])