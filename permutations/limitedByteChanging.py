def choose(s, r):
    ans = []
    if r == 1:
        for i in range(len(s)):
            ans.append(s[i])
        return ans
    if len(s) == r:
        ans.append(s)
        return ans
    t = s[1:]
    a = choose(t, r-1)
    for item in a:
        ans.append(s[0] + item)
    b = choose(t, r)
    return ans + b


s = str(12345)
r = 3
ans = choose(s, r)
print(ans)
