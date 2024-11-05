import random

list1=[]
i=0
while i<10:
    new = random.randint(1,10)
    if new in list1:
        continue
    else:
        list1.append(new)
        i+=1
print(list1)
print(len(list1))

