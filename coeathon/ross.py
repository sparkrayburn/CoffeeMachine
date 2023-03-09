from itertools import combinations_with_replacement, combinations

test = 3
array1 = []
while True:
    try:
        inp = list(map(int, input().split()))
        if inp[0] < 1 or inp[0] > 1000 or inp[1] < 1 or inp[1] > 500 or inp[2] < 1 or inp[2] > 10000:
            raise ValueError
        break
    except ValueError:
        print("")
# try:
#     inp = list(map(int, input().split()))
# except RuntimeError:
#     inp = list(map(int, input().split()))

while inp[0] >= 1 :
    array1.append(inp[0])
    inp[0] = inp[0] - 1
while inp[1] > 1:
    array1.extend(array1)
    inp[1] -= 1

comb = combinations(array1, inp[2])
lizy=[]
list0 =[]
for i in list(comb):
    lizy.append(i)
for j in lizy:
    list0.append(sorted(j))

list1 = []
for num in list0:
    if num not in list1:
        list1.append(num)

print(len(list1))


# for i in list1:
#     sorted(i)
#     print(sorted(list1[1]))

