a = float(input())
x = 1
for i in range(4):
    #print(".")
    x = (x + a / x) / 2
print(x)