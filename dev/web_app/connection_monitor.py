from flask import Flask, render_template
app = Flask(__name__)

import threading
from queue import Queue
import time
import socket

print_lock = threading.Lock()


target = 'xploreitcorp.com'
port_all="21,20,23,25,80"
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            port_all=port_all+","+port
        con.close()
    except:
        pass


def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()



        

# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(30):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()


start = time.time()

# 100 jobs assigned.
for worker in range(1,100):
    q.put(worker)

# wait until the thread terminates.
q.join()
print(port_all)

@app.route('/scan')
def result():
    port_list = port_all.split(",")
    return render_template('result.html', ports =port_list )

if __name__ == '__main__':
    app.run(debug = True)
    
