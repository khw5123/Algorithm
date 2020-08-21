import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())
left, right = 0, m
if sum(budget) <= m:
    print(max(budget))
else:
    while left+1 < right:
        mid = (left+right)//2
        total = 0
        for money in budget:
            if money < mid:
                total += money
            else:
                total += mid
        if total > m:
            right = mid
        else:
            left = mid
    print(left)