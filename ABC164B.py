a, b, c, d = map(int, input().split())
while True:
    c -= b 
    if c <= 0:
        break
    a -= d
    if a<= 0:
        break
print('Yes' if a > c else 'No')