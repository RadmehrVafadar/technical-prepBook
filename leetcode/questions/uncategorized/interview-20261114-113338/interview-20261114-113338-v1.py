# You start at index 0 of an integer list. Each element gives the maximum
# distance you can jump forward from that index. Return the fewest jumps
# needed to reach the last index.
#
# [2, 3, 1, 1, 4] -> 2
# [2, 3, 0, 1, 4] -> 2

"""
Questions:
input: list of ints
output: int

range of len(nums)? 1-10,000 (inclusive)
range of nums[i]? 0-1,000 (inclusive)

duplicates? yes
sorted? no
modify? yes

if len(nums) == 1? zero jumps because we are already at the last index

will always reach last index? yes


"""