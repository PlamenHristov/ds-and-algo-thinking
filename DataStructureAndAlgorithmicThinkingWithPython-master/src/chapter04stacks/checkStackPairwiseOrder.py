# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import math
class Stack(object):
	def __init__(self, limit=10):
		self.stk = []
		self.limit = limit	
	def isEmpty(self):
		return len(self.stk) <= 0

	def push(self, item):
		if len(self.stk) >= self.limit:
			print 'Stack Overflow!'
		else:
			self.stk.append(item)
		print 'Stack after Push', self.stk

	def pop(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk[-1]
			
	def size(self):
		return len(self.stk)

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def setData(self, data):
		self.data = data
	# method for getting the data field of the node   
	def getData(self):
		return self.data
	# method for setting the next field of the node
	def setNext(self, next):
		self.next = next
	# method for getting the next field of the node    
	def getNext(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def hasNext(self):
		return self.next != None


class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.rear.getData()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.getData()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.getData()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0	
		
def checkStackPairwiseOrder(stk):
	que = Queue()
	pairwiseOrdered = 1
	# Reverse Stack elements
	while not stk.isEmpty():
		que.enQueue(stk.pop())
	while not que.isEmpty():
		stk.push(que.deQueue())

	while not stk.isEmpty():
		n = stk.pop()
		que.enQueue(n)
		if not stk.isEmpty():
			m = stk.pop()
			que.enQueue(m)
			if (abs(n - m) != 1):
				pairwiseOrdered = 0
				break
	while not que.isEmpty():
		stk.push(que.deQueue())
	return pairwiseOrdered

stk = Stack()
stk.push(-2)
stk.push(-3)
stk.push(11)
stk.push(10)
stk.push(5)
stk.push(6)
stk.push(20)
stk.push(21)
print checkStackPairwiseOrder(stk)
