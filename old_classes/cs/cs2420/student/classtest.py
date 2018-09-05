
import urllib2  # the lib that handles the url stuff
import time

class students:
    def __init__(self, name, last, ssn, email, age):
        self.name = name
        self.last = last
        self.ssn = ssn
        self.email = email
        self.age = age
        
    def getname(self, name):
        return self.name

    def getlast(self, last):
        return self.last

    def getssn(self, ssn):
        return self.ssn        

    def getemail(self, email):
        return self.email

    def getage(self, age):
        return self.age    


def read_url():
    data = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNames.txt") # it's a file like object and works just like a file
    for line in data: # files are iterable
        words = line.split()
        s = students(words[0], words[1], words[2], words[3], words[4])
        print s.getssn(words[2])
        for  

        # duplicate = False
        # for i in studentlst:
        #     if 

def main():
    read_url()

main()
