import random
a = list(range(1,1023))
b = random.choice(a)
print(bin(b))
c=""
while b > 0:
  r = b % 2
  c = str(r) + c
  b = (b - r) // 2
print("convert", b, "to", "0b"+c)