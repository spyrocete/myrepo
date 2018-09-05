import student
class Node:
    def __init__(self,data,lnode,rnode):
        self.mData = data
        self.mLeft = lnode
        self.mRight = rnode

class bst:
    def __init__(self):
        self.mcount = 0
        self.mRoot = None

    def Exist(self,data):
        return self.ExistR(data,self.mRoot)

    def ExistR(self,data,curr):
        if curr == None:
            return False
        elif curr.mData == data:
            return True
    
        elif data< curr.mData:
            return self.ExistR(data,curr.mLeft)
        elif data> curr.mData:
            return self.ExistR(data,curr.mRight)

    def Insert(self,data):
        if self.Exist(data):
            return False
        self.mRoot = self.InsertR(data,self.mRoot)
        
        return True

        
    def InsertR(self,data,curr):
        if curr ==None:
            n=Node(data,None,None)
            curr = n 
            self.mcount +=1
        elif data<curr.mData:
            curr.mLeft = self.InsertR(data,curr.mLeft)
        else:
            curr.mRight = self.InsertR(data,curr.mRight)
        return curr

    def Traverse(self,callback):
        
        self.TraverseR(self.mRoot,callback)

    def TraverseR(self,curr,callback):
        if curr ==None:
            return
        self.TraverseR(curr.mLeft,callback)
        callback(curr.mData)
        self.TraverseR(curr.mRight,callback)


    def Retrieve(self,data):
        return self.RetrieveR(data,self.mRoot)

    def RetrieveR(self,data,curr):  #delete self.mRoot
        if (curr == None):
            return None

        elif (curr.mData==data):
            return curr.mData
        elif (data<curr.mData):
            return self.RetrieveR(data,curr.mLeft)
00        e00lse:
            return self.RetrieveR(data,curr.mRight)
    

    def TrueCount(self):
        return self.CountR(self.mRoot)

    def CountR(self,node):
        if node==None:
            return 0
        return 1+self.CountR(node.mLeft)+self.CountR(node.mRight)
    def Count(self):
        return self.mcount

    def Delete(self,data):
        if not self.Exist(data):
            return False
        self.mRoot=self.DeleteR(data,self.mRoot)
        self.mcount -=1
        return True

    def DeleteR(self,data,curr):
        if data < curr.mData:
            curr.mLeft = self.DeleteR(data,curr.mLeft)
        elif data> curr.mData:
            curr.mRight = self.DeleteR(data,curr.mRight)
        else:
            if curr.mLeft == None and curr.mRight ==None:
                curr = None
            elif curr.mRight == None:   #left only
                curr=curr.mLeft
            elif curr.mLeft ==None:    #right only
                curr=curr.mRight
            else:   #two children
                ios = curr.mRight
                while ios.mLeft != None:
                    ios = ios.mLeft
                curr.mData = ios.mData
                curr.mRight = self.DeleteR(ios.mData,curr.mRight)
        return curr





            
