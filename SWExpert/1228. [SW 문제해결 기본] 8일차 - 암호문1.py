for t in range(10):
    n = int(input())
    cryptograph = list(map(int, input().split()))
    count = int(input())
    command = []
    for c in list(map(str, input().split())):
        if c == 'I' or c == 'D' or c == 'A':
            command.append([c])
        else:
            command[-1].append(c)
    for i in range(len(command)):
        for j in range(int(command[i][2])):
            cryptograph.insert(int(command[i][1])+j, int(command[i][j+3]))
    print('#' + str(t+1), end=' ')
    for i in range(10):
        print(cryptograph[i], end=' ')
    print()