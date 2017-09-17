import csv
def Reader(fileName):
    file=open(fileName)
    dicr=csv.DictReader(file)
    for row in dicr:
        L=[]
        
        
        L.append(row['price'])
        print(row('price'))    
    
        
    













import csv
def reader(fileName):
    file=open(fileName)
    L=[]
    M=[]
    L1=[]
    L2=[]
    dicr=csv.DictReader(file)
    for row in dicr:
        L.append(row['price'])
        L1.append(row['latitude'])
        L2.apprnd(row['longitude'])
        
    l1=len(L1)
    l2=len(L2)
    a=len(L)
    #return(a)
    for p in range(a):
        d=eval(L[p])
        M.append(d)
    f=len(M)
    for i in range(f):
        if(M[i]<100000):
            r=
    
    Maxmin=[]
    for i in range(0,J):
        d=eval(M[i])
        Maxmin.append(d)
        s=s+d
    m=max(Maxmin)
    n=min(Maxmin)
    #print(s)
    Average= (s/J)
    print("Average is ",Average)
    print("Maximum Grade is",m)
    print("Lowest Grade is ",n)


#End
        
