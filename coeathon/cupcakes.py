from itertools import combinations_with_replacement, combinations


list1 = []
inp = list(map(int, input().split()))
for i in inp:
    list1.append(i)

# print(list1)



r = list1[0] % list1[1]
# print(r)
list2 = []
while r>=1:
    list2.append(r)

    r -=1
lippy = []
i =0
r = list1[0] % list1[1]
lizy = []
while i<=r:
    comb = combinations_with_replacement(list2, i)
    for j in list(comb):
        lizy.append(j)
    i +=1
#print(lizy)
counts = 0
for j in lizy:
    lippy.append(sorted(j))
#rint(lippy)
litty = []
for k in lippy:
    if sum(k) == r:
        litty.append(k)

        counts += 1

#print(r)
print(counts)
#print (litty)

