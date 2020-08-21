import sys
input = sys.stdin.readline

n, arr = int(input()), sorted(list(map(int, input().split())))
m, target = int(input()), list(map(int, input().split()))
answer = {}
for num in target:
    if num in answer:
        continue
    result = 0
    left, right = 0, n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == num:
            for i in range(mid, n):
                if arr[i] == num:
                    result += 1
                else:
                    break
            for i in range(mid-1, -1, -1):
                if arr[i] == num:
                    result += 1
                else:
                    break
            break
        if arr[mid] < num:
            left = mid+1
        else:
            right = mid-1
    answer[num] = result
for num in target:
    print(answer[num], end=' ')
print()
'''
import sys
input = sys.stdin.readline

def binarySearch(left, right, num):
    if left > right:
        return 0
    ret = 0
    mid = (left+right)//2
    if arr[mid] == num:
        for i in range(mid, n):
            if arr[i] == num:
                ret += 1
            else:
                break
        for i in range(mid-1, -1, -1):
            if arr[i] == num:
                ret += 1
            else:
                break
    elif arr[mid] < num:
        ret = binarySearch(mid+1, right, num)
    else:
        ret = binarySearch(left, mid-1, num)
    return ret

n, arr = int(input()), sorted(list(map(int, input().split())))
m, target = int(input()), list(map(int, input().split()))
answer = {}
for num in target:
    if num not in answer:
        answer[num] = binarySearch(0, n-1, num)
for num in target:
    print(answer[num], end=' ')
print()
'''