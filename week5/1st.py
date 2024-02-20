n = int(input())
x = float(input())

for i in range(n*2):
    x += x * 0.17

print(x)