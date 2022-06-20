from graphics import*
from time import*
from time import sleep
from button import*


class Castle:
    def __init__(self,win):

        #sky
        sky=Rectangle(Point(0,0), Point(600,400))
        sky.setFill('sky blue')
        sky.draw(win)
        #sun
        sun=Circle(Point(500,100),(60))
        sun.setFill('goldenrod2')
        sun.draw(win)
        
        #lawn
        lawn = Rectangle(Point(0,350), Point(600,600))
        lawn.setFill('green4')
        lawn.draw(win)
        
        #moat around castle
        moat = Rectangle(Point(0, 470), Point(600, 500))
        moat.setFill('blue')
        moat.draw(win)

        #castle
        castle = Polygon(Point(150, 450), Point(150, 230), Point(175, 230), Point(175, 200), Point(225, 200), Point(225,230), Point(275, 230), Point(275, 200), Point (325, 200), Point(325, 230), Point(375, 230), Point(375, 200), Point(425, 200), Point(425, 230), Point(450, 230),Point(450, 450))
        castle.setFill('pink')
        castle.draw(win)

        #first pillar
        pillar1 = Rectangle(Point(100,170), Point(150, 450))
        pillar1.setFill('pink')
        pillar1.draw(win)

        #first window
        window1 = Polygon(Point(120, 200), Point(120, 185), Point(125, 180), Point(130, 185), Point(130,200))
        window1.setFill('black')
        window1.draw(win)

        #top of first pillar
        pillartop1 = Polygon(Point(125, 100), Point(90, 170), Point(160, 170))
        pillartop1.setFill('pink')
        pillartop1.draw(win)

        #second pillar
        pillar2 = Rectangle(Point(500, 170), Point(450, 450))
        pillar2.setFill('pink')
        pillar2.draw(win)

    ##    hedge1 = Rectangle(Point(90, 400), Point(170, 450))
    ##    hedge1.setFill('green')
    ##    hedge1.draw(win)

        #2nd window
        window2 = Polygon(Point(470, 200), Point(470, 185), Point(475,180), Point(480, 185), Point(480,200))
        window2.setFill('black')
        window2.draw(win)

        #top of second pillar
        pillartop2 = Polygon(Point(475, 100), Point(440, 170), Point(510, 170))
        pillartop2.setFill('pink')
        pillartop2.draw(win)

        #additional windows
        window3 = Polygon(Point(295, 270), Point(295, 255), Point(300, 250), Point(305, 255), Point(305, 270))
        window3.setFill('black')
        window3.draw(win)

        window4 = Polygon(Point(195,270), Point(195, 255), Point(200, 250), Point(205, 255), Point(205, 270))
        window4.setFill('black')
        window4.draw(win)

        window5 = Polygon(Point(395,270), Point(395, 255), Point(400, 250), Point(405, 255), Point(405, 270))
        window5.setFill('black')
        window5.draw(win)

        #castle door
        door = Rectangle(Point(285, 400), Point(315, 450))
        door.setFill('black')
        door.draw(win)

        #drawbridge
        drawbridge = Polygon(Point(285, 450), Point(315, 450), Point(325, 520), Point(275,520))
        drawbridge.setFill('brown')
        drawbridge.draw(win)

        
        #trees around castle
        stump1 = Rectangle(Point(45, 430), Point(60, 450))
        stump1.setFill('brown')
        stump1.draw(win)

        tree1 = Polygon(Point(55, 300), Point(30, 430), Point(75, 430))
        tree1.setFill('green')
        tree1.draw(win)

        stump2 = Rectangle(Point(540, 430), Point(555, 450))
        stump2.setFill('brown')
        stump2.draw(win)

        tree2 = Polygon(Point(550, 300), Point(525, 430), Point(570, 430))
        tree2.setFill('green')
        tree2.draw(win)

        #first text prompt
        text1 = Text(Point(300,560), "Finally, after days of navigating treacherous terrain in search \n of a new home, you stumble upon a castle. \n And what luck, it's for sale! (click)")
        text1.setSize(14)
        text1.draw(win)

        #next text prompting user to click for sale sign
        text2 = Text(Point(300, 560), "Click to purchase the castle!")
        text2.setSize(14)

        #congratulations!
        text3 = Text(Point(300, 100), "YOU WIN!!!")
        
        text4 = Text(Point(300,560), "Congratulations...\n(click)")
        text4.setSize(20)

        #pole of for sale sign                    
        pole = Rectangle(Point(498, 600), Point(507, 455))
        pole.setFill('brown')
        pole.draw(win)

        #drawing sign
        sign = Rectangle(Point(430,475), Point(570, 525))
        sign.setFill('white')
        sign.draw(win)

        #'for sale' label for sign
        label = Text(Point(500, 500), "FOR SALE")
        label.setFill('red')
        label.setSize(25)
        label.draw(win)


        #changing text prompts when user clicks
        
        win.getMouse()
        text1.undraw()
        text2.draw(win)

        #'sold' sign
        sign2 = Rectangle(Point(450, 520), Point(550, 550))
        sign2.setFill('red')
        
        label2 = Text(Point(500,535), "SOLD")
        label2.setFill("white")
        label2.setSize(20)
        
        
        
        #wait until user clicks to draw the 'sold' sign
    ##    pt = win.getMouse()
    ##    x = pt.getX()
    ##    y = pt.getY()
    ##    while win.getMouse():
    ##        if x>=430 and x<=570 and y>=475 and y<=525:
    ##                win.getMouse()
    ##                sign2.draw(win)
    ##                label2.draw(win)
    ##                text2.undraw()
    ##                text4.draw(win)
        win.getMouse()
        sign2.draw(win)
        label2.draw(win)
        text2.undraw()
        text4.draw(win)
        #change text prompts when user clicks
        win.getMouse()
        text4.undraw()
        text3.draw(win)
        #creating and activating quit button


        #flashing color effect for 'you win' text
        for i in range(10):
            text3.setSize(72)
            text3.setStyle("bold")
            text3.setFill('purple')
            sleep(0.10)
            text3.setFill('red')
        #creating and activating quit button
        quitButton = Button(win, Point(300, 570),100,40,"Quit")
        pt = win.getMouse()
        while not quitButton.clicked(pt):
            quitButton.activate()
            pt = win.getMouse()
        win.close()

    
        
def main():
    castle = Castle()
