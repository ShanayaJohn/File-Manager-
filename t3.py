# Store the pairs from unique_QA_Pairs.txt as a dictionary.
import t1
import string
def dict(L):
    d={}

    for ques,ans in L:
        d[ques]=ans
    return d
      
if __name__=="__main__":   
    d= dict(t1.Pair('unique_QA_Pairs.txt'))

    with open ('QA_dictionary.txt', 'w') as QD:
        for key,value in d.items():
            QD.write(key[:-2]+ " : "+ value)
