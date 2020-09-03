import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.count = 0
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
        curr_node.count += 1
        return curr_node.count

trie, answer, length = Trie(), {}, 0
while True:
    species = input().rstrip()
    if not species:
        break
    answer[species] = trie.insert(species)
    length += 1

for k, v in sorted(answer.items()):
    print('%s %.4f' % (k, v/length*100))