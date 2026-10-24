# Personal notes (preserved)

# - Remember that a combiantion of datastructures could also be used eg (hashmap and lists) also remember the flip and pop trick for maintinging O(1)
# - Reported struggling with the questions and looking at the topic tags (hashmap and arrays), which helped; reported not viewing the algorithm.

class RandomizedSet:
    """
    possible data-structures:
     . lists (no go)
        - insert
        - remove
        -
        [1, 3, ]
        {1:0, 3:1}

    """

    def __init__(self):
        self.dict = {}
        self.mylist = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.mylist)
            self.mylist.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            self.dict[self.mylist[-1]] = self.dict[val]
            self.mylist[self.dict[val]] = self.mylist[-1]
            self.mylist.pop()
            del self.dict[val]
            return True

        else:
            return False

    def getRandom(self) -> int:
        return self.mylist[random.randint(0,len(self.mylist)-1)]
