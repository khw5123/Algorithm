import sys
input = sys.stdin.readline
MAX = 200000

def update(tree, index, diff):
    while index < len(tree):
        tree[index] += diff
        index += (index & (-index))

def _sum(tree, index):
    result = 0
    while index > 0:
        result += tree[index]
        index -= (index & (-index))
    return result

n, answer = int(input()), 1
tree_cost, tree_count = [0]*(MAX+1), [0]*(MAX+1)
for i in range(n):
    coord = int(input())+1
    if i == 0:
        update(tree_cost, coord, coord)
        update(tree_count, coord, 1)
    else:
        tmp = ((coord*_sum(tree_count, coord-1) - _sum(tree_cost, coord-1)) % 1000000007)
        tmp += (((_sum(tree_cost, MAX) - _sum(tree_cost, coord)) - coord*(_sum(tree_count, MAX) - _sum(tree_count, coord))) % 1000000007)
        answer = (answer * tmp) % 1000000007
        update(tree_cost, coord, coord)
        update(tree_count, coord, 1)
print(answer)