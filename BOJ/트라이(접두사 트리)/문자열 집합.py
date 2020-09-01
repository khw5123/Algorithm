import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.flag = False
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.flag = True

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if curr_node.flag:
            return True
        return False

n, m = map(int, input().split())
trie, answer = Trie(), 0
for _ in range(n):
    trie.insert(input())
for _ in range(m):
    if trie.search(input()):
        answer += 1
print(answer)