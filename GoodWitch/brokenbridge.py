from graphics import*
from button import*
from gameover import Gameover


class Brokenbridge:
    def __init__(self,win):
    
        
        
        #drawing sky
        sky= Rectangle(Point(0,0), Point(600,500))
        sky.setFill(color_rgb(180,180,245))
        sky.draw(win)
        #sun
        sun=Circle(Point(500,100),(55))
        sun.setFill('goldenrod1')
        sun.draw(win)
        #grass
        grass=Rectangle(Point(0,200), Point(600,600))
        grass.setFill('SeaGreen2')
        grass.draw(win)

        #abyss on either side of bridge
        abyss1=Rectangle(Point(0,200), Point(600,400))
        abyss1.setFill('black')
        abyss1.draw(win)
        abyss2=Rectangle(Point(0,200), Point(600,250))
        abyss2.setFill('gray25')
        abyss2.draw(win)
        abyss3=Rectangle(Point(0,220), Point(600,250))
        abyss3.setFill('gray17')
        abyss3.draw(win)
        abyss4=Rectangle(Point(0,300), Point(600,250))
        abyss4.setFill('gray10')
        abyss4.draw(win)
        grass2=grass=Rectangle(Point(0,200), Point(600,195))
        grass2.setFill('SeaGreen3')
        grass2.draw(win)
    ##    abyss5=Rectangle(Point(200,400), Point(600,250))
    ##    abyss5.setFill('gray6')
    ##    abyss5.draw(win)
        #drawing bridge stretching out into the distance
        bridge = Polygon(Point(400,400), Point(200,400), Point(285,200),Point(315,200))
        bridge.setFill("brown")
        bridge.draw(win)

        #text prompt to tell user that it's Game Over when they cross the bridge
        text = Text(Point(300,440), "You step onto the bridge. You're nearly halfway across when you suddenly hear a loud snap. \n Before you can even process what you've heard you realize that you're falling(click)")
        text.draw(win)
        text.setStyle('bold')
        #undraw text and bridge when user clicks
        win.getMouse()
        text.undraw()
        bridge.undraw()
        text1 = Text(Point(300,440), "")
        text1.draw(win)
        
        text1.setSize(12)
        text1.setStyle("bold")

        #game over screen
        gameover = Gameover(win)
    
   
def main():
    brokenbridge = Brokenbridge()

