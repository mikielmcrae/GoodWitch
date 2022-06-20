from graphics import *
from goblin import Goblin
from button import*
from gameover import Gameover
from castle import Castle

class Forest2:
        
        
        def __init__(self,win):
                
                
 #               win = GraphWin("Goblin",600,600)
                lawn = Rectangle(Point(0,620),Point(620,300))
                lawn.setFill("green4")
                lawn.draw(win)
                
                #blue-ish sky
                sky = Rectangle(Point(620,300),Point(0,0))
                sky.setFill(color_rgb(180,180,245))
                sky.draw(win)

                #yellow sun
                sun = Circle(Point(500,100),60)
                sun.setFill("yellow")
                sun.draw(win)

                stump1 = Rectangle(Point(110,400), Point(140,360))
                stump1.setFill('brown')
                stump1.draw(win)
                bottomLeaves1 = Polygon(Point(40,360), Point(210,360), Point(125,200))
                bottomLeaves1.setFill('light green')
                bottomLeaves1.draw(win)
                midLeaves1 = Polygon(Point(50,320), Point(200, 320), Point(125,190))
                midLeaves1.setFill('light green')
                midLeaves1.draw(win)
                topLeaves1 = Polygon(Point(60, 280), Point(190, 280), Point(125, 180))
                topLeaves1.setFill('light green')
                topLeaves1.draw(win)
                stump2 = Rectangle(Point(290,400), Point(320, 360))
                stump2.setFill("brown")
                stump2.draw(win)
                bottomLeaves2 = Polygon(Point(305,220), Point(220,360), Point(390,360))
                bottomLeaves2.setFill('light green')
                bottomLeaves2.draw(win)
                midLeaves2 = Polygon(Point(305, 200), Point(230,320), Point(380,320))
                midLeaves2.setFill('light green')
                midLeaves2.draw(win)
                topLeaves2 = Polygon(Point(305, 180), Point(240, 280), Point(370, 280))
                topLeaves2.setFill('light green')
                topLeaves2.draw(win)
                
                stump3 = Rectangle(Point(470,400), Point(500,360))
                stump3.setFill("brown")
                stump3.draw(win)
                bottomLeaves3 = Polygon(Point(480,220), Point(400,360), Point(560,360))
                bottomLeaves3.setFill('light green')
                bottomLeaves3.draw(win)
                midLeaves3 = Polygon(Point(480,200), Point(410,320), Point(550,320))
                midLeaves3.setFill('light green')
                midLeaves3.draw(win)
                topLeaves3 = Polygon(Point(480,180), Point(420, 280), Point(540, 280))
                topLeaves3.setFill('light green')
                topLeaves3.draw(win)
                goblin = Goblin(win)
                text1 = Text(Point(300,550), "You found the goblin! He gives you your stuff back for being so persistent(click)")
                text1.draw(win)
                text1.setStyle('bold')
                text1.setSize(15)
                win.getMouse()
                text1.undraw()
                text2 = Text(Point(300,500), "The goblin points out which way to go, but he doesn't seem very trustworthy...\n Do you trust him?(click)")
                text2.draw(win)
                text2.setStyle('bold')
                text2.setSize(15)
                

        

        
        
        
              
        def run(self, win):
                
                pt = win.getMouse()
                A = Button(win, Point(250,550),80,40, "A: Yes")
                B = Button(win, Point(350, 550), 80,40, "B: No")
                while (True):
                    pt = win.getMouse()
                    if A.clicked(pt) == True:
                            
 #                          return 0
                            gameover = Gameover(win)
                                
                    #pt = win.getMouse()
                    elif B.clicked(pt):
 #                          return 1
                            castle = Castle(win)
                   # if result == 0:
 #                       gameover = Gameover(win)
 #                   elif result == 1:
 #                       pass
                
       
def main():
    forest2 = Forest2()

