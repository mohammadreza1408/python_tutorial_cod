


# lst=[3,"A",4.5]
# for i in range(len(lst)):
#     print(lst[i])

_list=[6,7,9]
_list.append(54)
print(_list)

_list.insert(2,"AA")
print(_list)

list1=[1,2,3,4,5,6,7,8,9,10]
x=len(list1)

while x >0:
    x -= 1
    print(list1[x])


list2=[1,2,3,4,5,6,7,8,9,10]
x=int(input("inter number : "))
if x in list2:
    print("your number in and index is : ", list2.index(x))
else:
    print("your number not in ")
