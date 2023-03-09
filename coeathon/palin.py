
from itertools import combinations_with_replacement, combinations

# Get all combinations of [1, 2, 3] and length 2

# def isPalindrome(s):
#     return s == s[::-1]
lists = []
word = input()
for i in word:
    lists.append(i)



comb = combinations_with_replacement(lists, 3)


list1 = []
for i in list(comb):
    list1.append(i)
    #print(i)


list2 = []
domb = combinations_with_replacement(list1[1], 3)
for j in list(domb):
    list2.append(j)
    print(j)




        # s = j
        # ans = isPalindrome(s)
        # if ans:
        #     print(s)

# print(list1)

# k = 0
# domb = combinations_with_replacement(list1, 3)
# for m in list1:
#     print(m)



















