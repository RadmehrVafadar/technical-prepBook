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
1. Making of a hasmpah key : linked list
2. the node would have the timestamp and the value from its set()
3. if the get's index is smaller then the nodes timestamp go to the next node 
4. if the cur nodes timestamp is smaller or equal to, the gets index timestamp then we return the nodes assgined value
5. whenver we are given a set with higher timestamp (this is garanteed so no need to worry abt it so basiclly just whenever we are given a new set for that key) we make a new node and make its next point to the previously set node. 
6. if the node points to a dummy node (we can call it null node ) then just return "".

Time: O(n) # max number of calls if all calls are set() and key's are unique 
Time O(n) * n being the max number of calls 
"""










