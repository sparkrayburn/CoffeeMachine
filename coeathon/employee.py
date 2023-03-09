inp = list(map(int, input().split()))
list = []
for i in inp:
    list.append(i)


print(list)

i = 0
j =1
lump =10000
count = 10000
while j< len(list):
    if list[i] < list[j]:
        count += 20000
        count = count + lump
        i +=1
        j +=1
        print(count)
    else:
        count += 10000
        lump = 10000
        i += 1
        j += 1
        print(count)
print(lump)