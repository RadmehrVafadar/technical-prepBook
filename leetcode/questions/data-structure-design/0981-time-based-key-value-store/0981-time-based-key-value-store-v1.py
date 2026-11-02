# Design a store that supports these operations:
# set(key, value, timestamp): store a value for a key at that timestamp.
# get(key, timestamp): return the value stored at the latest timestamp
# less than or equal to the requested timestamp, or "" if none exists.
#
# Example, starting with an empty store:
# set("foo", "bar", 1)
# get("foo", 1) -> "bar"
# get("foo", 3) -> "bar"
# get("foo", 0) -> ""
# set("foo", "bar2", 4)
# get("foo", 4) -> "bar2"
# get("foo", 5) -> "bar2"

"""
Questions:
- will key be string? Yes
- smallest and largest length of key string? 1-100 characters inclusive
- keys are lowercase english letters or digit 1-9. No spaces
- no upper case letters
- will value always be a tring? Yes
- contraint of value string? 1-100 characters (inclusive)
- values are always lowercase english letters and digits 0-9
- what is timestamp value? Integer
- range of the value of timestamp? 1/10^7 (inclusive)
- is there a target Time or Spae for this question? No
- no two set calls will ever share a timestamp
-----------------------------
- do set calls come in timestamp order? Yes
- how many calls does it need to handle? 200,000 calls to set and get
- even with a diffirent key timestamps must increase 
- what would be the maxiumum number of diffirent keys? 200,000 since there can not be more than 200,000 calls
- combined call limit is 200,000 (inclusive)
"""


"""
Approach (brute force):
1. Make a hashmap of key : list
2. when given a timestamp and value fill all of the indicies that equal to are larger to that timestamp with the value untill len of list is 10^7
3. the get function would just grab the key and then the value at the index where the time is
4.If a new value is added with the same key on a later timestamp replate the existing values with the new one starting the new timestamp till 10^7

Better Approach: (worst is filling in the list till 10^7)
1. Making of a hasmpah key : list (values in the list would be the timestamps)
2. There will be another dictionary that would have a key: value where key is "key+timestamp" : value
2. If the key was not in hashamp we add it and add the empty list
3. we would append out new timestamp to the list for that key and also add key+timestamp : value to the master hashmap
3. if the get's index is smaller then the nodes timestamp go to the next node 
4. if the cur nodes timestamp is smaller or equal to, the gets index timestamp then we return the nodes assgined value
5. whenver we are given a set with higher timestamp (this is garanteed so no need to worry abt it so basiclly just whenever we are given a new set for that key) we make a new node and make its next point to the previously set node. 
6. if the node points to a dummy node (we can call it null node ) then just return "".


[3,5] ask 4
  crl 
l
l = 1
r = 0
c = 1

what is a valid condition? 
- if it is in the sorted list
- if it is not in the sorted list then we look for the closest value that is smaller then our target
- we check if the centure is smaller then the target. if it is keep track of the largest value

Time: O(n) # max number of calls if all calls are set() and key's are unique 
Time O(n) * n being the max number of calls 
"""



class TimeMap:
  def __init__(self):
    self.timeSet = {}
  
  def set(self, key, value, timestamp):
    timeSet = self.timeSet
    if key in timeSet:
      timeSet[key].append((timestamp, value))
      return
    
    timeSet[key] = [(timestamp, value)]  
    
 """
 # Example, starting with an empty store:
# set("foo", "bar", 1)
# get("foo", 1) -> "bar"
# get("foo", 3) -> "bar"
# get("foo", 0) -> ""
# set("foo", "bar2", 4)
# get("foo", 4) -> "bar2"
# get("foo", 5) -> "bar2"

timeset = {"foo":[(1, "bar")]}
res = ""
cur_timeline = [(1, "bar")]
max_et = 0
res = 0
l = 0

 """      
  
  def get(self, key, timestamp):
    timeSet = self.timeSet
    if key not in timeSet:
      return ""
# get("foo", 1) -> "bar"
    cur_timeline = timeSet[key]
    
    l, r = 0, len(cur_timeline)-1
    max_eligible_time = 0
    res = ""
    while l <= r:
      c = l + (r-l)//2
      
      if cur_timeline[c][0] == timestamp:
        return cur_timeline[c][1]
      
      elif cur_timeline[c][0] > timestamp:
        r = c - 1
      else:
        if max_eligible_time < cur_timeline[c][0]:
          max_eligible_time = cur_timeline[c][0]
          res = cur_timeline[c][1]
        l = c + 1
      
    return res    
    
        
  








