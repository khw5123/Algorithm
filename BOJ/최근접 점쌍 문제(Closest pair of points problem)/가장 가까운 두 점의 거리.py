import sys
input = sys.stdin.readline
INF = 9876543210

def closest_pair(points, start, end):
    if end - start <= 0:
        return INF
    mid = (start + end) // 2
    midX = (points[mid][0] + points[mid+1][0]) / 2
    leftDist, rightDist = closest_pair(points, start, mid), closest_pair(points, mid+1, end)
    minDist = min(leftDist, rightDist)
    tmp, save = [], []
    leftPtr, rightPtr = start, mid+1
    while leftPtr <= mid or rightPtr <= end:
        leftY, rightY = points[leftPtr][1] if leftPtr <= mid else INF, points[rightPtr][1] if rightPtr <= end else INF
        if leftY <= rightY:
            tmp.append(points[leftPtr])
            leftPtr += 1
        else:
            tmp.append(points[rightPtr])
            rightPtr += 1
        if tmp[-1][0] >= midX - minDist and tmp[-1][0] <= midX + minDist:
            save.append(tmp[-1])
    for i in range(start, end+1):
        points[i] = tmp[i-start]
    result = INF
    getDist = lambda p1, p2: (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    for i in range(len(save)):
        for j in range(1, 13):
            if i + j < len(save):
                result = min(result, getDist(save[i], save[i+j]))
    return min(minDist, result)

n, points = int(input()), []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort()
print(closest_pair(points, 0, n-1))