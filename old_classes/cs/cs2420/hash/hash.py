
class Node:
#Student container class
   def __init__(self,item,nextitem=None):
	self.mItem = item
	self.mNext = nextitem


class Hash:
	def __init__(self,size):
		self.TableSize = size
		self.mTable = []
		self.mSize = 0
		self.mCount = 0
                self.dupecount = 0
		self.mRetrieveSize = 0
		for i in range(size):
			self.mTable.append(None)
	def Insert(self,item):

	#recieves a student object
	#create hash code
	#check if it already exists
	#insert it into the chain at table[hashcode]
		item = Node(item)
		if self.Exists(item) == True:
		#if item exists, return leaving a message
                        self.dupecount += 1
#			print item.mItem,'already exists'
			return
		hashcode = item.mItem % self.TableSize
		if self.mTable[hashcode] is None:
			self.mTable[hashcode] = item
		else:
		#there is already an item at that index
		#assign the item that is already there to
		#point to the current item
			c = self.mTable[hashcode]
			while c.mNext:
				c = c.mNext
			c.mNext = item
		self.mSize += 1

	def Delete(self,item):
		#recieves a student object
		item = Node(item)
		if self.Exists(item) == False:
			#item does not exist
			return False
		self.mSize -= 1
		hashcode = item.mItem % self.TableSize
		c = self.mTable[hashcode]
		previous = self.mTable[hashcode]
		if self.mTable[hashcode].mItem == item.mItem:
			self.mTable[hashcode] = self.mTable[hashcode].mNext
			return True
		#check the chains
		else:
			#iterate c, we already checked this one
			#I still have problems with this
			c = c.mNext
			while c:
				if c.mItem == item.mItem:
					previous.mNext = c.mNext
					return True
				else:
					previous = c
					c = c.mNext
				
	def Retrieve(self,item):
		#recieves a student object and finds that objects age
		item = Node(item)
		if self.Exists(item) == False:
			return None
		self.mRetrieveSize += 1
		hashcode = item.mItem % self.TableSize
		c = self.mTable[hashcode]
		while True:
			if c.mItem == item.mItem:
				return c.mItem
			else:
				c = c.mNext
	
		
	def Traverse(self):
		count = 0
		table = self.mTable
		for i in range(len(table)):
			c = table[i]
			while c:
				count += c.mItem.mAge
				c = c.mNext
		print 'average age:',count/self.mSize

	def Exists(self,item):
		#recieves a node object
		hashcode = item.mItem % self.TableSize
		c = self.mTable[hashcode]
		if c is None:
			return False
		elif c.mItem == item.mItem:
			#item exists
			return True
		else:
			while c.mNext:
				c = c.mNext
				if c.mItem == item.mItem:
					return True
			return False
		
		
