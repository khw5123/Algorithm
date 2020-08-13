import sys
input = sys.stdin.readline

need = set(tuple(map(int, input().split())) for _ in range(int(input())))
star = set(tuple(map(int, input().split())) for _ in range(int(input())))
tx, ty = list(need)[0]
for x, y in star:
    dx, dy, exist = x-tx, y-ty, True
    for x2, y2 in need:
        if (x2+dx, y2+dy) not in star:
            exist = False
            break
    if exist:
        print(dx, dy)
        break