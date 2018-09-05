import student
import bst
import urllib2 
import time

biglist = True

age = 0
def main():
    student_bst = bst.bst()
    total_age = 0
    count1 = 0
    print "start..."
    if biglist:
        data = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNamesBig.txt")	
    else:
        data = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNamesMedium.txt")
        data = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNames.txt")
    time1 = time.time()
    for line in data:
        words = line.split()
        s = student.student(words[0],words[1],words[2],words[3],words[4])
        test=student_bst.Insert(s)
        
        if not test:
            temp = 1
#            print "this one is duplicate:  ", words[2]
                
    time2 = time.time()
    tt1 = time2  -time1
    print "Insert time is: ",tt1, " seconds."
    print "total count is ",student_bst.Count()

# true count is to test the count
#    print "TrueCount is: ",student_bst.TrueCount()

#########################################
########## Traverse Code ################
#########################################
    timeage1 = time.time()
    print "Start Traverse Process...."
    Traverse(student_bst)
    timeage2 = time.time()
    ttage = timeage2 - timeage1
    print "Count age took ", ttage, " seconds."

#########################################
########## Delete Code ##################
#########################################
    time3 = time.time()
   
    print "Start Delete Process..."
    if biglist:
        data2 = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesBig.txt")
    else:
        data2 = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesMedium.txt")


    for line2 in data2:
        ssn = line2.split()
        s2 = student.student("","",ssn[0],"","")
        test2 = student_bst.Delete(s2)
        if not test2:
            temp = 1
#            print "The SSN ", ssn[0], " dose not exist."
    time4 = time.time()
    tt2 = time4-time3
    print "Delete took ", tt2, " seconds."

#########################################
########## Retrieve Code ##################
#########################################
    time5 = time.time()
    print "Start Retrieve: "
    if biglist:
        data3 = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesBig.txt")
    else:
        data3 = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesMedium.txt")
	
    #data3 = open("retrieve.txt")
    for line3 in data3:
        retrieve =line3.split()
        s3 = student.student("","",retrieve[0],"","")
        test3 = student_bst.Retrieve(s3)
        
        if test3:
            count1 += 1
            total_age += float(test3.Getnum())
        else:
            temp = 1
#            print "The SSN is: ", retrieve[0], " dose not exist."
    
        
    time6 = time.time()
    tt3 = time6 - time5
#    print "Average age is: ", total_age/count1
    
    print "Retrieve took: ",tt3 , " seconds."

def Addage(s):
    global age
    age +=int(s.Getnum())
    
def Traverse(student_bst):
    global age
    age = 0
    student_bst.Traverse(Addage)
    print "The average age is ", float(age)/student_bst.Count(), " years old"

main()
        
