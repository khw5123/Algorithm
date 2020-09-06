for _ in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li2 = [(li[i], i) for i in range(n)]
    answer = 0
    while True:
        idx = li.index(max(li))
        if idx == 0:
            answer += 1
            if li2[idx][1] == m:
                break
            del li[0], li2[0]
        else:
            li.append(li[0])
            li2.append(li2[0])
            del li[0], li2[0]
    print(answer)