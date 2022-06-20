from crossroads import Crossroads
from graphics import *
from time import *
from random import *
from button import*
from time import sleep

class Buildfire:
   def __init__(self, win):
      


      sky = Rectangle(Point(620,600),Point(0,0))
      sky.setFill('black')
      sky.draw(win)

      sun = Circle(Point(750,100), 60)
      sun.setFill('yellow')
      sun.draw(win)
      
      lawn = Rectangle(Point(0,620),Point(620,300))
      lawn.setFill(color_rgb(0,153,0))
      lawn.draw(win)


      moon = Circle(Point(500,100),60)
      moon.setFill(color_rgb(255,255,255))
      moon.draw(win)

      #trees
      stump1 = Rectangle(Point(110,400), Point(140,360))
      stump1.setFill('brown')

      bottomLeaves1 = Polygon(Point(40,360), Point(210,360), Point(125,200))
      bottomLeaves1.setFill('light green')

      midLeaves1 = Polygon(Point(50,320), Point(200, 320), Point(125,190))
      midLeaves1.setFill('light green')

      topLeaves1 = Polygon(Point(60, 280), Point(190, 280), Point(125, 180))
      topLeaves1.setFill('light green')

      stump2 = Rectangle(Point(290,400), Point(320, 360))
      stump2.setFill("brown")

      bottomLeaves2 = Polygon(Point(305,220), Point(220,360), Point(390,360))
      bottomLeaves2.setFill('light green')

      midLeaves2 = Polygon(Point(305, 200), Point(230,320), Point(380,320))
      midLeaves2.setFill('light green')

      topLeaves2 = Polygon(Point(305, 180), Point(240, 280), Point(370, 280))
      topLeaves2.setFill('light green')


      stump3 = Rectangle(Point(470,400), Point(500,360))
      stump3.setFill("brown")

      bottomLeaves3 = Polygon(Point(480,220), Point(400,360), Point(560,360))
      bottomLeaves3.setFill('light green')

      midLeaves3 = Polygon(Point(480,200), Point(410,320), Point(550,320))
      midLeaves3.setFill('light green')

      topLeaves3 = Polygon(Point(480,180), Point(420, 280), Point(540, 280))
      topLeaves3.setFill('light green')


      star = [] #start with an empty list of stars
      for i in range(100):
           #generate random x and y values for a Point object
           #and add it to the list of stars
          x=randrange(0,600)
          y=randrange(0,300)

          star.append(Point(x,y))
          star[i].setFill("white")
          sleep(0.0000001)
          star[i].draw(win)


          
          

      stump1.draw(win)
      bottomLeaves1.draw(win)
      midLeaves1.draw(win)
      topLeaves1.draw(win)

      stump2.draw(win)
      bottomLeaves2.draw(win)
      midLeaves2.draw(win)
      topLeaves2.draw(win)
      stump3.draw(win)
      bottomLeaves3.draw(win)
      midLeaves3.draw(win)
      topLeaves3.draw(win)

      flame1 = Polygon(Point(270, 320), Point(250, 450), Point(300, 450))
      flame2 = Polygon(Point(310, 330), Point(330, 450), Point(280, 450))
      fire = Polygon(Point(250, 290), Point(270, 370), Point(290, 320), Point(310, 380), Point(335, 330), Point(350, 410), Point(330, 450), Point(250,450), Point(230, 400))

      clickText=Text(Point(300,580), '(click)')
      clickText.setSize(16)
      clickText.setStyle('bold')
      clickText.draw(win)
      pt=win.getMouse()
      pt.draw(win)
      clickText.undraw()
      x=pt.getX()
      y=pt.getY()

      log1=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
      log1.setFill(color_rgb(139,69,19))

      log2=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
      log2.setFill(color_rgb(139,69,19))

      log3=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
      log3.setFill(color_rgb(139,69,19))

      pit = Circle(Point(300,435), 98)
      pit.setFill(color_rgb(110,110,110))

      rock1 = Circle(Point(380, 430), 17)
      rock1.setFill(color_rgb(160,160,160))

      rock2 = Circle(Point(220, 430), 17)
      rock2.setFill(color_rgb(160,160,160))

      rock3 = Circle(Point(300,360), 17)
      rock3.setFill(color_rgb(160,160,160))

      rock4 = Circle(Point(300,510), 17)
      rock4.setFill(color_rgb(160,160,160))

      rock5 = Circle(Point(245,480), 17)
      rock5.setFill(color_rgb(160,160,160))

      rock6 = Circle(Point(245,380), 17)
      rock6.setFill(color_rgb(160,160,160))

      rock7 = Circle(Point(355,380), 17)
      rock7.setFill(color_rgb(160,160,160))

      rock8 = Circle(Point(355,480), 17)
      rock8.setFill(color_rgb(160,160,160))

    

      def isClicked(button, pt):
         x = pt.getX()
         y = pt.getY()
         p1 = button.getP1()
         p2 = button.getP2()
         if (min(p1.getX(),p2.getX()) <x<max(p1.getX(),p2.getX())):
             if (min(p1.getY(),p2.getY()) <y<max(p1.getY(),p2.getY())):
                 return True
         return False
         

      def drawFire():
         flame1.draw(win)
         flame2.draw(win)
         fire.draw(win)
            
         for i in range (15):
             
            fire.setFill(color_rgb(255,215,0))
            sleep(0.05)
            fire.setFill(color_rgb(255,140,0))
            sleep(0.05)
            fire.setFill(color_rgb(255,215,0))
            flame1.setFill(color_rgb(255,0,0))
            sleep(0.05)
            flame1.setFill(color_rgb(255,140,0))
            flame2.setFill(color_rgb(255,0,0))
            sleep(0.05)
            flame2.setFill(color_rgb(255,140,0))

            
      def placeLogs():
          pt=win.getMouse()
          x=pt.getX()
          y=pt.getY()
          log1=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
          log1.setFill(color_rgb(139,69,19))
          for i in range(1):
              pt=win.getMouse()
              x=pt.getX()
              y=pt.getY()
              log1=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
              log1.setFill(color_rgb(139,69,19))
              log1.draw(win)
          for i in range(1):
              pt=win.getMouse()
              x=pt.getX()
              y=pt.getY()
              log2=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
              log2.setFill(color_rgb(139,69,19))
              log2.draw(win)
          for i in range(1):
              pt=win.getMouse()
              x=pt.getX()
              y=pt.getY()
              log3=Rectangle(Point(x-37,y+12), Point(x+37,y-12))
              log3.setFill(color_rgb(139,69,19))
              log3.draw(win)
          drawFire()


            
      def firePit():
          
          pit.draw(win)
         
          rock1.draw(win)
          
          rock2.draw(win)
          
          rock3.draw(win)
        
          rock4.draw(win)
          
          rock5.draw(win)
          
          rock6.draw(win)
        
          rock7.draw(win)
          
          rock8.draw(win)

          firstText = Text(Point(300,580), "Click to create a fire pit.")
          firstText.setSize(16)
          firstText.setStyle('bold')
          
          t=Text(Point(300, 580), 'A fire pit! Place 3 logs to create fire. (click)')
          t.draw(win)
          t.setSize(16)
          t.setStyle('bold')
          

          
          placeLogs()
          t.undraw()
             

         
      def forest():
          text1 = Text(Point (300,580), "You chose to stay and rest in the forest until morning (click)")
          text1.draw(win)
          text1.setSize(16)
          text1.setStyle("bold")
          win.getMouse()
          text1.undraw()
          text2 = Text(Point (300,580), "It's chilly outside! You can build a fire by chopping down the trees in the forest. \n Chop down the trees by clicking on the tree stumps. (click)")
          text2.draw(win)
          text2.setSize(16)
          text2.setStyle("bold")

       
          #chop down 1 tree each time the user clicks

         #stump1 = Rectangle(Point(110,400), Point(140,360))
          pt = win.getMouse()

          stumps = 0

          while stumps < 3:
            
             if isClicked(stump1, pt) == True:
                stumps = stumps + 1
                stump1.undraw()
                bottomLeaves1.undraw()
                midLeaves1.undraw()
                topLeaves1.undraw()
             elif isClicked(stump2, pt) == True:
                stumps = stumps + 1
                stump2.undraw()
                bottomLeaves2.undraw()
                midLeaves2.undraw()
                topLeaves2.undraw()
             elif isClicked(stump3, pt) == True:
                stumps = stumps + 1
                stump3.undraw()
                bottomLeaves3.undraw()
                midLeaves3.undraw()
                topLeaves3.undraw()

             pt = win.getMouse()
                
            
          if win.getMouse():
             text2.undraw()
             firePit()

         

                      
                                  
                                  
           
      forest()

      def toSleep():
         
         sleepText=Text(Point(300,580), "You're getting sleepy. (click)")
         sleepText.setStyle('bold')
         sleepText.setSize(16)
         sleepText.draw(win)
         pt=win.getMouse()
         sleepText.undraw()
         text=Text(Point(300,580), "(zzz)")
         text.draw(win)
         text.setSize(16)
         text.setStyle('bold')
         #sunrise
         for i in range(35):
                 sleep(.002)
           #move the moon off the screen
                 moon.move(-13,-5)
                 sleep(.002)
           #move the sun onto the screen
                 sun.move(-7,0)
         
            #starting from black, have sky fade to lavender
                 sky.setFill(color_rgb(0+5*i,0+5*i,0+7*i))
                 sleep(.1)
         for i in range(100):
            star[i].undraw()

           #undraw stars during sunrise
##           for i in range(100):
##                 star[i].undraw()
              
                   
         text.undraw()
         text2=Text(Point(300,580), "Good morning! You had a good night's sleep and you're feeling energized- (click)")
         text2.draw(win)
         text2.setSize(16)
         text2.setStyle('bold')
         pt=win.getMouse()
         text2.undraw()
         text3=Text(Point(300,580), "...Hey! Where'd all your stuff go!? You better try and find it\n or else you won't last long out here (click)")
         text3.setSize(16)
         text3.setStyle('bold')
         text3.draw(win)
         pt=win.getMouse()
         text3.undraw()
 #        crossroads = Crossroads(win)
      
       
  
      toSleep()
##      def run(self, win):
##         pt = win.getMouse()
##         A = Button(win, Point(250,550),80,40, "A: Continue")
##         
##           
##         while (True):
##            pt = win.getMouse()
##            if A.clicked(pt) == True:
##               
##               crossroads = Crossroads()
##                   
##                  # return 0
                  
                   
##            pt = win.getMouse()
##            elif B.clicked(pt):
##               
##               return 1
   
           

def main():
   buildfire = Buildfire()
#main()
