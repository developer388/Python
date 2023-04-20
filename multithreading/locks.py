import threading
import time

class User:
    def __init__(self, name):
        self.name = name
        self.booked_seats = []

    def update(self, booked_seat):
        self.booked_seats.append(booked_seat)

class SeatBookingService:
    def __init__(self):
        self.__total_seat = 10
        self.lock = threading.Lock()          # lock created
                   #threading.Semaphore(1)
        
    def getAvailableSeat(self):
        return self.__total_seat

    def bookSeat(self, user):
        # print('\n')
        print(f'For {user.name} available seats in system: {str(self.__total_seat)}')
        if self.__total_seat  > 0:
            
            self.lock.acquire()              # lock accuired 
            seat_no = self.__total_seat       

            time.sleep(0.1)                   # read the total_seat and sleep()

            self.__total_seat -= 1
            self.lock.release()               # lock released
        
            user.booked_seats.append(seat_no)
            print(f'For {user.name} seat_no {seat_no} booked, available seats in system after booking {str(self.__total_seat)}')
            return True
        else:
            print('booking failed for ' + user.name)
            return False


"""
 Program info:
 - User can book a seat using SeatBookingService
 - Whenever a seat is booked we will print the available seats in the system prior to actual booking
   During booking we will decrement the total_seat counter and print the available seat in system after booking

 - In case of a multithreaded program it can lead to race condition as multiple Users (executing in seperated thread)
   will try to decrement the common data structure

 - In above example, without lock all threads will read the same initial value of total seats (i.e 10)
   and then try to book the seat and decrement the total_seat counter

"""
    
service = SeatBookingService()    # service created

users = [User('Nikhil'), User('Fedrick'), User('Rob'), User('Falcon'), User('Raj'), User('Anna')]  # List of 6 Users

for user in users:                # for each user create and start a seperate thread
    thread = threading.Thread(target=service.bookSeat, kwargs={'user':user})
    thread.start()                # thead started
    
"""
    Starting above threads without lock will give inconsistent results as critical section is not protected
    
    Program output without using Lock:  

        For Nikhil available seats in system: 10
        For Fedrick available seats in system: 10
        For Rob available seats in system: 10
        For Falcon available seats in system: 10
        For Raj available seats in system: 10
        For Anna available seats in system: 10
        For Nikhil seat_no 10 booked, available seats in system after booking 9
        For Fedrick seat_no 10 booked, available seats in system after booking 8
        For Rob seat_no 10 booked, available seats in system after booking 7
        For Raj seat_no 10 booked, available seats in system after booking 6
        For Anna seat_no 10 booked, available seats in system after booking 4
        For Falcon seat_no 10 booked, available seats in system after booking 5

        All users ended up booking the same seat 

    
    Program output after using Lock:

        For Nikhil available seats in system: 10
        For Fedrick available seats in system: 10
        For Rob available seats in system: 10
        For Falcon available seats in system: 10
        For Raj available seats in system: 10
        For Anna available seats in system: 10
        For Nikhil seat_no 10 booked, available seats in system after booking 9
        For Fedrick seat_no 9 booked, available seats in system after booking 8
        For Falcon seat_no 8 booked, available seats in system after booking 7
        For Rob seat_no 7 booked, available seats in system after booking 6
        For Raj seat_no 6 booked, available seats in system after booking 5
        For Anna seat_no 5 booked, available seats in system after booking 4

        Before reading and decrementing the total_seat counter thread accuired the lock
        
        All threads read and updated the counter in syncronized manner which resulted in
        consistent result
        
"""





"""
Concept

There are 3 ways to perform locking in python:

1. threading.Lock 
    
    A primitive lock is a synchronization primitive that is not owned by a particular thread when locked. 
    In Python, it is currently the lowest level synchronization primitive available, implemented directly 
    by the _thread extension module.

    A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. 
    It has two basic methods, acquire() and release(). 
    
    When the state is unlocked, acquire() changes the state to locked and returns immediately. 
    
    When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, 
    then the acquire() call resets it to locked and returns. 
    
    The release() method should only be called in the locked state; it changes the state to unlocked and returns immediately. 
    If an attempt is made to release an unlocked lock, a RuntimeError will be raised.
    
    class threading.Lock
        acquire(blocking=True, timeout=- 1)
        release()
        locked()

2. threading.RLock
   
   A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread. 
   Internally, it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked 
   state used by primitive locks. 
   
   In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.

   To lock the lock, a thread calls its acquire() method; this returns once the thread owns the lock. 
   
   To unlock the lock, a thread calls its release() method. acquire()/release() call pairs may be nested; 
   only the final release() (the release() of the outermost pair) resets the lock to unlocked and allows another 
   thread blocked in acquire() to proceed.

   class threading.RLock
        acquire(blocking=True, timeout=- 1)
        release()

3. threading.Semaphore
    
    A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call. 
    The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().

    semaphore can be used when we want to allow multiple threads to enter critical sections

    class threading.Semaphore(value=1)
        This class implements semaphore objects. A semaphore manages an atomic counter representing the number of release()
        calls minus the number of acquire() calls, plus an initial value. The acquire() method blocks if necessary until it can
        return without making the counter negative. If not given, value defaults to 1.

        The optional argument gives the initial value for the internal counter; it defaults to 1. 
        If the value given is less than 0, ValueError is raised.

        acquire(blocking=True, timeout=None)   decrements semaphore counter
        release(n=1)                           increments semaphone counter 

    
    Using semaphore as value 1 is smiliar to Lock and RLock, since only one thread is allowed to enter in critical section
    Using semaphore as greater than 1 can lead to race conditions we are allowing multiple threads to act on critical section


    Semaphore is compatible with RLocks therefore we can multiple times accuire() and release() locks, but since semaphore is counter based.
    releasing() lock multiple time in an incorrect manner can lead to unexpected behaviour and even system crash. For multiple times release()
    lock safety
    
    BoundedSemaphore can be used, which internally handles such cases.

    class threading.BoundedSemaphore(value=1)
        Class implementing bounded semaphore objects. A bounded semaphore checks to make sure its current value doesn’t exceed its initial value. 
        If it does, ValueError is raised. In most situations semaphores are used to guard resources with limited capacity. 
        If the semaphore is released too many times it’s a sign of a bug. If not given, value defaults to 1.

"""





