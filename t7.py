import t6
def order():
    d=t6.getWord()
    order_d=sorted(d.items(), key=lambda x:-x[1])
    return order_d
order_d=order()
print(len(order_d))
with open ('Decreasing_Frequency.txt', 'w') as DF :
    for i in order_d:
         DF.write(i[0]+", "+str(i[1])+"\n")
      