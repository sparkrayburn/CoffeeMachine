
inp = list(map(int, input().split()))
object = []
for _ in range(inp[0]):
    inp = list(map(int, input().split()))
    object.append(inp)

print(object)


list1 = []
for i in object:
    q = 0
    for j in i:
        if i[q] not in list1:
            list1.append(i[q])
            try:
                if i[0] in list1 and i[q+1] in list1:
                    break
            except IndexError:
                break
            else:
                q += 1


for i in list1:
    if i == 0:
        list1.remove(i)

print(len(list1))
print(list1)

# 6 6
# 2 3 4
# 1 4
# 3 4 5 6
# 3
# 1 3 4
# 0
# 4