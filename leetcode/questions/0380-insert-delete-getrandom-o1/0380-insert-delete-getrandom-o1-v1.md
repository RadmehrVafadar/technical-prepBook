- Confidence: 4/5
- Result: can get with hint
- Workon: State precisely which value moves, which dictionary key is deleted, and the invariant preserved by removal.

# 380. Insert Delete GetRandom O(1)

## Users Own notes

- Remember that a combiantion of datastructures could also be used eg (hashmap and lists) also remember the flip and pop trick for maintinging O(1)
- Reported struggling with the questions and looking at the topic tags (hashmap and arrays), which helped; reported not viewing the algorithm.

## Code

```python
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
```

## Session summary

- Attempt started October 17, 2026 at 7:39:38 PM EDT (America/Toronto).
- Shared the problem statement and an empty Python 3 class skeleton.
- Restated insert and remove, including their Boolean return values, and described getRandom as choosing a stored value. Stated that all operations must take O(1) time.
- Coach clarified that the bound is average O(1) and that random selection must give each stored value equal probability.
- Independently proposed a Python set with membership checks for insert and remove. Proposed converting the set to a list for random selection and identified that conversion as an O(n) bottleneck for getRandom.
- Reported consulting hashmap and array topic tags after struggling, without viewing the algorithm. Then proposed a list plus a dictionary mapping values to list indices, explained insertion, removal, random indexing, and O(n) storage for n unique elements.
- Submitted the implementation above. Explained constant-time operations, though list append is amortized and dictionary operations are average constant time. The verbal removal description mentioned moving the front value, whereas the code moves the last value and updates its dictionary entry before popping.
- Coach acknowledged the tag assistance separately from the user's subsequent derivation and pointed out the front-versus-last wording discrepancy.
- Correctly dry-ran removing 3 from [1, 3] with {1: 0, 3: 1}: the last element replaces itself, then is popped and deleted from the dictionary. Concluded that both structures remain consistent.
- Explained that the random function chooses indices with equal probability and that the list remains consistent with the dictionary. Coach sharpened the justification by stating that each stored value occupies exactly one index.
- Proposed testing removal of an absent value and insertion of a duplicate. Coach noted that these cover both False return paths and should leave both structures unchanged.
- Correctly gave [9, 7] and {7: 1, 9: 0} after removing 4 from [4, 7, 9]. Mentioned updating 9's index, but verbally said to remove 9 from the hashmap; coach clarified that 4 is deleted while 9 remains.
- User pointed out that the final approach and complexity explanation had already been provided; coach accepted that explanation rather than requiring repetition.

## Feedback

**Advance this person to the next round?**
Yes. For an internship mock interview, you demonstrated a correct implementation and could reason through removal edge cases. This recommendation accounts for your disclosed topic-tag assistance; completely independent discovery was not demonstrated.

**Technical: 3 out of 4.**
You completed a working solution with no identified algorithmic defects. Your list and dictionary updates are consistent, including removal of the last element. You identified O(n) storage and constant-time operations; coach refined append to amortized O(1) and dictionary operations to average O(1). You proposed absent-removal and duplicate-insertion cases and completed verbal removal dry runs. The snippet relies on random being available in the execution environment.

**Problem solving: 3 out of 4.**
You established a set-based baseline and independently identified conversion to a list as the random-selection bottleneck. After consulting topic tags, you derived the index map and last-element replacement operations without being shown the algorithm. You justified the removal cases; your probability explanation needed a small refinement to explicitly connect one index per value to equal probability.

**Communication: 3 out of 4.**
Your approach and complexity explanation were understandable, and you clearly disclosed assistance. Removal wording was occasionally inconsistent with your correct code and final states: front versus last, and deleting the moved value versus the requested value. Shorter, precise descriptions would make your reasoning easier to assess.

**Things you did well:**

- Identified the O(n) conversion bottleneck before choosing the combined structures.
- Implemented the moved value's index update correctly and explained the last-element edge case.
- Disclosed the topic-tag help, making the independence assessment accurate.

**Areas of improvement:**

- Keep removal terminology precise: move the last value, update its index, and delete the requested value. Your code and final states were correct, but your wording sometimes contradicted them.
- State the invariant explicitly: every stored value appears once in the list, and its dictionary entry points to that position.
- Choose cases by the state transitions they exercise, including relocation and removal down to an empty structure.

**My advice:**

- Highest priority: describe removal in three precise sentences while tracking the requested value separately from the moved value.
- On review, reconstruct the implementation without tags and explain the invariant before coding.
- Practice a variation where duplicate values are allowed to check whether you can adapt the representation rather than recall it.
