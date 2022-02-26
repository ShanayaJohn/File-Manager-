import os
import t1
    


def fileDivision(L):
   
    ques=[]
    ans=[]
    rep_v=[]#overlapping values
    unique=[]
    overlap=[]
    for q,a in L:
        if q not in ques and a not in ans:
            unique.append((q,a))
            rep_v.append(q)
            rep_v.append(a)
        elif q not in rep_v and  a not in rep_v and (q,a) not in unique:
            unique.append((q,a)) 
        else:
            overlap.append((q,a))
            if q in ques and a in ans:
                rep_v.append(q)
                rep_v.append(a)
            elif q in ques:
                rep_v.append(q)
                i=ques.index(q)
            else:
                rep_v.append(a)
                i=ans.index(a)
               
        ques.append(q)
        ans.append(a)
    
    
    
    #if overlapping file is empty 
    if not overlap:
        if os.path.exists("unique_QA_Pairs.txt"):
            os.remove("unique_QA_Pairs.txt")
        if os.path.exists("Overlapping.txt"):
            os.remove("Overlapping.txt")

        os.rename('QA_Pairs.txt','unique_QA_Pairs.txt')

    else:
        UQ= open('unique_QA_Pairs.txt','w')
        OL= open('Overlapping.txt','w')
                    
    
        for ques,ans in overlap:
            OL.write(ans)
            OL.write(ques)
   

        for ques,ans in unique:
            UQ.write(ans)
            UQ.write(ques)
        UQ.close()
        OL.close()
  
fileDivision(t1.Pair('QA_Pairs.txt'))
 