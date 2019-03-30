import sys
import random
b=random.randint(1,10)
while True: 
    a=int(input('输入一个数字'))
    if a>b:
        print ("bigger")
    elif a<b:
        print ('smaller')
    else:
        print ('equal')
        break
    