# 투 포인터 + 해싱
import sys
input = sys.stdin.readline

n, answer = int(input()), 0
a, b, c, d, ab, cd = [], [], [], [], [], []
for _ in range(n):
    _a, _b, _c, _d = map(int, input().split())
    a.append(_a); b.append(_b); c.append(_c); d.append(_d)
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        cd.append(c[i]+d[j])
ab, cd = sorted(ab), sorted(cd)
end, save = len(cd)-1, {}
for start in range(len(ab)):
    if ab[start] in save:
        answer += save[ab[start]]
        continue
    while end >= 0 and ab[start]+cd[end] >= 0:
        if ab[start]+cd[end] == 0:
            answer += 1
            if ab[start] not in save:
                save[ab[start]] = 1
            else:
                save[ab[start]] += 1
        end -= 1
print(answer)
'''
# 투 포인터(시간 초과)
import sys
input = sys.stdin.readline

n, answer = int(input()), 0
a, b, c, d, ab, cd = [], [], [], [], [], []
for _ in range(n):
    _a, _b, _c, _d = map(int, input().split())
    a.append(_a); b.append(_b); c.append(_c); d.append(_d)
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        cd.append(c[i]+d[j])
ab, cd = sorted(ab), sorted(cd)
end = len(cd)-1
for start in range(len(ab)):
    idx, confirm = -1, False
    while end >= 0 and ab[start]+cd[end] >= 0:
        if ab[start]+cd[end] == 0:
            answer += 1
            if not confirm:
                idx, confirm = end, True
        end -= 1
    if confirm:
        end = idx
print(answer)
'''