import collections

class newDict (collections.UserDict):
	def __missing__(self,key):
		if isinstance(key,str):
			raise KeyError(key)
		return self[str(key)]
	
	def __setitem__(self,key,item): #it will recursion if use 'dict', UserDict will not
		self.data[str(key)] = item
	
	def __contains__ (self,key):
		return str(key) in self.data

a = newDict([('1','one'),('2','two')])
a [32] = 11
print(32 in a)