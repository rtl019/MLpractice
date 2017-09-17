#authors= Muhammad Ali Shah and Kazim Hyder Nizam Shaikh (mashah and kshaikh)

#Conversion to Pixels

#this function uses % to change latitude and longitude to Pixels.

def LatLongToPixels(lat,long,XPixels,YPixels): # The latitude and longitude entered here will be values that need to be converted
    Lat1, Lat2= eval(input("Enter the two extreme latitude values seperated by comma: ")) #The latitude values entered here will be the range of latitude values given to us.
    Long1, Long2= eval(input("Enter the two extreme longitude values seperated by comma: ")) #The longitude values entered here will be the range of longitude values given to us.
    Xpix= (((long-Long2)/(Long1-Long2))*(XPixels))
    Ypix= (((lat-Lat1)/(Lat2-Lat1))*(YPixels))
    print("The converted width pixel is",int(Xpix),"and the converted height pixel is",int(Ypix))
    return


    
            


