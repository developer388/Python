class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, value):
		self.queue.append(value)

	def dequeue(self):
		result = self.queue[0]
		del self.queue[0]
		return result

	def isEmpty(self):
		return len(self.queue) == 0

queue = Queue()

print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(16)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
