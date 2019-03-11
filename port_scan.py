import socket
import sys

if len(sys.argv)!=3: # to verify if all arguments
    print("Usage python Psanner.py [ip] [ports]")
    print("Exemple python Pscanner.py 192.168.1.10 21,22,25")
    sys.exit()
    
ports = sys.argv[2].split(",") # assign port to ports variable
ports=[int(p) for p in ports] # cast list items to integer type
ip=sys.argv[1] # assign ip address
i=1 # variable use to print once

for port in ports: # starting port scanning
    try: # exception

        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# socket object initiate
        rep=sock.connect_ex((ip,port)) # connecting to target
        if rep==0: # check the respond after connection attemp
                if i==1: # just to print once
                    print("Report for {0}:".format(ip))
                    i=i-1

                    print("Port {0} Open".format(port)) # print if port open
                else:
                    print("Port {0} close".format(port)) # print if port close
    except Exception as e:
        pass

sock.close()# close socket
print("thewind")