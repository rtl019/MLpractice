import csv
def Reader(fileName):
    file=open(fileName)
    dicr=csv.DictReader(file)
    for row in dicr:
        #L=[]
        #L.append(row['price'])
        print(row['beds'])
        
    
        
    














     
