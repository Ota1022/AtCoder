s = input()
ans = 0
l = []
r = len(s)

for i in range(1, r):
    for j in range(i, r):
        num = s[0:j]
        l.append(num)
        l_i = [int(p) for p in l]

for k in l_i:
    if k % 2019 == 0:
        ans += 1
print(ans) 