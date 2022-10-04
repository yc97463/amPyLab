import random
a = int(input())
for i in range(a):
  stu = random.choice(range(0,100))
  def sc(level):
    print(stu, level, sep="\t")
  if stu>=90:
    sc("A")
  elif stu>=75:
    sc("B")
  elif stu>=60:
    sc("C")
  elif stu>=40:
    sc("D")
  elif stu>=20:
    sc("E")
  else:
    sc("F")
  #stu.append(random.choice(range(0,100))