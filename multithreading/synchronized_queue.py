# https://docs.python.org/3/library/queue.html
import queue


q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print('Queue:')
print(q.get())
print(q.get())
print(q.get())
print(q.get())


r = queue.LifoQueue()



print('LifoQueue:')
r.put(1)
r.put(2)
r.put(3)
r.put(4)

print(r.get())
print(r.get())
print(r.get())
print(r.get())
