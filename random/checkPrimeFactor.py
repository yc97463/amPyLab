import random
import numpy as np
a=list(range(1,100000))
a=int(random.choice(a))
prime=[]
maxp = 1
while a > maxp:
  for i in range(2, int(np.ceil(a))):
    if a%i == 0:
      print("number=", a, "now=", i)
      c=i
      m=a/c
      break
  else:
    print(a, "is a prime number")
    c=a
    m=a//c
  a=m
  if not c in prime:
    prime.append(int(c))
    maxp=c
print(prime)