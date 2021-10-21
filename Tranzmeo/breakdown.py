def breakdown(amount,amt):
    notes = []
    for x in amt.keys():
        
        notes.append(x)

 
    noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
     

    lst1 = []
    lst2=[]
     
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            lst1.append(i)
            lst2.append(j)
            # print(lst1,lst2)
            # print (i ," : ", j)
    res = {}
    for key in lst1:
        for value in lst2:
            res[key] = value
            lst2.remove(value)
            break 
    print ("Currency Count -> ")
    print(res)
 
# Driver code
amount = 1256
amt = {2000:10,  500:10,  100:20, 50:0, 20:10, 10:5,  5:10, 2:10, 1:10}

breakdown(amount,amt)