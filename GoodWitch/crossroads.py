from graphics import*
from time import *
from button import*
from time import sleep

from gameover import Gameover
from forest2 import *

class Crossroads:
    

    def __init__(self, win):
        
        grass1 = Rectangle(Point(0,200), Point(600,600))
        grass1.setFill("palegreen3")
        grass1.draw(win)
        grass2 = Rectangle(Point(0, 225), Point(600,600))
        grass2.setFill("palegreen2")
        grass2.draw(win)
        grass3 = Rectangle(Point(0, 290), Point(600,600))
        grass3.setFill("palegreen1")
        grass3.draw(win)
        sky = Rectangle(Point(0,200), Point(600,0))
        sky.setFill("paleturquoise1")
        sky.draw(win)
        sun=Circle(Point(500,100),(55))
        sun.setFill('goldenrod1')
        sun.draw(win)
        road = Polygon(Point(75,600), Point(200,350), Point(50,200), Point(60,200), Point(300,330), Point(540,200), Point(550,200), Point(400,350), Point(525,600))
        road.setFill("gray")
        road.draw(win)
        pole = Rectangle(Point(295,100), Point(305,340))
        pole.setFill("gray90")
        pole.draw(win)
        sign1 = Polygon(Point(295,140), Point(260,140), Point(250,150), Point(260,160), Point(295,160))
        sign1.setFill('snow')
        sign1.draw(win)
        sign2 = Polygon(Point(305, 170), Point(340, 170), Point(350, 180), Point(340, 190), Point(305, 190))
        sign2.setFill('snow')
        sign2.draw(win)
        text = Text(Point(300,550), "You arrive at a crossroad. Click on one of the signs to choose which way you go. If you \n pick the wrong path you will surely die because all your supplies are gone. (click)")
        text.draw(win)
        text.setStyle('bold')
        text.setSize(13)
        

        def isClicked(button, pt):
            
            x = pt.getX()
            y = pt.getY()
            p1 = button.getP1()
            p2 = button.getP2()
            if (min(p1.getX(),p2.getX()) <x<max(p1.getX(),p2.getX())):
                if (min(p1.getY(),p2.getY()) <y<max(p1.getY(),p2.getY())):
                    return True
            return False


    ##    def clickSign():
    ##        pt = win.getMouse()
    ##        signs = 0
    ##        while signs < 3:
    ##            if isClicked(sign1, pt) ==True:
    ##                signs = signs + 1
    ##                gameover = Gameover(win)
    ##            elif isClicked(sign2, pt) == True:
    ##                signs = signs + 1


        pt = win.getMouse()
        x=pt.getX()
        y=pt.getY()
        signclicked = False
        while not signclicked:
            
            if x>= 250 and x<= 295 and y >=140 and y<=160:
                signclicked = True
 #               return 1
                gameover = Gameover(win)


            elif x>=305 and x<=350 and y>=170 and y<=190:
                signclicked = True
 #               return 0
 #               forest2 = Forest2(win)
            pt = win.getMouse()
                
 
                

            
    ##    def run(self, win):
    ##        pt = win.getMouse()
    ##        A = sign1
    ##        B = sign2
    ##        while (True):
    ##            pt = win.getMouse()
    ##            if A.clicked(pt) == True:
    ##                
    ##                return 0
    ##            #pt = win.getMouse()
    ##            elif B.clicked(pt):
    ##                return 1
    ##    def sign():
    ##        if result == 0:
    ##            gameover = Gameover(win)
    ##            result = gameover.run(win)
    ##        elif result ==1 :
                

def main():
    crossroads = Crossroads()
    
