import random
a = list(range(1,1023))
b = random.choice(a)
print(b)
print(hex(b))
c=""
while b > 0:
  r = b % 16
  if r <= 9:
    c = str(r) + c  
  elif r >= 10 and r <= 15:
    c = str(chr(65+r-10)) + c
  b = (b - r) // 16
print("convert", b, "to", "0x"+c)