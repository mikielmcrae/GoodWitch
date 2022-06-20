from graphics import*
from button import*


class Bridge:
    def __init__(self, win):
        
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

        #drawing the bridge
        bridge = Polygon(Point(400,400), Point(200,400), Point(285,200),Point(315,200))
        bridge.setFill("brown")
        bridge.draw(win)

        #text prompt allowing user to pick where the want to go
        text1 = Text(Point(300,440), "After walking all night you come across a rickety old bridge going over a deep dark chasm. \nIt looks like a shortcut, \n but is potentially dangerous.You can walk around the chasm but it will take longer. Do you:\n A: Take the bridge, I'm a risk taker! \n B: Play it safe and walk around the chasm")
        text1.draw(win)
        text1.setSize(12)
        text1.setStyle("bold")

        #if user clicks A, they take the bridge
    def run(self, win):
        A = Button(win, Point(250,550),80,40, "A: Bridge")
        B = Button(win, Point(350, 550), 100,40, "B: Go around")
        while (True):
            pt = win.getMouse()
            if A.clicked(pt) == True:
                #returns value 0 for next function to be called in main module
                return 0
            #pt = win.getMouse()

            #if user clicks B, they go around bridge
            elif B.clicked(pt):
                #returns value 1 for next function to be called in main module
                return 1
        
    def main():
        bridge = Bridge()

    ##    win.getMouse()
    ##    win.close()
    

    
                    
