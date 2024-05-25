N = int(input())
area = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x_loc, y_loc = map(int, input().split())

    for x in range(x_loc, x_loc+10):
        for y in range(y_loc, y_loc+10):
            area[x][y] = 1
    
res = 0
for n in area:
    res += sum(n)

print(res)