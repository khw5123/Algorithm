for _ in range(int(input())):
    h, w, n = map(int, input().split())
    y = str(h if n%h == 0 else n%h)
    x = str(n//h if n%h == 0 else ((n//h)+1))
    if len(str(x)) == 1:
        x = '0' + x
    print(y+x)