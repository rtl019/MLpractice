import graphics
def initializeMap(mapFile, xPixels, yPixels):
    win = graphics.GraphWin('Sacramento Area', xPixels, yPixels)
    win.setCoords(0, 0, xPixels, yPixels)
    center = graphics.Point(xPixels/2, yPixels/2)
    image = graphics.Image(center, mapFile)
    image.draw(win)
    return win
