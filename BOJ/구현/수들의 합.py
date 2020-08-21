s, num, _sum, answer = int(input()), 1, 0, 0
while True:
    _sum += num
    answer += 1
    if _sum > s:
        answer -= 1
        break
    num += 1
print(answer)