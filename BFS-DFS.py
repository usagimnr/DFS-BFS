########################################
#
# This program tests BFS (Breadth-first search) and 
# DFS (Depth-first search) which are algorithms that traverse 
# or search tree or graph data structures.
#
########################################
 
class Node:
	def __init__(self, value):
		self.value = value  
		self.next = None 
	
	def __str__(self):
		return "Node({})".format(self.value) 

	__repr__ = __str__
						  

class Stack:
	def __init__(self):
		self.top = None
		self.count = 0
	
	def __str__(self):
		temp=self.top
		out=[]
		while temp:
			out.append(str(temp.value))
			temp=temp.next
		out='\n'.join(out)
		return ('Top:{}\nStack:\n{}'.format(self.top,out))

	__repr__=__str__
	
	def isEmpty(self):
		if self.top == None:
			return True 
		else: 
			return False

	def __len__(self):
		return self.count

	
	def peek(self):
		if self.top == None:
			return 'Stack is empty'
		else: 
			return self.top.value

	def push(self,value):
		nn = Node(value)
		nn.next = self.top
		self.top = nn 
		self.count += 1

	def pop(self):
		if self.top == None:
			return 'Stack is empty'
		else: 
			x = self.top.value
			self.top = self.top.next 
			self.count -= 1
			return x

class Queue:
	def __init__(self): 
		self.head=None
		self.tail=None
		self.count = 0

	def __str__(self):
		temp=self.head
		out=[]
		while temp:
			out.append(str(temp.value))
			temp=temp.next
		out=' '.join(out)
		return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

	__repr__=__str__

	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False

	def __len__(self):
		return self.count

	def enqueue(self, value):
		if self.head == None:
			nn = Node(value)
			self.tail = nn
			self.head = nn 
			self.count += 1
		else: 
			nn = Node(value)
			self.tail.next = nn
			self.tail = nn
			self.count += 1

	def dequeue(self):
		if self.count == 0:
			return 'Queue is empty'
		elif self.count == 1:
			x = self.head.value
			self.head = None
			self.tail = None
			self.count -= 1
			return x
		else:
			x = self.head.value
			self.head = self.head.next
			self.count -= 1
			return x
   
class Graph:
	def __init__(self, graph_repr):
		self.vertList = graph_repr


	def bfs(self, start):
		if start not in self.vertList:
			return 'error'
		q = Queue()
		q.enqueue(start)
		visited = []
		visited.append(start)
		while q.isEmpty() == False:
			node = q.dequeue()
			neighbor = self.vertList.get(node)
			newList = []
			for x in neighbor:
				if type(x) == tuple:
					if x[0] not in visited:
						q.enqueue(x[0])
						newList.append(x[0])
				elif type(x) == str:
					if x not in visited:
						q.enqueue(x)
						newList.append(x)
			sortList = sorted(newList)
			for x in sortList:
				visited.append(x)

		return visited



	def dfs(self, start):
		s = Stack()
		s.push(start)
		visited = []
		while s.isEmpty() != True:
			node = s.pop()
			if node not in visited:
				visited.append(node)
			newList = []
			neighbor = self.vertList.get(node)
			for x in neighbor:
				if type(x) == tuple:
					if x[0] not in visited:
						newList.append(x[0])
				elif type(x) == str:
					if x not in visited:
						newList.append(x)
			sortList = sorted(newList, reverse = True)
			for x in sortList:
				if x not in visited:
					s.push(x)
		return visited	
