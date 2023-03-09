list1 = []
inp = list(map(int, input().split()))
for i in inp:
    list1.append(i)




list1.sort(reverse=True)



r = 0
j = 2
x = len(list1)/3

while j < len(list1):
    list1.remove(list1[j])
    j +=2

print(sum(list1))




















