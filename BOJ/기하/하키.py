w, h, x, y, p = map(int, input().split())
dist, answer = lambda x1, y1, x2, y2: (x1-x2)**2 + (y1-y2)**2, 0
for _ in range(p):
    a, b = map(int, input().split())
    if (x <= a <= x+w and y <= b <= y+h) or (dist(a, b, x, y+h/2) <= (h/2)**2) or (dist(a, b, x+w, y+h/2) <= (h/2)**2):
        answer += 1
print(answer)