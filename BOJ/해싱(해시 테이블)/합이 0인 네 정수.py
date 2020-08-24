# 해싱
import sys
input = sys.stdin.readline

n, answer = int(input()), 0
a, b, c, d, ab, cd = [], [], [], [], {}, {}
for _ in range(n):
    _a, _b, _c, _d = map(int, input().split())
    a.append(_a); b.append(_b); c.append(_c); d.append(_d)
for i in range(n):
    for j in range(n):
        if a[i]+b[j] not in ab:
            ab[a[i]+b[j]] = 1
        else:
            ab[a[i]+b[j]] += 1
        if c[i]+d[j] not in cd:
            cd[c[i]+d[j]] = 1
        else:
            cd[c[i]+d[j]] += 1
for k, v in ab.items():
    if -k in cd:
        answer += (ab[k]*cd[-k])
print(answer)