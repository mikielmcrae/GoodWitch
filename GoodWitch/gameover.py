
from graphics import*
import time
from time import sleep
from button import *

class Gameover():
    
    def isClicked(button, pt):
        
        #isClicked function to return true if buttons were clicked
        #setting x and y values for user's click
        pt=win.getMouse()
        x = pt.getX()
        y = pt.getY()
        p1 = button.getP1()
        p2 = button.getP2()
        #testing if mouse click was in button
        if (min(p1.getX(),p2.getX()) <x<max(p1.getX(),p2.getX())):
            if (min(p1.getY(),p2.getY()) <y<max(p1.getY(),p2.getY())):
                return True
        return False
    def __init__(self, win):

        #drawing black background in graphic window
        background = Rectangle(Point(0,600), Point(600,0))
        background.setFill("black")
        background.draw(win)

        #drawing game over text
        gameOver = Text(Point(300,300),"You Died")
        gameOver.draw(win)
        #layering text
        gameOver2 = Text(Point(303,302), "You Died")
        gameOver2.draw(win)

                         

        #flashing colors for game over text
        #setting font to times new roman
        for i in range(20):
            gameOver.setFill("red")
            gameOver.setSize(72)
            gameOver.setFace("times roman")
            sleep(0.01)
            gameOver.setFill("white")
            sleep(0.01)
            gameOver2.setFill("white")
            gameOver2.setSize(72)
            gameOver2.setFace("times roman")
            sleep(0.01)
            gameOver2.setFill("red")
            sleep(0.01)

##    def run(self,win):
##        
##        restart=Button(win,Point(360,550), 110, 40, "Restart")
##        while (True):
##          pt=win.getMouse()
##          if restart.clicked(pt) == True:
##              return 0
            
            
##        quitButton = Button(win, Point(300, 570),100,40,"Quit")
##        pt = win.getMouse()
##        while not quitButton.clicked(pt):
##            quitButton.activate()
##            pt = win.getMouse()
##        win.close()

      

def main():
    gameover = Gameover()

  ##gameover()

