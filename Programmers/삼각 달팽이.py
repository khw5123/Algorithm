def solution(n):
    answer, li = [], []
    for i in range(1, n+1):
        li.append([0]*i)
    x, y, d, num = 0, 0, 'down', 1
    li[x][y] = 1
    while num != (n*(n+1))//2:
        num += 1
        if d == 'down':
            x += 1
            if x == n or li[x][y] != 0:
                x -= 1
                d = 'right'
                num -= 1
            else:
                li[x][y] = num
        elif d == 'right':
            y += 1
            if y == n or li[x][y] != 0:
                y -= 1
                d = 'up'
                num -= 1
            else:
                li[x][y] = num
        else:
            x -= 1
            y -= 1
            if li[x][y] != 0:
                x += 1
                y += 1
                d = 'down'
                num -= 1
            else:
                li[x][y] = num
    for i in range(n):
        for j in range(i+1):
            answer.append(li[i][j])
    return answer