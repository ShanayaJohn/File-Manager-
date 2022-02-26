

def Pair(file):
    with open (file, 'r') as QA :  
        Lines= QA.readlines()
        L=[]
        
        for i in range(0,len(Lines)-1,2):
            L.append((Lines[i+1].lower(),Lines[i].lower()))
    return L

def countPair(L): 
    return len(L)

if __name__=="__main__":

    print(countPair(Pair('QA_Pairs.txt')))
    print(countPair(Pair('unique_QA_Pairs.txt')))
    print(countPair(Pair('Overlapping.txt')))
    