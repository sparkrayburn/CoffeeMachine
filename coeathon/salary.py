from itertools import combinations_with_replacement, combinations, permutations
import functools

list1 = []

while True:
    try:
        inp = list(map(int, input().split()))
        if inp[0] < 0 or inp[0] >= 60 or inp[1] < 0 or inp[1] >= 60 or inp[2] < 0 or inp[2] >= 60:
            raise ValueError
        break
    except ValueError:
        print("")
for i in inp:
    list1.append(i)


list2 = []
for j in list1:
    while list1[0] !=0:
        list2.append(3)
        list1[0] -=1
    while list1[1] !=0:
        list2.append(6)
        list1[1] -=1
    while list1[2] !=0:
        list2.append(9)
        list1[2] -=1

i = 0
lizy = []
while i<= len(list2):
    comb = permutations(list2, i)
    for j in list(comb):
        lizy.append(j)
    i +=1
num = 0

n = 1
list3 = []
while n < len(lizy):
    res = functools.reduce(lambda sub, ele: sub * 10 + ele, lizy[n])
    n += 1
    list3.append(res)

print(sum(list3))

# lippy = []
# i =0
# r = list1[0] % list1[1]
# lizy = []
# while i<=r:
#     comb = combinations_with_replacement(list2, i)
#     for j in list(comb):
#         lizy.append(j)
#     i +=1
# #print(lizy)
# counts = 0
# for j in lizy:
#     lippy.append(sorted(j))
# #rint(lippy)
# litty = []
# for k in lippy:
#     if sum(k) == r:
#         litty.append(k)
#
#         counts += 1
#
# #print(r)
# print(counts)
# #print (litty)

