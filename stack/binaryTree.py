from stackModule import Stack

s = Stack()
stackLst = ["-","+","7","*","4","5","+","2","1"]
for i in range(len(stackLst)):
  s.push(stackLst[i])