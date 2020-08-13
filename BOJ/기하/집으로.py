import math

x, y, d, t = map(int, input().split())
answer = []
l = math.sqrt(x**2 + y**2)
k = l // d
answer.append(l) # 걸어서 가는 경우(일직선)
answer.append(k*t + l-k*d) # 점프 후 남은 거리 걸어서 가는 경우(일직선)
answer.append((k+1)*t + (k+1)*d-l) # 점프 후 초과한 거리 걸어서 돌아가는 경우(일직선)
if l < d:
    answer.append(t*2) # 방향을 꺾어서 2번 점프로만 가는 경우
else:
    answer.append((k+1)*t) # 방향을 꺾어서 점프로만 가는 경우
print(min(answer))