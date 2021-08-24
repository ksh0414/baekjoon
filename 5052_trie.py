import sys
input = sys.stdin.readline

class Node:
  def __init__(self, key, data = None):
    self.key = key
    self.data = data
    self.children = {}

def insert(trie, string):
  current_node = trie
  for char in string:
    if current_node.data:
      return True
    elif char not in current_node.children:
      current_node.children[char] = Node(char)
    current_node = current_node.children[char]
  current_node.data = string
  return False

for _ in range(int(input())):
  trie = Node(None)
  nums = [input().strip() for _ in range(int(input()))]
  nums.sort()
  for num in nums:
    if insert(trie, num):
      print('NO')
      break
  else:
    print('YES')