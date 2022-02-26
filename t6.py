#find the frequency of each term
import t3 
import string
def getWord():
    with open ('Unique_QA_Pairs.txt', 'r') as UQ :
        Words=UQ.read().lower()
        for i in Words:
            if i in string.punctuation and i !="'":
                Words=Words.replace(i,"")
            if i == "\n":
                Words=Words.replace(i, " ")

        R=Words.split(" ")
        S=set(R)
        d={}
        for i in S:
            if i != '' and i !='question' and i != 'answer':
                y=R.count(i)
                d[i]=y
        return d

if __name__=="__main__":    
    with open ('Frequency.txt', 'w') as FW :
        d=getWord()
        item=d.items()
        for x,y in item:
            FW.write(x+", "+str(y)+"\n")
        
    
    

    