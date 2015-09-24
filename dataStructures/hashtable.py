class HashTable:
	def __init__(self, size):
		''' Initializes hashtable size and two lists 
		to keep track of the key and the data ''' 
		
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data):
		''' Inserts new key/data into the hashtable'''
		hashvalue = self.hashfunction(key)

		if self.slots[hashvalue] == None:
			
			self.slots[hashvalue] = key
			self.data[hashvalue] = data

		else:

			if self.slots[hashvalue] == key:
				#if key exists replace old data with new
				self.data[hashvalue] = data
			else:
				nextslot = self.rehash(hashvalue)
				#keep on rehashing until you find an empty spot or the key
				# perform linear probing with open addressing
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot)
				
				if self.slots[nextslot] == None:
					self.slots[hashvalue] = key
					self.data[hashvalue] = data
				else:
					self.data[hashvalue] = data

	def hashfunction(self, key):
		''' Hashfunction using the remainder method '''
		return key % self.size

	def rehash(self, oldhash):
		''' Performs linear probing with open addressing to return a new place to hash '''
		return (oldhash + 1) % self.size

	def get(self, key):
		''' Returns data of the provided key '''
		startslot = self.hashfunction(key)

		data = None
		stop = False
		found = False
		position = startslot

		while self.slots[position] != None and not found and not stop:

			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position)
				# if you searched the whole list and came back to the starting point, return None
				if position == startslot:
					stop = True

		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)