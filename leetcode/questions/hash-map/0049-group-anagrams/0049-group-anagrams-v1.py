# Given a list of strings, collect together strings that can be formed
# by rearranging one another's letters. Return a list of these groups.
#
# Input: strs = ["arc", "dog", "car", "god", "rat"]
# Output: [["arc", "car"], ["dog", "god"], ["rat"]]
"""
Question:
- are the strings given lowercase english letters? Yes
- do all of the given strings have to have the same length? No
- say I have a string of length 4 string of length 3, do those get grouped together cars and arc? No
- strings in the same group must have the same length? Yes
- for strs[i] what is the contraint? 0-100 chars empty strings are allowed
- how do we handle empty strings? there can be multiple empty strings, they are all in the same group
- could words be the same or are they unique? same string can appear multiple times
- for len strs what is the contraint? 1-10,000
- is there an order? no
- does the output have to have a certain order? No, groups can be in any order and the strings inside can be in any order
- is there an explicit target? no time or space complecity
- can Counter be used?
"""

"""
Approach:
1. For every value in our list, create a Counter (frequency per char) and add to a hashmap
2. If it was already in hashmap we append the list the Counter is attached to
3. if not we add key : value where counter : list containing the words
4. add all of the groups in the hashmap to a list and return list

Time: O(n * m ) # length of list ad m is the strings length
Space: O(n) # length of the list

Invariance:
We would only add to that group if it has the same type and frequency of letters

 
Approach #2:
1. For every value in our list, sort that value
2. have a ditionary with key : value where the key is the sorted character string : list containing the words
3. if the cur sorted string is in the ditionary; add to the keys list and append
4. if not in the ditionary already add it as the key and the word and the first element in the list
5. when gone though the entire strs, we add the values to a results list and return it

time: O(n * klogk) # the max len of a string in the list
space: O(n) 

Invariance:
- subset in the hashmap will always have words grouped together that meet our requirements 
- we return those in one list of lists
"""

"""
DryRun: 
strs = ["arc", "dog", "car", "god", "rat"]
  
word_bucket = {'acr': ['arc', 'car'], 'dgo': ['dog', 'god'] 'art': ['rat'] }
word = "dog"
sorted_word = "dgo"
"""
class Solution:
  def groupAnagrams(strs):
    word_bucket = {}
    
    for word in strs:
      sorted_word = sorted(word)
      sorted_word = "".join(sorted_word)
      if sorted_word in word_bucket:
        word_bucket[sorted_word].append(word)
      else:
        word_bucket[sorted_word] = [word]
    
    res = []
    for value in word_bucket.values():
      res.append(value)
    return res

if __name__ == "__main__":
  strs = ["arc", "dog", "car", "god", "rat"]
  # Output: [["arc", "car"], ["dog", "god"], ["rat"]]

  print(Solution.groupAnagrams(strs))
      




























