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
            if curr_node.flag:
                return False
        curr_node.flag = True
        return True

for _ in range(int(input().rstrip())):
    n, trie, answer = int(input().rstrip()), Trie(), True
    phone_number = sorted([input().rstrip() for _ in range(n)])
    for number in phone_number:
        if not trie.insert(number):
            answer = False
            break
    if answer:
        print('YES')
    else:
        print('NO')
'''
import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
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

    def search(self, string):
        curr_node = self.head
        for char in string:
            curr_node = curr_node.children[char]
        if not len(curr_node.children):
            return False
        return True

for _ in range(int(input().rstrip())):
    n, phone_number = int(input().rstrip()), []
    trie, answer = Trie(), True
    for _ in range(n):
        number = input().rstrip()
        trie.insert(number)
        phone_number.append(number)
    for number in phone_number:
        if trie.search(number):
            answer = False
            break
    if answer:
        print('YES')
    else:
        print('NO')
'''