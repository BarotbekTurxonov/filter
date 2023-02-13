# def domain_name(url):
#     a = url.split('//')[-1].split('.')
#     return a[1] if a[0] == "www" else a[0]
#
#
#
#
# print(domain_name('"http://www.zombie-bites.com"'))
# i=input()
# z=0
# y=0
# n=0
# for x in i:
#     x=int(x)
#     if n:
#         z+=x
#         n=0
#     else:
#         y+=x
#         n=1
# print('Yes'if z==y else 'No')



# x=input().split()
# y=int(input())
# x.pop(y)
# print(' '.join(x))
#
#
#
# a = input()
# print(a.count(max(a, key=a.count)))


import math
import os
import random
import re
import sys

# first_multiple_input = input().rstrip().split()
#
# n = int(first_multiple_input[0])
#
# m = int(first_multiple_input[1])
#
# matrix = []
#
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)


#
# def time(time):
#     print(time)
#     from datetime import datetime
#     now = str(datetime.now())
#         print(now)
#     x = now.split()[0].split('-')
#     z = now.split()[-1].split(':')
#     y = int(x[0])
#     mo = int(x[1])
#     d = int(x[-1])
#     h = int(z[0])
#     m = int(z[1])
#     s = int(z[-1].split('.')[0])
#     # request time
#
#     time = str(time)
#     tx = time.split()[0].split('-')
#     tz = time.split()[-1].split(':')
#     ty = int(tx[0])
#     tmo = int(tx[1])
#     td = int(tx[-1])
#     th = int(tz[0])
#     tm = int(tz[1])
#     ts = int(tz[-1].split('.')[0])
#
#     year = y-ty
#     mounth = mo-tmo
#     day = d-td
#     hour = h-th
#     minut = m-tm
#
#     time = f"{s-ts} soniya"
#     if minut:
#         time = f"{m-tm} daqiqa"
#     if hour:
#         time = f"{h-th} soat"
#     if day:
#         time = f"{d-td} kun"
#     if mounth:
#         time = f"{mo-tmo} oy"
#     if year:
#         time = f"{y-ty} yil"
#     print(time)
#
#     return

import os
from random import randint

for i in range(365):
    for j in range(0,randint(1, 10)):
        d= str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="'+ d +'" -m "commit"')

os.system('git push -u origin main')












