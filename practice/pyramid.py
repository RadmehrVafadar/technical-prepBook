



"""
input: n : int 
 - Number of levels

output:
n = 3
  *
 ***
*****


n = 5

stars = (n * 2) - 1

    *       1   4
   ***      3   3 
  *****     5   2
 *******    7   1
*********   9
"""


def pyramid(n):
    for i in range(n):
        for _ in range((n-i)-1):
            print(" ", end='')

        for j in range(( (i) *2)-1):

            print("*", end='')
        
        print()




if __name__ == "__main__":
    pyramid(10)
