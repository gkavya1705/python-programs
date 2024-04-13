a=list(map(int,input().split()))
a.sort()
a.remove(max(a))
print(max(a))