a = int(input())
bnr = bin(a).replace('0b','')
x = bnr[::-1]
while len(x) < 8:
    x += '0'
bnr = x[::-1]
print(bnr)