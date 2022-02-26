def ans():
    with open ('QA_Pairs.txt', 'r', encoding='utf-8-sig') as QA : 
        Lines= QA.readlines()
        L=[]
        
        for i in range(0,len(Lines)-1,2):
            L.append((Lines[i]))
    return L

L=ans()
print(len(L))
with open ('Answers.txt', 'w', encoding='utf-8-sig') as ans :
     for i in L:
         i=i.replace('answer ','')
         ans.write(i)
