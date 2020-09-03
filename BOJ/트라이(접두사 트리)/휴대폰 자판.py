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
        result = 0
        curr_node = self.head
        for char in string:
            curr_node = curr_node.children[char]
            if len(curr_node.children) > 1:
                    result += 1
            elif curr_node.flag:
                result += 1
        return result

while True:
    try:
        trie, answer, words = Trie(), 0., []
        n = int(input().rstrip())
        for _ in range(n):
            word = input().rstrip()
            trie.insert(word)
            words.append(word)
        for word in words:
            answer += trie.search(word)
        answer /= n
        print('%.2f' % round(answer, 2))
    except:
        break