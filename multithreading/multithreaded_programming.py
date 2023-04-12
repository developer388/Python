import threading
import time


# thread creation using threading.Thread() method
def worker1():
    for i in range(100):        
       print('in worker2: ', i)
       time.sleep(1)

def worker2():
    for i in range(100):
       print('in worker1: ',i)
       time.sleep(3)

thread1 = threading.Thread(target=worker1, args=(), daemon=False)
thread2 = threading.Thread(target=worker2, args=(), daemon=False)


#thread1.start()
#thread1.join() # thread2 will not start until thread1 completes its execution
#thread2.start() 
# print(threading.current_thread().name)
# print(threading.current_thread().ident)
# print(threading.current_thread().is_alive())

#print(time.time()) # prints epoch time



# thread creating using inheriting Thread class and overiding run()
class MyClass(threading.Thread):
    def __init__(self):
        print('thread created')
        super().__init__()
    def run(self):
        while True:
           print('arg')
           time.sleep(1)


# method provided by Thread class

# t1 = MyClass()
# t1.start()
# time.sleep(2)
# print('Child ident: ', t1.ident)
# print('Child ident: ', t1.native_id)

# main =  threading.current_thread()
# print('MAIN ident: ', main.ident)
# print('MAIN pid: ', main.native_id)
# print('active count: ', threading.active_count())
# print('List of all threads: ', threading.enumerate())
# print('Main thread details: ', threading.main_thread())
# print('Thread alive status ', main.is_alive())
# print('Get native id of thread from which called', threading.get_native_id())



# t2 = MyClass()


"""
https://docs.python.org/3/library/threading.html
https://www.youtube.com/watch?v=Gp-ppEddKHM

Threads are python objects of threading.Thread class

threading.current_thread()  returns reference to current thread object


Steps to create a thread in python:
1. import thread class from threading module
2. create a function containing code to be executed parallely
3. create an object of thread class
4. start thread using .start() method

t1 = Thread(target=function_name, args=(,))
t1 = Thread(target=function_name, kwargs={'value': 1})

args: arguments passed as tuple; comma is neccessary for tuples hence single comma is necessary
kwargs: can also be passed 


A second way to create threads in python is to extend Thread class.

Thread class has a method called run()
when a thread is created using Thread(target=function_name, args=(,))
function reference passed in target argument is called by the internal run() method of thread class

In second way we can extend thread class and overide run() method to provide our implentation

class MyClass(Thread):
    def run():
        <login>
t1 = MyClass()

if a thread needs to be executed after an another thread join() method is used


Locking mechanism:
1. Lock 
    A primitive lock is a synchronization primitive that is not owned by a particular thread when locked. 
    In Python, it is currently the lowest level synchronization primitive available, implemented directly by the _thread extension module.

    A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. 
    It has two basic methods, acquire() and release(). When the state is unlocked, acquire() changes the state to locked and returns immediately. 
    When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to locked and returns. 
    The release() method should only be called in the locked state; it changes the state to unlocked and returns immediately. 
    If an attempt is made to release an unlocked lock, a RuntimeError will be raised.
    
    class threading.Lock
        acquire(blocking=True, timeout=- 1)
        release()
        locked()

2. RLock
   A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread. 
   Internally, it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked state used by primitive locks. 
   In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.

   To lock the lock, a thread calls its acquire() method; this returns once the thread owns the lock. 
   To unlock the lock, a thread calls its release() method. acquire()/release() call pairs may be nested; 
   only the final release() (the release() of the outermost pair) resets the lock to unlocked and allows another thread blocked in acquire() to proceed.

   class threading.RLock
        acquire(blocking=True, timeout=- 1)
        release()

3. Semaphore
    A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call. 
    The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().

    semaphore can be used when we want to allow multiple threads to enter critical sections

    class threading.Semaphore(value=1)
        This class implements semaphore objects. A semaphore manages an atomic counter representing the number of release() calls minus the number of acquire() calls, 
        plus an initial value. The acquire() method blocks if necessary until it can return without making the counter negative. If not given, value defaults to 1.

        The optional argument gives the initial value for the internal counter; it defaults to 1. If the value given is less than 0, ValueError is raised.

        acquire(blocking=True, timeout=None)   decrements semaphore counter
        release(n=1)                           increments semaphone counter 

    
    Using semaphore as value 1 is smiliar to Lock and RLock, since only one thread is allowed to enter in critical section
    Using semaphore as greater than 1 can lead to race conditions we are allowing multiple threads to act on critical section


    Semaphore is compatible with RLocks therefore we can multiple times accuire() and release() locks, but since semaphore is counter based.
    releasing() lock multiple time in an incorrect manner can lead to unexpected behaviour and even system crash. For multiple times release() lock safety
    BoundedSemaphore can be used, which internally handles such cases.

    class threading.BoundedSemaphore(value=1)
        Class implementing bounded semaphore objects. A bounded semaphore checks to make sure its current value doesn’t exceed its initial value. 
        If it does, ValueError is raised. In most situations semaphores are used to guard resources with limited capacity. 
        If the semaphore is released too many times it’s a sign of a bug. If not given, value defaults to 1.


Exception handling in mulithread program


Thread Lifecylce

1. New Thread   (until we call thread.start() method)

2. Running Thread (when start() is called)          2.1 Blocked Thread  (waiting for I/O, acquire lock)

3. Termiated Thread   
     3.1 Terminated with exception
     3.2 Terminated normally


Thread Communication
  Thread communicates with each other using signals

  There are three ways to do this
    1. create event object
            event object is based on a boolean flag
            using event object we can perform communication between two theads only
            event class has these methods:
                1. set() it sets flag value to True
                2. wait() thread two call wait method to wait for the signal
                3. clear() reset the internal flag to False
                           second thread with wait again
                4. is_set()  returns true if internal flag is true
                5. wait(timeout) keeps second thread in waiting state for signal for specified time
        
        event = threading.Event()
        
        Thread 1
        event.set()     set the flag to true
         ...
        event.clear()   set the flat to false

        Thread 2
        event.wait()

        if event.is_set()
           ... do something when flag is true
        else
           ... do something when flag is false

    2. condition object

        condition object can be used when we want to unblock other multiple threads

        condition object uses concecpt of lock acquire and release

        condition = threading.Condition()

        Thread 1
        condition.acquire()
        condition.notify() other threads when a condition is met.
        condition.release()
        
        Thread 2
        condition.acquire()
        condition.wait() other threads when a condition is met.
        condition.release()

    3. use queue module
        queue provided atomic operations using inbuilt thread synchronization logic

        import queue
        q = queue.Queue()
        queue.empty() returns bool
        queue.put(value) add item to queue
        queue.get()      read item from the queue

"""


