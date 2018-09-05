import random
import sys
import math

def bubble(lst, count):
    size = len(lst)
    sorted = False;
    while not sorted:
          sorted = True
          for i in range (len(lst)-1):
              count[0] += 1
              if lst[i]> lst[i+1]:
                 lst[i],lst[i+1] = lst[i+1],lst[i]
                 sorted = False 
                 count[1] += 1


def selection(lst, count):
    for s in range(len(lst)):
        small=s
        for i in range(s,len(lst)):
            count[0] += 1
            if lst[small] > lst[i]:
               small = i
        lst[s],lst[small] = lst[small],lst[s]
        count[1] += 1


def shaker(lst, count):
    sorted = False;
    while not sorted:
          sorted = True;
          for i in range(len(lst)-1):
              count[0] += 1
              if lst[i]>lst[i+1]:
                 lst[i],lst[i+1] = lst[i+1],lst[i]
                 sorted = False	  
                 count[1] += 1

          for i in range(len(lst)-2,-1,-1):
              count[0] += 1
              if lst[i] > lst[i+1]:
                 sorted = False
                 lst[i],lst[i+1] = lst[i+1],lst[i]
                 count[1] += 1
          if sorted:
             break



def hash(lst):
    f=[0]*len(lst)
    findex=0
    for i in range(len(lst)):
        value = lst[i]
        f[value] +=1
    
    for j in range(len(f)):
        count =f[j]
        for k in range(count):
            lst[findex]=j
            findex+=1



def merge(lst, count):
    result = []
    if len(lst) < 2:
        return lst
    mid = int(len(lst)/2)
    y = merge(lst[:mid], count)
    z = merge(lst[mid:], count)
    i = 0
    j = 0
    count[1] += len(lst)
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    count[0] += len(lst)
    count[1] += len(lst)


def prepare_one(a, left, right): 
    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    i = left + 1
    pivot = a[left]

    for j in range(left + 1, right + 1):
        count[0] += 1
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            count[1] += 1
            i += 1
             
    pos = i - 1
    a[left], a[pos] = a[pos], a[left]
    count[1] += 1
     
    return pos 
 
def quickr(lst, low, high, count, mod):
    if low>=high:
        return
    
    if mod:
        mid = (low+high)/2
        lst[low],lst[mid] = lst[mid],lst[low]

    pivot = low+1
    for i in range(low+1, high+1):
        count[0] += 1
        if (lst[i] < lst[low]):
            lst[i], lst[pivot] = lst[pivot], lst[i]
            count[1] += 1
            pivot += 1
    pivot += 1
    lst[low], lst[pivot] = lst[pivot], lst[low]
    count[1] += 1
    quick(lst, low, pivot-1, count, mod)
    quick(lst, pivot+1, high, count, mod)

def quick(lst, count):
    quickr(lst, 0, len(lst)-1, count, False)

def modified(lst, count):
    quickr(lst, 0, len(lst)-1, count, True)
 

def make_random_lst(size):
    original =[]
    for i in range(size):
        num = random.randrange(1, size)
        original.append(num)
    
    return original

def make_mostly_sorted(size):
    lst = []
    for i in  range(size):
        r = random.randint(0,size-1)
        lst.append(r)
    return lst

# def quick_sort(a, left, right):
 
#     if left < right: 
#         pivot_pos = prepare_one(a, left, right )
        
#         quick_sort(a, left, pivot_pos - 1)
#         quick_sort(a, pivot_pos + 1, right)
#     return a

# def modified(list,low,high):
   
#     loh = low+1
#     if high-low<=0:
	
#         return list
  
#     mid =(low+high)/2
#     list[low],list[mid]=list[mid],list[low]
#     for i in range (low+1,high+1):
#         if list[i]<list[low]:
#             list[i],list[loh]=list[loh],list[i]
#             loh+=1
#     p=loh-1
#     list[low],list[p]=list[p],list[low]
#     modified(list,low,p-1)
#     modified(list,p+1,high)
#     return list
def Format(x):
    if x!=0:
        x = math.log(x)/math.log(2)
        x = "%s.2t" %x
          

def main():
    startingSize = 8
    endingSize = 1024*4
    sys.setrecursionlimit(endingSize+10)
    
    Sortlstlgorithms = [bubble, shaker, selection,merge, quick, modified]
    SortNames = ["bubble", "shaker", "selection","merge", "quick","modified"]
    WhatToCount = ["Comparea", "Swaps"]
    KindOfData = ["Random","MostlySorted"]
    for dataType in KindOfData:
        for countType in WhatToCount:
            print"\n Countiny",countType,"on" ,dataType,"data"
            print"\t",
            for name in SortNames:
                print "\t"+name,
            print
            
            size = startingSize
            while size <=endingSize:
                  print Format(size),
                  for i in range(len(Sortlstlgorithms)):
                      LOriginal = []
                      if dataType =="Random":
                         LOriginal = make_random_lst(size)
                         print LOriginal
                      else:
                         LOriginal = make_random_lst(size)
                      LSorted = LOriginal[:]
                      LSorted.sort()
                      lst = LOriginal[:]
                      count = [0,0]
                      Sortlstlgorithms[i](lst,count)
                      if lst != LSorted:
                         print "error!", SortNames[i]
                         print lst
                         print LSorted
                         sys.exit(0)
                      if countType == "Campares":
                          print "\t\t", Format(count[0]),
                      else:
                          print "\t\t", Format(count[1]),
                  print
                  size *= 2

     


# def main():
#     final_list = make_lst()
#     # print final_list
#     # final_list.sort()
# #    print final_list

#     print "random list"
#     print make_lst()
#     print "selection"
#     print selection(make_lst())
#     print "shaker"
#     print shaker(make_lst())
#     print "bubble"
#     print bubble(make_lst())

#     print "hash"
#     print hash(make_lst())
#     print "merge"
#     print merge(make_lst())
#     print "modified quick"
#     print modified(make_lst(),0,49)
#     print "quick sort"
#     print quick_sort(make_lst(),0,
#    final_list = make_lst()
    # print final_list
    # final_list.sort()
#    print final_list

#    count=[0,0]
# quick sort will need to be put in as a param 
# make mostly sorted list so sort.blu swap 0 with -1
# math.log(x,2)


    
main()
