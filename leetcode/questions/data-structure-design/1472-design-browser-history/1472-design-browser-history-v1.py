# Model the browsing history of a single tab that starts at a homepage.
# Support visiting another URL and moving back or forward by a number of
# steps. Each move returns the URL where the tab lands.
#
# Start at "home.com"
# Visit "a.com"
# Visit "b.com"
# Back 1 -> "a.com"
# Forward 1 -> "b.com"

"""
Questions:
is the urls wellformed? yes
forward but we dont have anything visited? return Homepage (the location you are at)
no expected mix? yes
specific contraint? no
"""
class Solution:
  def __init__(self, home):
    # space: O(n)
    self.websites = [home]
    self.index = 0
  
  # O(1)
  def visit(self, website):
    if self.index == len(self.websites)-1:
      self.websites.append(website)
    else:
      self.websites = self.websites[:self.index+1].append(website)
      
  # O(1)
  def forward(self, steps):
    newIndex = (self.index + steps)
    if isValidJump(newIndex):
      self.index = newindex
    return self.websites[self.index]  
    
  # O(1)
  def backwards(self, steps):
    newIndex = (self.index - steps)
    if isValidJump(newIndex):
      self.index = newindex

    return self.websites[self.index]
    
  def isValidJump(self, num):
    # checks if the jump is valid
    if (0 <= num < len(self.websites)):
      return True
    else:
      raise TypeError("This is not within range")
      return False
      
      
      
      
  # ----------------
class Solution:
  def __init__(self, home):
    # space: O(n)
    self.websites = [home]
    self.index = 0
    self.maxIndex = 1
  
  # O(n)
  def visit(self, website):
    if self.index == len(self.websites)-1:
      self.websites.append(website)
      self.index += 1
    else:
      self.websites = self.websites[:self.index+1]
      self.websites.append(website)
      self.index = len(self.websites)-1
  
  def forward(self, steps):
    newIndex = (self.index + steps)
    
    if len(self.websites)-1 < newIndex:
      newIndex = len(self.websites)-1

    self.index = newIndex
    return self.websites[self.index]
    
  # O(1)
  def backwards(self, steps):
    newIndex = (self.index - steps)
    if 0 > newIndex:
      newIndex = 0
    
    self.index = newIndex
    return self.websites[self.index]
  