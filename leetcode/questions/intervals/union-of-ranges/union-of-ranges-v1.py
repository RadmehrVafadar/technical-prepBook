# Implement a class that acts as a union of ranges.
#
# The class should allow to:
# - Insert ranges into the class.
# - Query the class to check if a particular point is in any of the inserted ranges.
#
# Example:
#
# Ranges Inserted:
#
# 2-5
# 9-13
#
# Points Queried
#
# 0 -> False
# 2 -> True
# 10 -> True




"""
Questions:
input: tuple of ints (start, end)
ouput: none or True or False

classes more insertions then points querried

range of ranges? -10^3-10
any ranges can be given? yes
the start and end wont be wellformed? no

endpoint would not be inclusive

are the overlappings common? yes




"""

# [[4, 8]


class Solution:
  def __init__(self):
      self.intervals = []


  # O(1)
  def insert(self, interval):
     if isValidRange(interval):
       self.intervals.append(interval)

  # O(n)
  def querry(self, num):

     for start, end in self.intervals:
       if start <= num < end:
         return True
     return False

  def isValidRange(interval):
      start, end = interval
      if type(start) is not int() or type(end) is not int() or end < start:
          raise TypeError("Please Insert correct interval")
          return False
      return True


class Solution:
  def __init__(self):
      self.intervals = []

  def insert(self, intervals):
  # same checks as above for inserted
   start, end = interval
   index = bisect_left(self.intervals, start)
   self.intervals.insert(index, (start, end))

  def search(self, num):
     index = bisect_left(self.intervals, num)
     return True if index else False


# [2, 50] [3,7] -> True
# 8
