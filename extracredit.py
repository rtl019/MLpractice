#This is the Extra Credit Part of Our Homework
from graphics import *
from HW6_Map import initializeMap
from graphics import *
from LatLongToPixels import *
from HW6_Filter import *
from RealestateData import *
def Extracredit():
    win=initializeMap('SacramentoMap.gif', 707, 774)
    #get and draw two end points of line
    Text(Point(360,680),"Click on one point on the map and then click on another point the required distance apart").draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    C=LatLong(707,774,38.24,39.03,-121.56,-120.6)
    one= C.pixels2LatLong(x1,y1)
    two= C.pixels2LatLong(x2,y2)
    a1,a2=one
    b1,b2=two
    d=distanceMiles(a1,a2,b1,b2)
    return filter(a2,a1,d) #see readme file to understand the output you get

