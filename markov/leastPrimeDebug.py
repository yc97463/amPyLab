import random
from leastPrime import leastPrime
s = list(range(1, 100000))
# n = random.choice(s)
n = 2*2*3*5*13*17*49
prime = []
max_prime = 1 #for temp
while n > max_prime:
  p = leastPrime(n)
  n = n // p
  if not p in prime:
    prime.append(p)
    max_prime = p

print(prime)