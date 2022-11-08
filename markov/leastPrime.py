def leastPrime(n):
  for a in range(2, n):
    if n%a == 0:
      print(n, 'equals', a, '*', n)
      break
    else:
      print(n, 'is a prime number')
      a=n
  return a