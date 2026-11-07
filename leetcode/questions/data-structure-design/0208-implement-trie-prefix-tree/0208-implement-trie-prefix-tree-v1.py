# Implement a word store with these operations:
# insert(word): store a word.
# search(word): return whether the exact word has been inserted.
# startsWith(prefix): return whether any inserted word begins with prefix.
#
# Example:
# insert("apple")
# search("apple") -> True
# search("app") -> False
# startsWith("app") -> True
# insert("app")
# search("app") -> True
"""
Questions:
- range of calls() 30,000 (in total across all three)
- lowercase english letters? yes
- range of word? max 2,000
- required complexity? no
- if the exact word is not inserted returns False
- if it does start with? True if it does not False
- it still counts if it is the exact same
"""

"""
Appraoch (trie):
Time: O(k)
Space: O(k)

Invariance: 
- comprise a tree that is able to hold all combinations of words and using that tree be able to search for them
"""

class Trie:
  def __init__(self, char):
    self.value= char
    self.isWord = False
    self.children = [None for _ in range(26)]    
"""
insert("apple")
['']
[None...]
cur = ['']
"""
class Solution:
  def __init__(self):
    self.tree = Trie('')
  
  def insert(self, word):
    cur= self.tree
    for letter in word:
      letterIndex = (ord(letter)-97)
      if cur.children[letterIndex] == None:
         cur.children[letterIndex]  = Trie(letter)
     
      cur= cur.children[letterIndex]
    
    cur.isWord = True
    
  def search(self, word):
    cur = self.tree
    for letter in word:
      letterIndex = (ord(letter)-97)
      if cur.children[letterIndex] == None:
        return False
      cur= cur.children[letterIndex]
    
    return cur.isWord
  
 def startsWith(self, word):
    cur = self.tree.children
    for letter in word:
      letterIndex = (ord(letter)-97)
      if cur.children[letterIndex] == None:
        return False
      cur= cur.children[letterIndex]
    
    return True
    
      
      
      
    








