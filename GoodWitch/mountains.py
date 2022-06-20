
from graphics import *
from time import *
from random import *
from button import*

class Mountains:
    #mountain class
    def __init__(self, win):

        #drawing different layers of sky with different colors
        sky=Rectangle(Point(0,0), Point(610,370))
        sky.setFill('thistle4')
        sky.draw(win)
        sky2=Rectangle(Point(0,40), Point(610,100))
        sky2.setFill('thistle3')
        sky2.draw(win)
        sky3=Rectangle(Point(0,100), Point(610,200))
        sky3.setFill('thistle2')
        sky3.draw(win)
        sky4=Rectangle(Point(0,200), Point(610,600))
        sky4.setFill('thistle1')
        sky4.draw(win)

    
        
        
        
        #drawing sun and moon
        sun = Circle(Point(500,120),60)
        sun.setFill("goldenrod2")
        sun.draw(win)
        moon = Circle(Point(300,-70),60)
        moon.setFill("ghostwhite")
        moon.draw(win)

        #drawing grey mountains with snow on top
        mountain4 = Polygon(Point(50,50), Point(-237, 610), Point(350,610))
        mountain4.setFill("grey")
        mountain4.draw(win)
        snow4 = Polygon(Point(50,50), Point(-10, 160), Point(20, 130), Point(30, 160), Point(50, 130), Point(70, 160), Point(80, 130),Point(110, 160))
        snow4.setFill('snow')
        snow4.draw(win)
                            
        mountain3 = Polygon(Point(300,100), Point(100,610), Point(500,610))
        mountain3.setFill("grey")
        mountain3.draw(win)
        snow3 = Polygon (Point(300,80), Point(248,230), Point(280, 200), Point(290, 230), Point(310, 200),Point(352,230))
        snow3.setFill("snow")
        snow3.draw(win)
                            
        mountain1 = Polygon(Point(150,150), Point(-50,610), Point(350,610))
        mountain1.setFill("grey")
        mountain1.draw(win)
        snow1 = Polygon(Point(150,140), Point(105,250), Point(130, 230), Point(140, 250), Point(165, 230), Point(193, 250))
        snow1.setFill("snow")
        snow1.draw(win)
        mountain2 = Polygon(Point(480,220), Point(680,610), Point(270,610))
        mountain2.setFill("grey")
        mountain2.draw(win)
        snow2 = Polygon(Point(480,210), Point(425, 320), Point(450, 300), Point(460, 320), Point(480,300), Point(500, 320), Point(510, 300), Point(533,320))
        snow2.setFill("snow")
        snow2.draw(win)

        #when user clicks, sun sets and the scene turns to night
        win.getMouse()
        text1 = Text(Point(300,580),"It's starting to get dark out...")
        text1.draw(win)
        text1.setSize(16)
        text1.setStyle("bold")
        #text undraws when user clicks
        win.getMouse()
        text1.undraw()

        #animation for sunset
        for i in range(35):
            #move 5 pixels down and 5 pixels over at a time
            sun.move(5,5)
            moon.move(5,5)
            #start from the initial blue-ish (color_rgb(180, 180, 247)) color (set above)
            #for loop allows the colors to gradually fade to black which is color_rgb(0,0,0)
            sky.setFill(color_rgb(180-5*i,180-5*i,245-7*i))
            sky2.setFill(color_rgb(180-5*i,180-5*i,245-7*i))
            sky3.setFill(color_rgb(180-5*i,180-5*i,245-7*i))
            sky4.setFill(color_rgb(180-5*i,180-5*i,245-7*i))
            #slowing animation down to look more realistic
            sleep(.1) 
            

        #after sunset, create stars
        star = [] #start with an empty list of stars
        for i in range(100):
            #generate random x and y values for a Point object
            #and add it to the list of stars
            star.append(Point(randrange(0,600),randrange(0,300)))
            #draws 100 white stars
            star[i].setFill("white")
            star[i].draw(win)

        #text prompting user to pick whether they want to stay or keep going
        text2 = Text(Point(300,470), "Do you: \n A: Stop and rest for the night. \n B: Keep going, you're in a hurry.")
        text2.draw(win)
        text2.setSize(16)
        text2.setStyle("bold")

        #run function returns a value 0 or 1 depending on what the user clicks
        #in the main module, the value of 0 calls the function that corresponds with button A
        #value of 1 calls the function corresponding with option B
    def run(self, win):
        pt = win.getMouse()
        A = Button(win, Point(250,550),80,40, "A: Stay")
        B = Button(win, Point(350, 550), 80,40, "B: Keep Going")
        while (True):
            pt = win.getMouse()
            if A.clicked(pt) == True:
                
                return 0
            
            elif B.clicked(pt):
                return 1
        
def main():
    mountains = Mountains()