# using locks and semaphores for critical section

class User:
    def __init__(self, name):
        self.name = name
        self.booked_seats = []

    def update(self, booked_seat):
        self.booked_seats.append(booked_seat)

class SeatBooking:
    def __init__(self):
        self.__total_seat = 10
        self.lock = threading.Lock() #threading.Semaphore(1)
        
    def getAvailableSeat(self):
        return self.__total_seat

    def bookSeat(self, user):
        print('\n')
        print('For ' + user.name + ' available seats in system: '+ str(self.__total_seat))
        if self.__total_seat  > 0:
            seat_no = self.__total_seat
            

            self.lock.acquire()   
      
            self.__total_seat -= 1
            self.lock.release()

            # with self.lock:
            #     self.__total_seat -= 1        

            user.booked_seats.append(seat_no)
            print('For ' + user.name + ' available seats in system after booking '+ str(self.__total_seat))
            return True
        else:
            print('booking failed for ' + user.name)
            return False


    
service = SeatBooking()


users = [User('Nikhil'), User('Fedrick'), User('Rob'), User('Falcon'), User('Raj'), User('Anna')]




def start():
    for user in users:
        thread = threading.Thread(target=service.bookSeat, kwargs={'user':user})
        thread.start()

    

# thread1 = threading.Thread(target=service.bookSeat, args=(0,0, user1))
# thread2 = threading.Thread(target=service.bookSeat, args=(0,0, user2))

# thread1.start()
# thread2.start()




#print(service.bookSeat(0,0, user1))

start()

time.sleep(2)


print('\n')
for user in users:
    print(f'{user.name} booked_seats: {user.booked_seats}')
