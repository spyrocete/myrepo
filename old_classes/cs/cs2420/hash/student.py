import time

class Student:
   def __init__(self,last,first,ssn,email,age):
	self.mLast = last
	self.mFirst = first
	self.mSSN = int(ssn.replace('-',''))
	self.mEmail = email
	self.mAge = float(age)

   def __eq__(self,rhs):
	return int(self.mSSN) == rhs
   def __lt__(self,rhs):
	return int(self.mSSN) < rhs
   def __gt__(self,rhs):
	return int(self.mSSN) > rhs
   def __int__(self):
	return int(self.mSSN)
   def __str__(self):
	return str(self.mSSN).strip() + ' '+self.mLast
   def __mod__(self,other):
	return self.mSSN % other

