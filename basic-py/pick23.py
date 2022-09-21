while(True):
    a = input()
    try:
        num = int(a)
    except:
        print("invalid")
        continue
    if num%2 == 0 or num%3 == 0:
        print("yes\nit's", "2's 倍數" if num%2==0 else "3's 倍數")
        break
    else:
        print("no")


