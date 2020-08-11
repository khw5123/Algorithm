import sys
input = sys.stdin.readline

distance = lambda x1, y1, x2, y2: (y2-y1)**2 + (x2-x1)**2
for _ in range(int(input())):
    coords = []
    for _ in range(4):
        coords.append(tuple(map(int, input().split())))
    coords.sort()
    if distance(coords[0][0], coords[0][1], coords[1][0], coords[1][1]) == distance(coords[0][0], coords[0][1], coords[2][0], coords[2][1]) and distance(coords[3][0], coords[3][1], coords[1][0], coords[1][1]) == distance(coords[3][0], coords[3][1], coords[2][0], coords[2][1]) and distance(coords[0][0], coords[0][1], coords[3][0], coords[3][1]) == distance(coords[1][0], coords[1][1], coords[2][0], coords[2][1]):
        print(1)
    else:
        print(0)