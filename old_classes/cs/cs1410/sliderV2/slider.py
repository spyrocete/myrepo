# Andrew Coulter

import pygtk
import gtk
import random
import solver




class SliderGUI:
    def __init__(self, size, imagefilename):

        self.size = size
        self.pixbufs=[]
        self.images = []
        self.buttons = []
        self.Slider = SliderLogic(size)


        self.readImageFile(imagefilename)

        self.cellheight = self.full_height / size
        self.cellwidth = self.full_width / size

        
        self.createWindow()        
        self.createBtnImages()
        self.createMenu()
        self.createGame()
        self.updateDisplay()
        

        self.window.show_all()


    def readImageFile(self, imagefilename):

        image = gtk.Image()
        image.set_from_file(imagefilename)

        
        self.full_pixbuf = image.get_pixbuf()
        self.full_height = self.full_pixbuf.get_height()
        self.full_width = self.full_pixbuf.get_width()

        
        

        
    def createWindow(self):

        self.window = gtk.Window()
        self.window.set_title("Slide on")
        self.window.connect('delete_event', self.delete_handler, None)
        self.window.connect('destroy', self.destroy_handler, None)
        self.window.resize(self.full_width, self.full_height)
        self.window.show_all()
        self.window.set_resizable(False)
        self.vbox = gtk.VBox()
        self.window.add(self.vbox)
        


        
    def createBtnImages(self):


        for xval in range (0, self.full_width, self.cellwidth):
            for yval in range (0, self.full_height, self.cellheight):
                subpixbuf = self.full_pixbuf.subpixbuf(xval, yval,self.cellwidth, self.cellheight)
                self.pixbufs.append(subpixbuf)


    def createMenuItem(self, title, handler):

        item = gtk.MenuItem(title)
        item.connect("activate", handler, None)
        self.menu.append(item)

    def createMenu(self):


        
        
        self.menu = gtk.Menu()
        self.createMenuItem("Start Over", self.restart_handler)
        self.createMenuItem("Solve", self.solve_handler)
        self.createMenuItem("Quit", self.destroy_handler)


        self.root_menu = gtk.MenuItem('Game')
        self.root_menu.set_submenu(self.menu)


        self.Menu_Bar = gtk.MenuBar()
        self.Menu_Bar.append(self.root_menu)
        self.vbox.pack_start(self.Menu_Bar)

        

    def createGame(self):
 
        self.table = gtk.Table(self.size, self.size)
        i = 0
        for x in range(self.size):
            for y in range(self.size):
                image = gtk.Image()
                image.set_from_pixbuf(self.pixbufs[i])
                self.images.append(image)
                button = gtk.Button()
                button.add(image)
                button.connect('clicked', self.clicked_handler, i)
                self.buttons.append(button)
                self.table.attach(button, x, x+1, y, y+1)
                i += 1
                
        self.vbox.pack_start(self.table)

    def updateDisplay(self):

        hole = SliderLogic.getHole(self.Slider)
        for i in range(len(self.buttons)):
           n = SliderLogic.getCell(self.Slider,i)
           pixbuf = self.pixbufs[n]
           img = self.images[i]
           if i == hole:
               img.clear()
           else:
               img.set_from_pixbuf(pixbuf)

         

    def delete_handler(self, widget, event, data):

        return False

    def destroy_handler(self, widget, data=None):

        gtk.main_quit()

    def restart_handler(self, widget, data):
        self.Slider.restart()
        self.Slider.shuffle(110)
        self.updateDisplay()
        

    def solve_handler(self, widget, data):


        print 'solve'

    def clicked_handler(self, widget, data):
        self.Slider.takeTurn(data)
        print 'clicked' + str(data)
        self.updateDisplay()

    def run(self):

         gtk.main()



##         Part 2 SliderLogic   ##

class SliderLogic:
    
    def __init__(self, size):

        self.size = size
        self.restart()

        

    def restart(self):

        self.positions = [i for i in range(self.size**2)]
        self.hole = (self.size**2) -1
        self.positions[self.hole] = -1


        
    def legalNeighbors(self):

        neighbors = []


        if self.hole % self.size > 0 :
            neighbors.append(self.hole -1)

        if self.hole % self.size < self.size -1:
            neighbors.append(self.hole +1)

        if self.hole / self.size > 0:
            neighbors.append(self.hole - self.size)   

        if self.hole / self.size < self.size -1 :
            neighbors.append(self.hole + self.size)
            
        return neighbors

    def shuffle(self, count):


        for i in range (count):
            neighbors = self.legalNeighbors()
            who = random.choice(neighbors)
            self.swapCells(who)
            

    def takeTurn(self, n):


        if n in self.legalNeighbors():
            self.swapCells(n)
            

    def swapCells(self, n):


        self.positions[self.hole] = self.positions[n]
        self.positions[n]= -1
        self.hole = n
        

    def getCell(self, n):

        return self.positions[n]
    

    def getHole(self):

        return self.hole

    def solveStep(self):
        solver.solve(self.positions,self.hole)

         
def main():
    s= SliderGUI(4, 'smiley.gif')
    s.run()
main()
