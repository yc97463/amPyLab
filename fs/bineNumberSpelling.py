# Description: This program will take a number and spell it out in English.
import random
dict = {}
for line in open("numberDict.txt"):
    ss = line.strip()
    if len(ss) == 0:
        continue
    num, eng = ss.split(", ")
    dict[num] = eng

dice = [i for i in range(1, 1000)]
pick = random.choice(dice)
print(pick)
if pick // 100 > 0:
    h = dict[str(pick // 100)] + " hundred "
else:
    h = ""

if not pick % 100 // 10 > 0:
    t = ""
else:
    if pick % 100 // 10 == 1:
        t = dict[str(pick % 100)]
    else:
        t = dict[str(pick % 100 // 10 * 10)]

if not pick % 10 > 0:
    u = ""
else:
    u = dict[str(pick % 10)]

if t == "ten":

    print(h + t + " " + u)
else:
    print(h + t + "-" + u)
