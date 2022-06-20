from graphics import*
from time import*
from button import*

class House:
    def __init__(self, win):
        sky=Rectangle(Point(0,0), Point(600,400))
        sky.setFill('sky blue')
        sky.draw(win)
        #sun
        sun=Circle(Point(500,100),(60))
        sun.setFill('goldenrod2')
        sun.draw(win)
        #moon
        moon=Circle(Point(500,500),(40))
        moon.setFill('light grey')
        #lawn
        lawn=Rectangle(Point(0,400), Point(600,600))
        lawn.setFill('green4')
        lawn.draw(win)


        

        #create square for house
        square=Rectangle(Point(190,270),Point(380,480))
        #make house yellow
        square.setFill('palevioletred1')
        #draw house
        square.draw(win)

        #triangle roof
        roof = Polygon(Point(285,125), Point(185,270), Point(385,270))
        roof.setFill('pink4')
        roof.draw(win)

        #square windows
        window1=Rectangle(Point(230,350),Point(270,310))
        window1.setFill('azure2')
        window1.draw(win)
        
        window2=Rectangle(Point(340,350),Point(300,310))
        window2.setFill('azure2')
        window2.draw(win)

        #rectangle for door
        door=Rectangle(Point(265,400),Point(310,480))
        door.setFill('sienna3')
        door.draw(win)

        #one point for doorknob
        doorknob=Point(300,440)
        doorknob.draw(win)
        #drawing stumps and leaves of trees around house
        stump1 = Rectangle(Point(90,450), Point(120,360))
        stump1.setFill('brown')
        stump1.draw(win)
        tree1 = Polygon(Point(105,100), Point(50,410), Point(160,410))
        tree1.setFill('light green')
        tree1.draw(win)
        stump2 = Rectangle(Point(470,500), Point(500,400))
        stump2.setFill("brown")
        stump2.draw(win)
        tree2 = Polygon(Point(480,200), Point(430,460), Point(540,460))
        tree2.setFill('light green')
        tree2.draw(win)

        #text prompt
        text1 = Text(Point(300,580),"It's a beautiful day!\n The sun is shining, the birds are chirping, there's not a cloud in the sky! (click)")
        text1.draw(win)
        text1.setStyle('bold')
        text1.setSize(16)
        #undraws when user clicks
        win.getMouse()
        text1.undraw()
        #new text appears after user click
        text2 = Text(Point(300,580), "Speaking of the sky, what's that?? (click)")
        text2.draw(win)
        text2.setStyle('bold')
        text2.setSize(16)
        #undraws text when user clicks
        win.getMouse()
        text2.undraw()
        #new text prompts another user click
        text3 = Text(Point(300,580), "Oh my!!! (click)")
        text3.draw(win)
        text3.setStyle('bold')
        text3.setSize(16)

        #drawing meteor as a grey circle that hits the house
        meteor = Circle(Point(100, -70), (115))
        meteor.setFill('grey')
        meteor.draw(win)
        win.getMouse()
        text3.undraw()

        #house is hit after user clicks
        text4 = Text(Point(300,580), "Was that a METEOR!?")
        text4.draw(win)
        text4.setStyle('bold')
        text4.setSize(16)
        #house and meteor catch on fire after impact
        #designing fire to be drawn
        fire = Polygon(Point(50,550), Point(30, 450), Point(50, 300), Point(80, 450), Point(90, 290), Point(130, 400), Point(150, 200), Point(190, 400), Point(230,290), Point(250, 450), Point(230, 550))
        fire2 = Polygon(Point(400,550), Point(380, 500), Point(400,450), Point(420,490), Point(450, 390), Point(470, 450), Point(490, 350), Point(520, 420), Point(540, 350), Point(570, 500), Point(540,550))
        
        #text prompting a user to pick which path they want to take
        text5 = Text(Point(300,580), "That was terrifying. Your house is DESTROYED! \n Let's try to find a new place to stay before sundown... \n Should we go through the forest or the mountains? (click)")
        text5.setStyle('bold')
        text5.setSize(14)
        
        for i in range(35):
            meteor.move(5,5)
            sleep(0.01)
            
            

        #animation for impact of meteor
        #meteor moves in and hits roof
        #roof detaches and house is ruined
        for i in range(35):
            meteor.move(5,9)
            
            roof.move(5,5)
            sleep(0.001)
            window1.move(-3,1)
            window2.move(-2,1)
            door.move(-4,1)
            doorknob.move(-3,1)
            square.move(-3,1)

        #drawing fire and changing colors in for loop for flickering effect           
        fire.draw(win)
        fire2.draw(win)
        for i in range(7):
            fire.setFill('gold2')
            sleep(0.05)
            fire.setFill('DarkOrange')
            sleep(0.05)
            fire.setFill('gold2')
            fire2.setFill('gold2')
            sleep(0.05)
            fire2.setFill('DarkOrange')
            sleep(0.05)
            fire2.setFill('gold2')
            
    
        text4.undraw()
        text5.draw(win)
        pt=win.getMouse()
        text5.undraw()
##    def isClicked(button, pt):
##        pt=win.getMouse()
##        x = pt.getX()
##        y = pt.getY()
##        p1 = button.getP1()
##        p2 = button.getP2()
##        if (min(p1.getX(),p2.getX()) <x<max(p1.getX(),p2.getX())):
##           if (min(p1.getY(),p2.getY()) <y<max(p1.getY(),p2.getY())):
##               return True
##        return False

    #function to test which button is clicked
    #if a button was clicked, return value 0 or 1
    #in the main module, different values run different results
    #run module runs function based on what the user clicked
    def run(self, win):
        #house = House(win)

                     
        A = Button(win, Point(240,550),110,40, "A: the forest path")
        B = Button(win, Point(360,550),110,40, "B: the mountain path")

        while (True):
            pt = win.getMouse()
            if A.clicked(pt) == True:
                
                return 0
            #pt = win.getMouse()
            elif B.clicked(pt):
                return 1
            
             


def main():
    house = House()
    
#main

  
        
    

        
        
    



    


