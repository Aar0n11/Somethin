import subprocess 

ips = []
netIndicies = []
netIps = []

try: 
    ipconf = subprocess.check_output(["ipconfig"], text=True)
    ipSplit = ipconf.splitlines()
    for i in range(len(ipSplit)):
        if "IPv4" in ipSplit[i]:
            ip = ipSplit[i].split(":", 1)
            ips.append(ip)
            print(ip[1])

    net = subprocess.check_output(["arp", "-a"], text=True)
    netSplit = net.splitlines()
    for j in range(len(netSplit)):
        if "Interface" in netSplit[i]:
            netIndicies.append(i)

    for u in range(len(netIndicies)):
        

except subprocess.CalledProcessError as e: 
    print(f"Command failed with return code {e.returncode}")