import random
score = 0
dice = [i for i in range(1,7)]
while True:
    this = []
    for i in range(3):
        this.append(random.choice(dice))
    diff = set(this) #turn list to set to get difference object
    if len(diff)==1:
        score+=7
        print(this,score, ", great job")
        break
    elif len(diff)==2:
        this.sort()
        if this[0]==this[1]:
            score+=this[2]
        else:
            score+=this[0]
        print(this, score)
        break
    else:
        print(this, "Try again ><")
        continue
