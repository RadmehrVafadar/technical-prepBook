# Design a fixed-capacity key-value cache.
# Reading a key returns its value, or -1 if it is absent.
# Writing a key inserts or updates its value.
# When an insertion exceeds capacity, discard the least recently used key.
# Successful reads and writes count as use.
#
# Example with capacity 2:
# put(1, 10), put(2, 20), get(1), put(3, 30), get(2), get(3)
# Read results: 10, -1, 30
"""
Questions:
- If key not in: return -1
- Writing a key inserts or updates its value
- reads and write count as a use.
- the function put and get must be made
- is there a constrainst for the methods?
  - both meant to be O(1)
- Key constraint: 0-10,000
- Value constraint: 0-100,000
- if duplicate key then we update its value and its cache, 
- dosent add a second copy
- if its same value we just update cache 
- does a get update location in the cache
- capacity 1-3,000
- do we have a dll node class to call on?

Time: O(1)
Space: O(capacity)
"""

class Node:
  def __init__(self, key, val):
    self.val = val
    self.key = key
    self.prev = None
    self.next = None
  


class RLU_Cache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    
    self.hashmap = dict()

    self.head.next = self.tail
    self.tail.prev = self.head
    
  
  def _add(self, node):
    tail = self.tail
    prev_node = tail.prev
    
    prev_node.next = node
    tail.prev = node
    
    node.prev = prev_node
    node.next =  tail
    
  
  def _remove(self, node):
    prev_node = node.prev
    next_node = node.next
    
    prev_node.next = next_node
    next_node.prev = prev_node
    
  
  def put(self, key, value):
      if key in self.hashmap:
        cur_node = self.hashmap[key]
        cur_node.val = value
        self._remove(cur_node)
        self._add(cur_node)
        return
      
      new_node = Node(key, value)
      if self.capacity > 0:
        self._add(new_node)
        self.hashmap[key] = new_node
        self.capacity -= 1
      else:
        leastUsed = self.head.next
        self._remove(leastUsed)
        self._add(new_node)
        
        del self.hashmap[leastUsed.key]
        self.hashmap[key] = new_node
    
  
  def get(self, key):
    if key not in self.hashmap:
      return -1
    cur_node = self.hashmap[key]
    self._remove(cur_node)
    self._add(cur_node)
    return self.hashmap[key].val
    
    
    
    
    
    
    
    
    
    
    
    
    
    