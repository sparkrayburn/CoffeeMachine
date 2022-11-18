# # def add(*args):
# #     sum = 0
# #     for n in args:
# #         sum += n
# #     print(sum)
# # add(3, 4)
#
#
# def calculate (n,**kwargs):
#
#     sum=0
#     sum = kwargs.get("y")
#     n += kwargs.get("x")
#
#     print(n)
#
# calculate(2, x=3)

import math
import os
import random
import re
import sys



n = input()
if (int(n) %2==0) and (2<int(n)<5) or (int(n)%2==0) and(20<int(n))  :
    print("Not Weird")
elif (int(n)%2==0) and (6<= int(n) < 20) or (int(n)%2!=0) :
    print ("Weird")