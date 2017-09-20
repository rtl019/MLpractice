import csv
def Reader(fileName):
    file=open(fileName)
    dicr=csv.DictReader(file)
    for row in dicr:
        size=[]
        size.append(row['sq__ft'])
        price=[]
        price.append(row['price'])
        return price,size 
        
    
        
    














     
