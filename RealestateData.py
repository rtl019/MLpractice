from graphics import *
import csv
from HW6_Map import initializeMap


def plotCircle (a1, a2, color, win):
    C = Point(a1,a2)
    circ = Circle(C,3)
    circ.setFill(color)
    circ.draw(win)
    
def LatLongToPixels(lat,long,XPixels,YPixels): # The latitude and longitude entered here will be values that need to be converted
    Lat1= 38.24
    Lat2= 39.03
    Long1= -120.6
    Long2= -121.56
    Xpix= (((long-Long2)/(Long1-Long2))*(XPixels))
    Ypix= (((lat-Lat1)/(Lat2-Lat1))*(YPixels))
    #print("The converted width pixel is",int(Xpix),"and the converted height pixel is",int(Ypix))
    return(Xpix,Ypix)

def key(win):
    Text(Point(500, 200),'cost less than $100000 = red').draw(win)
    Text(Point(510, 180),'cost between $100000 and $200000 = orange').draw(win)
    Text(Point(520, 160),'cost between $200000 and $300000 = yellow').draw(win)
    Text(Point(530, 140),'cost between $300000 and $400000 = green').draw(win)
    Text(Point(540, 120),'cost between $400000 and $500000 = blue').draw(win)
    Text(Point(550, 100),'cost between $500000 and $600000 = indigo').draw(win)
    Text(Point(560, 80),'cost greater than $600000 = violet').draw(win)

def Map(fileName, columnName):
    win=initializeMap('SacramentoMap.gif', 707, 774)
    file = open(fileName)
    dRdr = csv.DictReader(file)
    key(win)
    for row in dRdr:
        a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
        if (eval(row[columnName])<100000):
            plotCircle (a1, a2, 'red',win)
        if (eval(row[columnName]) in range(100000,200001)):
                 plotCircle (a1, a2, 'orange',win)
        if (eval(row[columnName])in range(200000,300001)):
                 plotCircle (a1, a2, 'yellow',win)
        if (eval(row[columnName])in range(300000,400001)):
                 plotCircle (a1, a2, 'green',win)
        if (eval(row[columnName])in range(400000,500001)):
                 plotCircle (a1, a2, 'blue',win)
        if (eval(row[columnName])in range(500000,600001)):
                 plotCircle (a1, a2, 'indigo',win)
        if (eval(row[columnName])>600000):
                 plotCircle (a1, a2, 'violet',win)
        



            
        
                
                 
        
