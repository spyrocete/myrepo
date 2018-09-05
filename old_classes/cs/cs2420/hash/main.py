from student import Student
from hash import *
import time
import urllib2 

# If true it will run hash on the big list if false it will run medium list
biglist = True

def main():
	students = []

	if biglist:
		f = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNamesBig.txt")	
	else:
		f = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNamesMedium.txt")
	a = time.time()
	student_amount = 0
	for line in f:
		#create list of student objects
		temp = line.split()
		student = Student(temp[0],temp[1],temp[2],temp[3],temp[4])
		students.append(student)
		student_amount += 1


	#insert
	initialtime = time.time()
	Container = Hash(student_amount)
	for i in range(len(students)):
		Container.Insert(students[i])

	print "*****************************"
	print "There are",Container.dupecount,"dupecates"
	print 'insert time:',time.time()-initialtime
	print "*****************************"
	#traverse
	initialtime = time.time()
	Container.Traverse()
	print "*****************************"
	print 'Traverse time:',time.time()-initialtime
	print "*****************************"
	b = time.time()
	#delete
	initialtime = time.time()
	Delete(Container)

	print 'delete time:',time.time()-initialtime
	print "*****************************"

	#retrieve
	initialtime = time.time()
	Retrieve(Container)
	print "*****************************"
	print 'Retrieve time:',time.time()-initialtime
	print "*****************************"

def Retrieve(Container):
	if biglist:
		f = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/RetrieveNamesBig.txt")
	else:
		f = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/RetrieveNamesMedium.txt")
	count = 0.0
	size = 0
	for line in f:
                line = line.strip()
		empty = Student('','',line,'',0)
		student = Container.Retrieve(empty)
		if student:
			size += 1
			count += student.mAge
	print "*****************************"
        print 'average retrieve age:', count/size
	print "*****************************"

def Delete(Container):
	if biglist:
		f = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesBig.txt")
	else:
		f = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesMedium.txt")
	
	delcount = 0
	for line in f:
                line = line.strip()
		empty = Student('','',line,'',0)
		ok = Container.Delete(empty)
                if not ok:
                        delcount += 1
#			print 'could not delete', empty
	print "*****************************"
	print "could not delete",delcount,"students"
main()
