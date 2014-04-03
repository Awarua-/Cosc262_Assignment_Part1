import random
from time import clock, time           #           t=bucket[x]=(top,bottom)
class cell:                            #                    x
  key=0                                #  ----------------------------
  next=0                     #    bucket  _________________|_|________
                                       #                    |
class list:                            #                   |x| top
  top=0    # top is first cell of list                     | |
  bottom=0 # bottom is the bottom cell                      |

def add(x):
  t=bucket[x]         # t is x-th bucket                   |x|  bottom
  w=cell(); w.key=x   # w is a new cell with key x         |0|
  if t.bottom!=0:
    temp=t.bottom     # temp is the bottom cell            | |  w
    temp.next=w       # new cell w comes under bottom cell | |
  if t.top==0:        # If x-th bucket is empty
    t.top=w           # w becomes the first cell in bucket[x]
  t.bottom=w
  print(x),


bucket=[]  # prepare 100 buckets
for i in range(0,100):bucket=bucket+[list()]

n=int(input('input n'))
tmp=[]
for i in range(0,n):
  x=int(100*random.random()) #maximum is 99
  tmp=tmp+[x]

tt=clock()
for i in range(0,n):  # Add data to buckets
  x=tmp[i]
  add(x)

print("\n")
j=0
for i in range(0, 100): # retrieve data from buckets to tmp
  p=bucket[i].top
  while p!=0:
    tmp[j]=p.key; j=j+1
    p=p.next

for i in range(0,n):
  print(tmp[i]),
tt=tt-clock()

