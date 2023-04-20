import threading
import time

#1 Signal using event object

event = threading.Event()

def switch_light():
	while True:
		print('GREEN')
		event.set()
		time.sleep(2)
		event.clear()
		print('RED')
		time.sleep(2)		
		event.set()


def display():
	# event.wait()
	while True:
		if event.is_set():
			print("Please go!")
			time.sleep(0.5)
		else:
			print("Please wait!")
			time.sleep(0.5)
		
# thread1 = threading.Thread(target=switch_light)
# thread2 = threading.Thread(target=display)

# thread1.start()
# thread2.start()



#2 Signal using condition object

condition = threading.Condition()

def sender(lock):
	lock.acquire()
	while True:
		result = input("Please enter password: ")
		if result == 'qwe':
			print('Login successfull\n')
			lock.notify_all()
			lock.release()
			break
		else:
			print('Incorrect password !\n')

def receiver1(lock):
	lock.acquire()
	lock.wait(timeout=0)
	lock.release()
	
	for i in range(5):		
	   print(threading.current_thread().name, ' processing ' + str(i+1) + ' iteration')
	   time.sleep(1)
	
def receiver2(lock):
	lock.acquire()
	lock.wait(timeout=0)
	lock.release()

	for i in range(5):
		print(threading.current_thread().name, ' processing ' + str(i+1) + ' iteration')
		time.sleep(0.4)
	
# thread3 = threading.Thread(target=sender, args=(condition,), name='SENDER_1')
# thread4 = threading.Thread(target=receiver1, args=(condition,), name='RECEIVER_1')
# thread5 = threading.Thread(target=receiver2, args=(condition,), name='REVEIVER_2')

# thread3.start()
# thread4.start()
# thread5.start()


#3 Signal and data passing Queue object

import queue

def entrance(toll_tax_queue):
	vehicle_list = ['Red Swift', 'Green CNG Autorickshaw', 'Yellow School Bus', 'Red Yamaha FZ Bike', 'White Hyndai Creta', 'Brown Reanult Duster', 'Black BMW', 'White Swift Desire', 'Grey Activa', 'Grey Truck', 'Red Tata Nexon', 'White Alto']

	for vehicle in vehicle_list:
		print('Entered: ', vehicle)
		toll_tax_queue.put(vehicle)
		
		# e.set()
		# time.sleep(0.5)
		# e.clear()


def deductTollCharges(event,toll_tax_queue):
	
	while toll_tax_queue.empty() == False:
		print('Charges deducted for : ', toll_tax_queue.get())
		time.sleep(0.7)
	# event.set()
	# event.clear()
	# time.sleep(0.5)

def exit(event):	
	while True:
		if event.is_set():
			print('Vehicle left from the toll tax')
		else:
			time.sleep(0.5)


	
q = queue.Queue()
e= threading.Event()

thread6 = threading.Thread(target=entrance, args=(q,))
thread7 = threading.Thread(target=deductTollCharges, args=(e, q,))
thread8 = threading.Thread(target=exit, args=(e,))

thread6.start()
thread7.start()
#thread8.start()





"""
Inter-thread communication in python

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