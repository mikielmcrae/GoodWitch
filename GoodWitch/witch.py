from graphics import*


class Witch:
    def __init__(self,win):
        #drawing green witch with orange hair

        #orange hair
        hair = Rectangle(Point(240, 170),Point(360,350))
        hair.setFill("darkorange1")
        hair.draw(win)

        #neck
        neck = Rectangle(Point(275,270), Point(325,230))
        neck.setFill("olivedrab2")
        neck.draw(win)

        #head
        head = Circle(Point(300,200),(50))
        head.setFill("olivedrab2")
        head.draw(win)

        #adding bangs to hair
        #needs to be drawn after head to show up on top
        bangs = Polygon(Point(290,180), Point(350, 180), Point(358, 200))
        bangs.setFill("darkorange1")
        bangs.draw(win)

        #triangular witch hat
        hat = Polygon(Point(300,50),Point(240,175), Point(360,175))
        hat.setFill("gray14")
        hat.draw(win)
        brim = Rectangle(Point(225,170),Point(375, 180))
        brim.setFill("gray14")
        brim.draw(win)

        #black dress
        dress = Polygon(Point(275,270), Point(325,270), Point(375, 310), Point(375,600), Point(225,600), Point(225,310))
        dress.setFill("gray14")
        dress.draw(win)

        #scary pink eyes
        eye1 = Circle(Point(278,200),(10))
        eye1.setFill("pink")
        eye1.draw(win)
        
        eye2 = Circle(Point(322,200),(10))
        eye2.setFill("pink")
        eye2.draw(win)
        
        pupil1 = Circle(Point(278,200),(3))
        pupil1.setFill("black")
        pupil1.draw(win)
        pupil2 = Circle(Point(322,200),(3))
        pupil2.setFill("black")
        pupil2.draw(win)

        #nose
        nose = Circle(Point(300,215),(7))
        nose.setFill("olivedrab2")
        nose.draw(win)

        #first arm, hand and thumb
        arm1 = Rectangle(Point(215,310), Point(245,500))
        arm1.setFill("gray14")
        arm1.draw(win)
        hand1 = Circle(Point(230,510),(20))
        hand1.setFill("olivedrab2")
        hand1.draw(win)
        thumb1 = Circle(Point(242,510),(8))
        thumb1.setFill("olivedrab2")
        thumb1.draw(win)
        #second arm, hand and thumb
        arm2 = Rectangle(Point(355,310), Point(385,500))
        arm2.setFill("gray14")
        arm2.draw(win)
        hand2 = Circle(Point(370,510),(20))
        hand2.setFill("olivedrab2")
        hand2.draw(win)
        thumb2 = Circle(Point(358,510),(8))
        thumb2.setFill("olivedrab2")
        thumb2.draw(win)

        #small freckles on her face
        dot1 = Point(272,220)
        dot1.setFill('olivedrab4')
        dot1.draw(win)
        dot2 = Point(277,216)
        dot2.setFill('olivedrab4')
        dot2.draw(win)
        dot3 = Point(282,220)
        dot3.setFill('olivedrab4')
        dot3.draw(win)

        #more freckles
        dot4 = Point(316,220)
        dot4.setFill('olivedrab')
        dot4.draw(win)
        dot5 = Point(321,216)
        dot5.setFill('olivedrab')
        dot5.draw(win)
        dot6 = Point(326,220)
        dot6.setFill('olivedrab')
        dot6.draw(win)
def main():
    witch = Witch()
                     
    
    
