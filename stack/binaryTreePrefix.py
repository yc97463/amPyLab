from stackModule import Stack

ss = input("a prefix exporession:")
items = ss.split()
print(items)

s = Stack()
for i in range(len(items)-1,-1,-1):
  if items[i].isdigit():
    s.push(items[i])
  else:
    op=items[i]
    d1=s.pop()
    d2=s.pop()
    ans = str(eval(d1+op+d2))
    s.push(ans)
ans=s.pop()
print(ans)