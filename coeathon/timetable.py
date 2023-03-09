
while True:
    try:
        time1 = input()
        time2 = input()
        if len(time1) < 2 or len(time2) < 2:
            raise ValueError
        break
    except ValueError:
        print("")

list1 = []
list2 = []


for i in time1:
    list1.append(i)

for i in time2:
    list2.append(i)

list3 = list1
q = len(list3)
list1.extend(list2)

# print(q)
i = 0
cp = 0
count = 0

while q<= len(list1) - 1:
    if list1[i] == list1[q]:
        cp += 1
    else:
        count += 1
    q += 1
    i += 1
# print(list1)
# print(count)
if count == 2:
    print("1")
else:
    print("0")








