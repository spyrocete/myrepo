import pygtk
import gtk
pygtk.require('2.0')
import random

WIDTH = 600
HEIGHT = 400
BOARD = WIDTH, HEIGHT

class SliderGUI:
    def __init__(self, BOARD, smiley) 
        self.createWindow()
        self.main_vbox()
        self.win.show_all()
        self.run()
   
    def run(self):
        gtk.main()
    
    def delete_event(self, widget, event, data=None):
        print "deleted event"
        return gtk.FALSE
    
    def destory(self, widget, data=None):
        gtk.main_quit()

        


    def createWindow(self):
        self.win = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
        self.win.set_title('Slider')
        self.win.show()
       # self.win.connect('destory', self.destory)
        self.win.connect('delete_event', self.delete_event)
  
    
    def main_vbox(self):
        vbox = gtk.VBox(homogeneous=True, spacing=0)    
        entry = gtk.Entry()
        button = gtk.Button('hi')
        button.connect('clicked', self.btn_handler)
        self.win.add(vbox)
        vbox.add(entry)
        vbox.add(button)

    def btn_handler(self, widget, data=None):
        print 'clicked'


def main():
    play = SliderGUI()

main()


