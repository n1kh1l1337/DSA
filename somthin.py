n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s[::-1])
print(*l,sep="\n")