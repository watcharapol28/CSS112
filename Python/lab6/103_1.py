n = int(input())
Dict = {}
for i in range(n):
    x = input().split()
#    print(x)
    if not x[1] in Dict:
        Dict[x[1]] = (x[0],)
    else:
        Dict[x[1]] += (x[0], )
#    print(Dict)
ans = input()
print(Dict[ans])