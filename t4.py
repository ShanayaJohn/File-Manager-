def question():
    with open ('QA_Pairs.txt', 'r') as QA : 
        Lines= QA.readlines()
        L=[]
        
        for i in range(0,len(Lines)-1,2):
            L.append((Lines[i+1]))
    return L

L=question()
print(len(L))
with open ('Questions.txt', 'w') as Qu :
     for i in L:
         i=i.replace('question ','')
         Qu.write(i)

    

       