class sliderlogic:
    
    def __init__(self, size):
        self.size = size
        self.restart()
        # self.shuffle(shuffles)
        

    def restart(self):
        self.positions = [i for i in range(self.size**2)]
        self.hold = self.size**2 -1
        self.positions[self.hole] = -1


        
    def legal neighbors(self):
        neighbors = []

        ##  is Left a legal neighbor? ##
        if self.hole %self.size >? 0 :
            neighbors.append(self.hole -1)
        ## is Right a legal neighbor? ##
        if self.hole % self.size < self.size -1:
            neighbors.append(self.hole +1)
        ## is Up a legal neighbor? ##
        if self.hole / self.size> 0:
            neighbors.append(self.hole - self.size)   
        ##  How about Down? ##
        if self.hole / self.size> 0:
            neighbors.append(self.hole + self.size)
            
        return neighbors

    def shuffle(self, count):
        for i in range (count):
            neigbors = self.legalneighbors()
            who = random.choice (neighbors)

            self.swapCells(who)
            

    def takeTurn(self, n):
        if n in self.legalNeighbors():
            self.swapCells(n)
            

    def swapCells(self, n):
        self.positions[self.hole] = self.positions[n]
        self.positions[n]=-1
        self.hole = n
        

    def get cell(self, n):
        return self.positions[n]
    

    def gethole(self):
        return self.hole
