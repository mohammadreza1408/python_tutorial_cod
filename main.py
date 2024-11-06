


# x= int(input("number 1: "))
# y= int(input("number 2: "))
#
#
# def max_(a,b):
#     if a>b:
#         return a
#     return b
#
# print(max_(x,y))
#################################################

# x= int(input("number 1: "))
#
# def zoj_fard(a):
#     if a % 2 ==0:
#         return "even"
#     return "odd"
#
# print(zoj_fard(x))
#################################################
# list_1=[]
#
# while True:
#     x=input(f"input number in list : ")
#     if x != "exit":
#         list_1.append(int(x))
#     else:
#         print(list_1)
#         break
#
# def maximom(lst):
#     _max=0
#     for i in range(len(lst)):
#         if lst[i] > _max:
#             _max = lst[i]
#     return _max
#
# print(maximom(list_1))

##################################################
# list_2=[]
# while True:
#     x = input(f"input number in list : ")
#     if x != "exit":
#         list_2.append(int(x))
#     else:
#         break
#
# def _sum(lst):
#     sum_lst=0
#     for i in range(len(lst)):
#         sum_lst += lst[i]
#     return sum_lst
#
# print(_sum(list_2))
###################################################
list_1=[5,7,6,4,5,8,9,7,6,5,8,10,12,15,12]

i=0
def tekrari(lst):
    list_2 = []
    for i in range(len(lst)):
        if lst[i] not in list_2:
            list_2.append(lst[i])
    return list_2

print(tekrari(list_1))




