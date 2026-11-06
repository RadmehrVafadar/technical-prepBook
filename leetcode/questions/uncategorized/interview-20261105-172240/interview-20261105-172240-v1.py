# Given coin denominations and a target amount, return the number of combinations
# that total the amount. You have an unlimited supply of each denomination.
# Return 0 if no combination makes the amount.
#
# Input: amount = 5, coins = [1, 2, 5]
                              ||
                              1      2
                          1,1  1,2  
                                
# Output: 4
#
# Input: amount = 3, coins = [2]
# Output: 0
"""
- modify? yes
- if does not reach target? return 0
- are values? they are all ints
- range of coin[i]? 1-5,000 (inclusive)
- range len(coins)? 1-300 (inclusive)
- range amount? 0-5,000 (inclusive) 
- when target is zero what to return? returns 1 because adding nothing
- adding nothing only matters when target is zero
- duplicates? no 
- is coins sorted? no
- does the order matter for reaching the target? no
- is there a required time or space complexity? no
"""


"""

coins = [1, 2, 5], amount = 5

dp[0] = 1
d[1] = d[0] = 1 
dp[2] = dp[2-1] + dp[2-2] = d[1] + dp[0] = 1 + 1 = 2
dp[3] = dp[3-1] + dp[3-2] = dp[2] + dp[1] = 2 + 1 = 3



Approach (coin change dp?):


Approach (exhustive?):
1. if the target is zero return 1
2. have an index value start at 0
3. at each index either add the current index to its sum or increase the index then feed the recursion that new index and its cur_sum
4. if at any point the cur_sum is equal to our target. our res variable would increase by one 
5. if the value of cur_sum goes over our target exit out of that branch

Time: O(2^k) #k is the length of coins
Space: O(k) # k is the length of the coins and this is for the calsstack


Invariance: 
- we are going though every valid combination and keeping count of the ones that equal the target.
"""