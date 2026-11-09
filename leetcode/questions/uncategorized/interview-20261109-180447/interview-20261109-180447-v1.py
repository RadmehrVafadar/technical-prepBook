# A bag holds at most capacity items. Each item has weight 1.
# You are given item types, each with a value and an available count.
# Return the maximum total value that can fit in the bag.
#
# Example:
#   values = [6, 10, 3], counts = [2, 1, 5], capacity = 4
#   Output: 25
"""
Question:
value : list of ints
counts : list of ints
capacitu: ints

range len(values)? 1-100,000 (invlusive) 
range len(counts)? 1-100,000 (inclusive)
same length as the values? yes
range of Capacity? 0-10^9
range of values[i]? 0-10^6 (inclusive)
range of counts[i]? 1-10^9
if capacity is zero? return zero?
is values sorted? no
is counts sorted? no
modify values? yes
modify counts? yes
is there an inherit contraint? no
"""






"""
Aproach (add largest value items first and keep going till capacity) 
"""
