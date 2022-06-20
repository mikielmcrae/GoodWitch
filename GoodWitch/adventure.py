from house import House
from forest import Forest
from forest2 import Forest2
from forest3 import Forest3
from buildfire import Buildfire
from bridge import Bridge
from brokenbridge import Brokenbridge
from mountains import Mountains
from cave import Cave
from crossroads import Crossroads
from treasure import Treasure
from gameover import Gameover
from castle import Castle
from button import*
from graphics import*



   
def isClicked(button, pt):
   #isClicked function to return true if buttons were clicked
   #setting x and y values for user's click
   pt=win.getMouse()
   x = pt.getX()
   y = pt.getY()
   p1 = button.getP1()
   p2 = button.getP2()
   #testing if mouse click was in button
   if (min(p1.getX(),p2.getX()) <x<max(p1.getX(),p2.getX())):
       if (min(p1.getY(),p2.getY()) <y<max(p1.getY(),p2.getY())):
           return True
   return False

def main():
   #House, A:Forest, B: Mountains
   win = GraphWin('Adventure', 600,600)
   house = House(win)
   result = house.run(win)
   #If house to forest is picked
   if result == 0:
      forest = Forest(win)
      #forest to fire
      result = forest.run(win)
      if result == 0:
         buildfire = Buildfire(win)
 
 #        result = buildfire.run(win)
         if result == 0:
            crossroads = Crossroads(win)
            if result == 0:
               forest2 = Forest2(win)
               result = forest2.run(win)
               if result == 0:
                  gameover = Gameover(win)
               elif result == 1:
                  castle = Castle(win)
            elif result == 1:
               gameover = Gameover(win)
   
               if result == 0:
                  adventure = Adventure(win)
               
            
 #           result= crossroads.run(win)
            
#            crossroads = Crossroads(win)
         elif result == 1:
            pass
         
      #forest to bridge
      elif result == 1:
         bridge = Bridge(win)
         result = bridge.run(win)
         if result == 0:
            brokenbridge = Brokenbridge(win)
         elif result ==1:
            forest3 = Forest3(win)
            result = forest3.run(win)
   elif result == 1:
      #if house to mountains is picked
      mountains = Mountains(win)
      result = mountains.run(win)
      if result == 0:
         cave = Cave(win)
         result = cave.run(win)
         if result == 0:
            
            
            castle = Castle(win)
         elif result == 1:
            gameover = Gameover(win)
      elif result ==1:
         treasure = Treasure(win)
         result = treasure.run(win)
         if result ==0:
            pass
            #gameover = Gameover(win) do not comment in
         elif result == 1:
            pass
            #castle = Castle(win) do not comment in
         
      
            


   ##
   ##   result = forest.run(win)
   ##   if result == 0:
   ##      pass
   ##   elif result == 1:
   ##      bridge = Bridge(win)
      

      
       
       
main()

