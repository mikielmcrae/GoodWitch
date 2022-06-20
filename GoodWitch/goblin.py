from graphics import*

class Goblin:
    def __init__(self, win):
    
        body = Rectangle(Point(200,200),Point(400,400))
        body.setFill("lightgreen")
        body.draw(win)

        sash = Polygon(Point(200,200), Point(230,200), Point(410,360), Point(380,360))
        sash.setFill("tan4")
        sash.draw(win)
        sashDesign1 = Circle(Point(250, 232),(8))
        sashDesign1.setFill("gray")
        sashDesign1.draw(win)
        
        sashDesign2 = Circle(Point(300, 275),(8))
        sashDesign2.setFill("gray")
        sashDesign2.draw(win)
        sashDesign3 = Circle(Point(350, 320),(8))
        sashDesign3.setFill("gray")
        sashDesign3.draw(win)
        
        ears = Polygon(Point(200, 170), Point(400,170), Point(300,200))
        ears.setFill("lightgreen")
        ears.draw(win)
        
        head = Circle(Point(300,190),(50))
        head.setFill("lightgreen")
        head.draw(win)
        eye1 = Circle(Point(275,190),(13))
        eye1.setFill("yellow")
        eye1.draw(win)
        pupil1 = Circle(Point(275,190),(5))
        pupil1.setFill("black")
        pupil1.draw(win)
        eye2 = Circle(Point(325,190),(13))
        eye2.setFill("yellow")
        eye2.draw(win)
        pupil2 = Circle(Point(325,190),(5))
        pupil2.setFill("black")
        pupil2.draw(win)
        nose = Circle(Point(300,200),(10))
        nose.setFill("lightgreen")
        nose.draw(win)
        
        
        
        leg1 = Rectangle(Point(345,400), Point(380,470))
        leg1.setFill("lightgreen")
        leg1.draw(win)
        leg2 = Rectangle(Point(220,400), Point(255,470))
        leg2.setFill("lightgreen")
        leg2.draw(win)
        foot1 = Rectangle(Point(345,470), Point(400,450))
        foot1.setFill("lightgreen")
        foot1.draw(win)
        
        foot2 = Rectangle(Point(255,470), Point(200,450))
        foot2.setFill("lightgreen")
        foot2.draw(win)
        
        pants = Polygon(Point(200,350), Point(400,350), Point(400,430), Point(325, 430), Point(325,400), Point(275,400), Point(275, 430), Point(200,430))
        pants.setFill("tan3")
        pants.draw(win)
        belt = Rectangle(Point(200, 330),Point(400,360))
        belt.setFill("tan4")
        belt.draw(win)
        buckle = Rectangle(Point(275,323),Point(325,367))
        buckle.setFill("gray")
        buckle.draw(win)
        bucklehole = Rectangle(Point(285,330), Point(315,360))
        bucklehole.setFill("tan4")
        bucklehole.draw(win)

        arm1 = Rectangle(Point(190,210), Point(220,370))
        arm1.setFill("lightgreen")
        arm1.draw(win)
        arm2 = Rectangle(Point(380, 210), Point(410,370))
        arm2.setFill("lightgreen")
        arm2.draw(win)
        hand1 = Circle(Point(205,385),(20))
        hand1.setFill("lightgreen")
        hand1.draw(win)
        thumb1 = Circle(Point(220,385),(8))
        thumb1.setFill("lightgreen")
        thumb1.draw(win)
        hand2 = Circle(Point(395,385),(20))
        hand2.setFill("lightgreen")
        hand2.draw(win)
        thumb2 = Circle(Point(380,385),(8))
        thumb2.setFill("lightgreen")
        thumb2.draw(win)
    
    
    def main():
        goblin = Goblin()
    
    
