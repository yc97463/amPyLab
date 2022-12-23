def perm(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in perm(s[:i] + s[i+1:]):
                yield s[i] + p


s = "abcde"
r = []
i = 0
for p in perm(s):
    r.append(p)
print(r, i, sep='\n')
