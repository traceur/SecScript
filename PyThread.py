import os
import queue
import threading
  
queue = queue.Queue()
  
class ThreadPro(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
  
    def run(self):
        while True:
            value = self.queue.get()
            os.system('java -jar xxx.jar %s'%value)
            self.queue.task_done()
        
        print("Consumer Finished")
 
def main():
    for i in range(30):
        t = ThreadPro(queue)
        t.setDaemon(True)
        t.start()
   
    for i in open('order.txt','r'):
        queue.put(i)
    
    queue.join()
     
if __name__ == '__main__':
    main()
