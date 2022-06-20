from buildfire import Buildfire
from graphics import *
from time import *
from random import *
from button import*

#class forest:
class Forest:
    def __init__(self, win):
        
        #green lawn
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
        #moon
        moon = Circle(Point(300,-70),60)
        moon.setFill("ghostwhite")
        moon.draw(win)
        

        #trees
    ##    stump1 = Rectangle(Point(110,400), Point(140,360))
    ##    stump1.setFill('brown')
    ##    stump1.draw(window)
    ##    tree1 = Polygon(Point(125,100), Point(70,360), Point(180,360))
    ##    tree1.setFill('light green')
    ##    tree1.draw(window)
    ##
    ##    stump2 = Rectangle(Point(290,400), Point(320, 360))
    ##    stump2.setFill("brown")
    ##    stump2.draw(window)
    ##    tree2 = Polygon(Point(300,100), Point(250,360), Point(360,360))
    ##    tree2.setFill('light green')
    ##    tree2.draw(window)
    ##    
    ##    stump3 = Rectangle(Point(470,400), Point(500,360))
    ##    stump3.setFill("brown")
    ##    stump3.draw(window)
    ##    tree3 = Polygon(Point(480,100), Point(430,360), Point(540,360))
    ##    tree3.setFill('light green')
    ##    tree3.draw(window)

        #stump for first tree
        stump1 = Rectangle(Point(110,400), Point(140,360))
        stump1.setFill('brown')
        stump1.draw(win)
        #bottom triangle of leaves
        bottomLeaves1 = Polygon(Point(40,360), Point(210,360), Point(125,200))
        bottomLeaves1.setFill('light green')
        bottomLeaves1.draw(win)
        #middle triangle
        midLeaves1 = Polygon(Point(50,320), Point(200, 320), Point(125,190))
        midLeaves1.setFill('light green')
        midLeaves1.draw(win)
        #top triangle
        topLeaves1 = Polygon(Point(60, 280), Point(190, 280), Point(125, 180))
        topLeaves1.setFill('light green')
        topLeaves1.draw(win)
                             
        #stump of middle tree
        stump2 = Rectangle(Point(290,400), Point(320, 360))
        stump2.setFill("brown")
        stump2.draw(win)
        #bottom, middle and top triangles for leaves
        bottomLeaves2 = Polygon(Point(305,220), Point(220,360), Point(390,360))
        bottomLeaves2.setFill('light green')
        bottomLeaves2.draw(win)
        midLeaves2 = Polygon(Point(305, 200), Point(230,320), Point(380,320))
        midLeaves2.setFill('light green')
        midLeaves2.draw(win)
        topLeaves2 = Polygon(Point(305, 180), Point(240, 280), Point(370, 280))
        topLeaves2.setFill('light green')
        topLeaves2.draw(win)

        #3rd tree stump
        stump3 = Rectangle(Point(470,400), Point(500,360))
        stump3.setFill("brown")
        stump3.draw(win)
        #triangles for 3rd tree leaves
        bottomLeaves3 = Polygon(Point(480,220), Point(400,360), Point(560,360))
        bottomLeaves3.setFill('light green')
        bottomLeaves3.draw(win)
        midLeaves3 = Polygon(Point(480,200), Point(410,320), Point(550,320))
        midLeaves3.setFill('light green')
        midLeaves3.draw(win)
        topLeaves3 = Polygon(Point(480,180), Point(420, 280), Point(540, 280))
        topLeaves3.setFill('light green')
        topLeaves3.draw(win)

        #text before scene turns to night
        text1 = Text(Point(300,580),"It's starting to get dark out... (click)")
        text1.draw(win)
        text1.setSize(16)
        text1.setStyle("bold")
        #undraw text when user clicks
        win.getMouse()
        text1.undraw()
         
        

        
        
        #animate sunset
        for i in range(35):
            sun.move(5,5)
            moon.move(5,5)#move 5 pixels down and 5 pixels over at at ime
            #start from the initial blue-ish (color_rgb(180, 180, 247)) color (set above)
            sky.setFill(color_rgb(180-5*i,180-5*i,245-7*i)) #and fade down to color_rgb(0,0,0)
            sleep(.1) #slow the animation down so it looks good
            
        #after sunset, create stars
        star = [] #start with an empty list of stars
        for i in range(200):
            #generate random x and y values for a Point object
            #and add it to the list of stars
            star.append(Point(randrange(0,600),randrange(0,300)))
            star[i].setFill("white")
            star[i].draw(win)


        t2 = Text(Point(300,580), "You've had a long day. You're getting sleepy...(click)")
        t2.setSize(16)
        t2.setStyle('bold')
        t2.draw(win)
        pt=win.getMouse()
        t2.undraw()
 
#        buildfire = Buildfire(win)
        
        
        
        

        #options for the user to be displayed along with buttons

        
    def run(self, win):
        text2 = Text(Point(300,470), "Do you: \n A: Stop and rest for the night. \n B: Keep going, you're in a hurry.(click)")
        text2.draw(win)
        text2.setSize(16)
        text2.setStyle("bold")

        pt = win.getMouse()
        A = Button(win, Point(250,550),80,40, "A: Stay")
        B = Button(win, Point(350, 550), 80,40, "B: Keep Going")
        while (True):
            pt = win.getMouse()
            if A.clicked(pt) == True:
                return 0
 
                text2.undraw()
 #               A.undraw()
 #               B.undraw()
 #               buildfire = Buildfire(win)
               
                
            #pt = win.getMouse()
            elif B.clicked(pt):
                return 1

        
        #pause and wait for mouse click before closing window

def main():
    forest = Forest()

#main()
