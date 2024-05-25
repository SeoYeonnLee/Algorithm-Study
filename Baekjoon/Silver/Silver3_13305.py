N = int(input())
dis  = list(map(int, input().split()))
price  = list(map(int, input().split()))
cnt = [0 for _ in range(N)]

min_idx = 0

for n in range(N-1):
    if price[n] <= price[min_idx]:
        cnt[n] += dis[n]
        min_idx = n
    else:
        cnt[min_idx] += dis[n]

total = 0
for p, c in zip(price, cnt):
    total += (p*c)
print(total)