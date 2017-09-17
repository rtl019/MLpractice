# LatLongToPixels.py -- CS-1004, C-term 2015, published Feb 26, 2015

""" This module is implemented as a class to provide a
    conversion function between pixel coordinates (as required
    by an image in graphics.py) and latitude and longitude, as
    represented by a map image."""

class LatLong:
    def __init__(self, xPixels, yPixels, latMin, latMax,
                  longMin, longMax):
        self.xWidth     = xPixels
        self.yHeight    = yPixels
        self.bottomEdge = latMin    # minimum latitude
        self.topEdge    = latMax    # maximum latitude
        self.leftEdge   = longMin   # minimum longitude
        self.rightEdge  = longMax   # maximum longitude

        self.latScale   = yPixels / (latMax - latMin)
        self.longScale  = xPixels / (longMax - longMin)

    def latLong2Pixels(self, latitude, longitude):
        #   Assumes that the origin is in the lower left corner
        yOffset     = latitude - self.bottomEdge 
        yPosition   = yOffset * self.latScale
        xOffset     = longitude - self.leftEdge
        xPosition   = xOffset * self.longScale
        return xPosition, yPosition

    def pixels2LatLong(self, x, y):
        #   Assumes that the origin is in the lower left corner
        lat = self.bottomEdge + y/self.latScale
        long = self.leftEdge + x/self.longScale
        return lat, long



    
