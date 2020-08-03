import sys
input = sys.stdin.readline

n, timetable, answer = int(input()), [], 1
for _ in range(n):
    timetable.append(tuple(map(int, input().split())))
timetable.sort(key=lambda x:(x[1], x[0]))
end = timetable[0][1]
for i in range(1, n):
    if timetable[i][0] >= end:
        end = timetable[i][1]
        answer += 1
print(answer)