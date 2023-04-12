import threading
import requests

class ConnectionPool:
    def __init__(self, count):
        self.pool = [requests for i in range(count)]
        self.lock = threading.Semaphore(3)

    def getConnection(self):
        # self.lock.acquire()     
        if len(self.pool) > 0:              
            conn = self.pool[0]; del self.pool[0]       
            # self.lock.release()
            return conn
        else:
            # self.lock.release()
            return None


class Service():
    def run(self, pool):    
        
        thread_name = threading.current_thread().name
        
        conn = pool.getConnection()
        
        if conn:
            response = conn.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
            print(thread_name, response)
            return 'nikhil'
        else:
            print(thread_name, 'Connection not available')


pool = ConnectionPool(5) 

service = Service()

service_list = [service for i in range(10)]

for i in range(10):
    thread = threading.Thread(target=service.run, args=(pool,), name='THREAD_'+(str(i+1)))
    thread.start()
