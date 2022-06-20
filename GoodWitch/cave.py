#cave
from graphics import *
from random import *
from witch import Witch
from castle import Castle
from gameover import Gameover
from button import*
from time import sleep


class Cave:
        def __init__(self,win):
                
#def witch():
        #drawing sky
        #win = GraphWin('witch',600,600)
                sky=Rectangle(Point(620, 600), Point(0,0))
                sky.setFill("black")
                sky.draw(win)

                #grass
                snow = Rectangle(Point(0,600), Point(620,300))
                snow.setFill('snow')
                snow.draw(win)
                snow2 = Rectangle(Point(0,350), Point(620,300))
                snow2.setFill('gray85')
                snow2.draw(win)
                snow3 = Rectangle(Point(0,450), Point(620,350))
                snow3.setFill('gray95')
                snow3.draw(win)

                #mountain behind cave
                mountain = Polygon(Point(-50, 300), Point(400,300), Point(100, -500))
                mountain.setFill(color_rgb(100,100,100))
                mountain.draw(win)

                #cave
                cave = Polygon(Point(40,300), Point(290, 300), Point(220,100))
                cave.setFill(color_rgb(125,125,125))
                cave.draw(win)

                #entrance to cave in front
                entrance = Polygon(Point(120,300), Point(250,300), Point(215,180))
                entrance.setFill(color_rgb(40,40,40))
                entrance.draw(win)

                text = Text(Point(300,550), "You spot a cave that looks like a suitable shelter for the night\n (click)")
                text.setFill('red')
                text.setStyle('bold')
                text.draw(win)
                win.getMouse()
                text.undraw()
                

                        
                
                witch = Witch(win)
                text2 = Text(Point(300,550), "Suddenly a witch comes out of the cave!\n She offers to point the way to a house she recently saw go on the market.\n Do you choose to trust her?(click)")
                text2.setFill("red")
                text2.setStyle('bold')
                text2.draw(win)
                win.getMouse()
                text2.undraw()
        

##                text3 = Text(Point(300,550), "She offers to point the way to a house she recently saw go on the market.\n Do you choose to trust her?")
##                text3.setFill("red")
##                text3.draw(win)
##                win.getMouse()
##                text3.undraw()


        def run(self, win):

                #pt = win.getMouse()
                A = Button(win, Point(250,550),80,40, "A: Yes")
                B = Button(win, Point(350, 550), 80,40, "B: No")
                while (True):
                    pt = win.getMouse()
                    if A.clicked(pt) == True:
                            text4 = Text(Point(300,500), "You're a little apprehensive, but you choose to trust the witch")
                            text4.setFill('red')
                            text4.setStyle('bold')
                            text4.draw(win)
                            sleep(3)
                            castle = Castle(win)
                            
                    
                        
                        
                    
                    elif B.clicked(pt):
                            text5 = Text(Point(300,500), "You go in the opposite direction that the witch tells you to go. You fall off a cliff")
                            text5.draw(win)
                            text5.setFill('red')
                            text5.setStyle('bold')
                            sleep(3)
                            return 1
 #                           gameover = Gameover(win)
                        
##witch()
##
def main():
    cave = Cave()

             
