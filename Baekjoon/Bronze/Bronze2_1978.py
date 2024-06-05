N = int(input())
nums = list(map(int, input().split()))
prime = 0

for num in nums:
    if num > 1:
        cnt = 1
        for n in range(2, num):
            if num % n == 0:
                cnt = 0
                break
        prime += cnt

print(prime)