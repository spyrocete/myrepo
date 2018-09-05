import pygtk
import gtk

# Basic flow chart #
##Window (main_win)
##    gtk.VBox (main_vbox)
##            gtk.MenuBar(menu_bar)
##                    gtk.Menu (menu)
##                            gtk.MenuItem (menu_item)
##                                    gtk.MenuItem
##                                    gtk.MenuItem
##                                    gtk.MenuItem
##            gtk.Table (game_table)
##                    gtk.Button (btn)
##                            gtk.Image (img)
##                    gtk.Button
##                            gtk.Image
##                    more buttons
##                            more images


class SliderGUI:
    def __init__(self, size, imagefilename):
        ## Initialize Variables ##
        self.size = size
        self.pixbufs=[]
        self.images = []
        self.buttons = []

        # call inorder to create the User interface #
        self.readImageFile(imagefilename)
        # calculate cell height and width #
        self.cellheight = self.full_height / size
        self.cellwidth = self.full_width / size

        
        self.createWindow()        
        self.createBtnImages()
        self.createMenu()
        self.createGame()
        
    # display all things in the window #
        self.window.show_all()


    def readImageFile(self, imagefilename):
        # Will read image from the file and store it as a large pixbuf #
        image = gtk.Image()
        image.set_from_file(imagefilename)

        
        self.full_pixbuf = image.get_pixbuf()
        self.full_height = self.full_pixbuf.get_height()
        self.full_width = self.full_pixbuf.get_width()

        
        

        
    def createWindow(self):
        # responsible for the creation of the window and main vbox #
        self.window = gtk.Window()
        self.window.set_title("Slider, oooooh yeah!")
        self.window.connect('delete_event', self.delete_handler, None)
        self.window.connect('destroy', self.destroy_handler, None)
        self.window.resize(self.full_width, self.full_height)
        self.window.show_all()
        self.window.set_resizable(False)
        self.vbox = gtk.VBox()
        self.window.add(self.vbox)
        


        
    def createBtnImages(self):
        # a helper method that breaks up the large pixbuf into smaller #
        # sub pixbufs for use in the buttons later. #
        for xval in range (0, self.full_width, self.cellwidth):
            for yval in range (0, self.full_height, self.cellheight):
                subpixbuf = self.full_pixbuf.subpixbuf(xval, yval,self.cellwidth, self.cellheight)
                self.pixbufs.append(subpixbuf)

##
    def createMenuItem(self, title, handler):
       # will aid in the creation of menuItems for the menu #
        item = gtk.MenuItem(title)
        item.connect("activate", handler, None)
        self.menu.append(item)
##
    def createMenu(self):
        # will create the menubar, menu and menu Items, then pack them #
        # into the main vbox #
        
        
        self.menu = gtk.Menu()
        self.createMenuItem("Start Over", self.restart_handler)
        self.createMenuItem("Solve", self.solve_handler)
        self.createMenuItem("Quit", self.destroy_handler)


        self.root_menu = gtk.MenuItem('Game')
        self.root_menu.set_submenu(self.menu)


        self.Menu_Bar = gtk.MenuBar()
        self.Menu_Bar.append(self.root_menu)
        self.vbox.pack_start(self.Menu_Bar)

        
##
    def createGame(self):
        # will create the table, and thje buttons and put the buttons in #
        # the table, assign images to the buttons, pack the table into the #
        # main vbox #
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


                
                
                
                
                
                
##
    def delete_handler(self, widget, event, data):
        # will handle the window delete event #
        return False
##        
    def destroy_handler(self, widget, data=None):
        #will handle destroy signals to quit the main gtk loop #
        gtk.main_quit()


        
##
    def restart_handler(self, widget, data):
        # will handle the signal to restart the game. This will be a stub #
        # method until part 2 is developed #
        print 'restart'

    def solve_handler(self, widget, data):
        # will handle the signal to solve the game. This will be a stub #
        # method until you test part 2 #
        print 'solve'
##
    def clicked_handler(self, widget, data):
        # will handle button click signals. This will be a stub method #
        # until part 2 is developed #
        print 'clicked'

    def run(self):
         # Will start the main gtk loop #
         gtk.main()



##         Part 2 SliderLogic Implementation        ##

class SliderLogic:
    
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


         
def main():
    s= SliderGUI(4, 'smiley.gif')
    s.run()
main()
