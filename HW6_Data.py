from graphics import *
import csv
from HW6_Map import initializeMap


def plotCircle (a1, a2, color, win):
    C = Point(a1,a2)
    circ = Circle(C,2)
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
    Text(Point(500, 200),'fraud= red').draw(win)
    Text(Point(510, 180),'robbery = orange').draw(win)
    Text(Point(520, 160),'homicide = yellow').draw(win)
    Text(Point(530, 140),'theft = green').draw(win)
    Text(Point(540, 120),'burglary= blue').draw(win)
    Text(Point(550, 100),'others = indigo').draw(win)

def Crime(fileName, columnName):
    win=initializeMap('SacramentoMap.gif', 707, 774)
    file = open(fileName)
    dRdr = csv.DictReader(file)
    key(win)
    for row in dRdr:       
        if (eval(row[columnName])in range(2500,2701)):  #Fraud red
            a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
            plotCircle (a1, a2, 'red',win)
        if (eval(row[columnName]) in range(1200,1301))or (eval(row[columnName]) in range(2700,2801)): #Robbery Orange
                 a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
                 plotCircle (a1, a2, 'orange',win)
        if (eval(row[columnName])in range(900,1001)) or (eval(row[columnName])  in range(1300,1401)) or (eval(row[columnName]) in range(5200,5301)): #Homicide yellow 
                 a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
                 plotCircle (a1, a2, 'yellow',win)
        if (eval(row[columnName])in range(2300,2501))or (eval(row[columnName]) in range(2800,2901)): #Theft Green 
                 a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
                 plotCircle (a1, a2, 'green',win)
        if (eval(row[columnName])in range(2200,2301))or (eval(row[columnName]) in range(2900,3001)): #Burglarly Blue 
                 a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
                 plotCircle (a1, a2, 'blue',win)
        if (eval(row[columnName])in range(3500,3601))or (eval(row[columnName]) in range(5300,7001)): # Miscellaneous Indigo
                 a1,a2=LatLongToPixels(eval(row['latitude']),eval(row['longitude']),707,774)
                 plotCircle (a1, a2, 'indigo',win)
        
        
                
                 
        
