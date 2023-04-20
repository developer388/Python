import threading     # threading package imported for thread releated classes
import time          # time module imported to use sleep() function


def worker1():
    for i in range(1,11):        # print no. from 1 to 10  
       print('Worker1: ', i)
       time.sleep(0.5)

def worker2():
    for i in range(11,21):       # print no. from 11 to 20
       print('Worker2: ',i)
       time.sleep(1)



# Execution of worker1 and worker2 in sequence 

# worker1()
# worker2()

# Thread creation using threading.Thread() method

thread1 = threading.Thread(target=worker1, args=(), daemon=False)
thread2 = threading.Thread(target=worker2, args=(), daemon=False)


# start thread1 and thread2 using start() method
# we will observe interleaved concurrent execution output of worker1 and worker2

thread1.start()
#thread1.join()

thread2.start()


# thread.join() method can be used to make a thread non-preemtive
# meaning other thread wills have to wait for current thread to complete



# Thread creation by inheriting Thread class and overiding run() method
class MyApp(threading.Thread):
    
    def __init__(self):
        print('MyApp instantiated')
        super().__init__()
    
    def run(self):
        for i in range(21,31):
           print('Worker3: ', i)
           time.sleep(0.8)

thread3 = MyApp()
thread3.start()


# every python program has a main thread from which other threads called child threads are spawned
# below while loop is executed in main thread

# while True:
#     print('Main executed')
#     print('Worker1:', thread1.is_alive(), ' Worker2:', thread2.is_alive(), ' Worker3:', thread3.is_alive())
#     time.sleep(2)


# print(time.time()) # prints epoch time

# Thread Info

print('\nthread1.name:', thread1.name)
print('thread1.ident:', thread1.ident)
print('thread1.is_alive:', thread1.is_alive())
print('thread1.native_id: ', thread1.native_id)

# Methods provided by threading module

# main =  threading.current_thread() get reference to current executing thread
print('\nactive threads count: ', threading.active_count())
print('list of all threads: ', threading.enumerate())
print('Main thread details: ', threading.main_thread())
print('Get native id current thread', threading.get_native_id())


"""
Threading Official Documentation: https://docs.python.org/3/library/threading.html
Youtube Tutorial Playlist:  https://www.youtube.com/watch?v=Gp-ppEddKHM

Theory of above programs

Threads are python objects of threading.Thread class

There are two ways by which we can create a thread in python
1. Creating an object of Thread class and passing it the reference of you code function
2. Extending Thread class in you program and overiding the run() method of Thread class

1st Way:
    1. import thread class from threading module
    2. create a function containing your code
    3. create an object of thread class and pass reference of your function in target argument
    4. start the thread using .start() method
    
    Example:
    t1 = Thread(target=function_name, args=(,), daemon=False name='name_of_thread')
    t1 = Thread(target=function_name, kwargs={'value': 1})

    args: arguments passed as tuple; comma is neccessary for tuples hence single comma is necessary
    kwargs: can also be passed 
    
    Thread class has a internal method called run()
    when a thread is created using Thread(target=function_name, args=(,))
    function reference passed in target argument is called by the internal run() method of thread class


2nd Way:
    1. Create a custom class and extend the Thread class
    2. Overide the run() method and provide our own logic in run() method
    
    Example:
        class MyClass(Thread):
            def run():
                <login>
        t1 = MyClass()


join(timeout=None):
    Wait until the thread terminates. This blocks the calling thread until the thread whose join() method is
    called terminates – either normally or through an unhandled exception – or until the optional timeout occurs.

    When the timeout argument is present and not None, it should be a floating point number specifying a timeout
    for the operation in seconds (or fractions thereof). As join() always returns None, you must call is_alive()
    after join() to decide whether a timeout happened – if the thread is still alive, the join() call timed out.

    When the timeout argument is not present or None, the operation will block until the thread terminates.

    A thread can be joined many times.

    join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock.
    It is also an error to join() a thread before it has been started and attempts to do so raise the same exception.
    threading.current_thread()  returns reference to current thread object

daemon
    A boolean value indicating whether this thread is a daemon thread (True) or not (False). This must be set before
    start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the 
    main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.

    The entire Python program exits when no alive non-daemon threads are left.


Thread Lifecycle

1. New Thread   (until we call thread.start() method)
       |
       V
2. Running Thread (when start() is called)  --->    2.1 Blocked Thread  (waiting for I/O, acquire lock)
       |
       V
3. Termiated Thread   
     3.1 Terminated with exception
     3.2 Terminated normally
"""