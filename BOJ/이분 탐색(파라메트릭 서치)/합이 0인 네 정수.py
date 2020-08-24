# 이분 탐색
import sys
input = sys.stdin.readline

n, answer = int(input()), 0
a, b, c, d, ab, cd = [], [], [], [], {}, []
for _ in range(n):
    _a, _b, _c, _d = map(int, input().split())
    a.append(_a); b.append(_b); c.append(_c); d.append(_d)
for i in range(n):
    for j in range(n):
        if a[i]+b[j] not in ab:
            ab[a[i]+b[j]] = 1
        else:
            ab[a[i]+b[j]] += 1
        cd.append(c[i]+d[j])
cd = sorted(cd)
for k, v in ab.items():
    left, right = 0, len(cd)-1
    while left <= right:
        mid = (left+right)//2
        if k+cd[mid] == 0:
            for i in range(mid, len(cd)):
                if k+cd[i] == 0:
                    answer += v
                else:
                    break
            for i in range(mid-1, -1, -1):
                if k+cd[i] == 0:
                    answer += v
                else:
                    break
            break
        elif k+cd[mid] > 0:
            right = mid-1
        else:
            left = mid+1
print(answer)