- Confidence: 3/5
- Result: need review
- Workon: Define the current subproblem precisely and explain why considering every last coin covers all optimal solutions.

# 322. Coin Change

## Code

[Python working file](0322-coin-change-v1.py)

## Session summary

1. You started Coin Change with the problem statement and an empty Python 3 editor visible in your screenshot.
2. You restated the task as forming the target amount using the available denominations and returning a coin count, or -1 when impossible. Your restatement did not explicitly mention minimizing the count.
3. You asked whether the coins array is sorted; the coach clarified that sorted order is not guaranteed.
4. You asked whether the array can be empty; the coach checked the problem constraints and clarified that it contains at least one denomination.
5. You proposed that coin values must be positive and asked whether the amount can be zero. The coach confirmed both from the constraints and asked you to determine the result for a zero amount.
6. You correctly answered that a zero amount requires zero coins. You also clarified whether denominations can be reused; the coach confirmed unlimited availability.
7. You proposed sorting denominations from largest to smallest, repeatedly taking each coin while it fits, counting coins, and returning -1 if a remainder persists after all denominations. You justified the order by claiming larger denominations require fewer coins, and dry-ran [1, 2, 5] with amount 11 as two fives and one one. You initially described modulus as giving the coin count, although you also correctly described its remainder and repeated subtraction.
8. The coach asked you to dry-run your proposed approach on [1, 3, 4] with amount 6 and compare its count with another combination.
9. You traced four followed by two ones, compared that with two threes, and recognized that your original approach fails to minimize the count.
10. You revised the approach to repeat the descending greedy scan starting at each denomination and keep the smallest valid count. You explained how starting at three fixes the amount-six example.
11. The coach offered [1, 5, 7] with amount 17 to check the revised approach against combinations that use fewer than the maximum number of a starting denomination.
12. You identified seven plus two fives as a three-coin combination and noticed that taking two sevens prevents using fives. Your coin counts during the trace were inconsistent, and you ultimately claimed your procedure would return three. The coach distinguished the combination you found from the choices made by your stated procedure and asked what rule would stop it after one seven.
13. You proposed using modulus, stopping when its result is zero, or moving to a denomination matching its result. The operands and how this rule selects coin counts were not yet clear; the coach asked you to specify the exact first calculation for amount 17 and coin 7.
14. You calculated a remainder of three after taking two sevens, checked whether three was a denomination, and became stuck when it was absent.
15. You requested a hint. The coach suggested considering just one first coin and identifying the remaining task, rather than committing to the maximum number of that denomination.
16. You proposed trying each denomination as one first coin, then scanning denominations to determine how many more coins reach zero. It remained unclear whether the remaining amount could use mixed denominations or reuse the first coin; the coach asked how you would find the fewest coins for the remaining amount ten.
17. You proposed comparing modulus results and choosing the lowest. The coach clarified that modulus measures a remainder and asked you to compare dividing ten into ones versus fives, which both leave zero remainder but use different coin counts.
18. You proposed subtracting the modulus remainder from the amount and dividing by the denomination to calculate its coin count. The coach clarified that this counts coins of one denomination but leaves the remainder unresolved, and offered amount eight with denominations three and five to examine mixed denominations.
19. You confirmed that eight can be formed using the denominations three and five, then requested another hint. The coach suggested assuming the minimum coin counts for smaller remaining amounts were known, and asked how to use the answers for five and three to choose the first coin for eight.
20. You said you would stop the attempt to watch a video explaining the solution. No implementation was submitted, and the final hint was not yet answered.
21. You returned after watching a solution video and reported viewing the approach but not its code. You proposed explaining it before implementing it.
22. You described a decision tree starting from the target amount, branching by subtracting each denomination at every step, stopping negative branches, and comparing successful paths when the remaining amount reaches zero. This approach was learned with video assistance. You had not yet specified how coin counts are tracked or returned, or how an impossible target is represented.
23. You explained that you would minimize the number of coins along a successful path, track it using the tree level, and increment and pass that count when visiting a child node. The coach clarified that repeated coins also count individually and asked for an upper bound on tree depth and branch count before implementation.
24. You considered several complexity expressions and settled on n factorial without defining n or deriving depth and branching. The coach pointed out that reusable coins do not cause the available choices to shrink and asked for the longest successful path when a denomination of one is available.
25. For target eleven with a coin worth one, you correctly identified a longest successful path of eleven coins. You initially answered one choice per node, then clarified that this applies to a single-denomination input; the coach explained that [1, 2, 5] permits up to three choices per node. You then asked whether the complexity is n to the power of n. The coach distinguished the number of denominations from the amount and supplied a loose exponential upper bound.

### New attempt — 2026-10-12

- Started at 2026-10-12 12:37:31 EDT (America/Toronto).
- You asked to try Coin Change again and supplied a screenshot of the statement with an empty Python 3 editor.

- You restated the inputs as integer denominations and an integer target, and the output as the minimum number of coins needed. You correctly stated that an impossible amount returns -1.
- The coach offered a choice between a brute-force approach and dynamic programming before you proposed an approach; you chose to ask clarification questions first.

- You asked whether denominations are sorted, whether their values can be floats, and whether the target can be zero. The coach clarified that sorted order is not guaranteed, denominations are positive integers, and zero is an allowed target.

- You correctly answered that a target of zero requires zero coins.
- You proposed storing minimum coin counts while progressing from smaller amounts toward the target. For amount one with denomination one available, you explained using one coin plus the stored zero-coin answer for the remaining zero.
- While discussing current amount two and denominations [1, 2, 5], you switched to subtracting five from the final target eleven, then described finding unstored remainders. The distinction between computing the current smaller amount and solving the final target remained unclear.

- You asked whether eleven was the target. The coach distinguished the final target eleven from the current subproblem two and asked how much remains after using a coin worth one toward two. You answered nine; the current subproblem and final target were still being mixed together.

- You described choosing a coin worth two for target eleven, counting one chosen coin, and adding the stored minimum coin count for amount two. You proposed moving to another denomination if that stored value was unavailable. The coach focused on which remaining amount the stored answer must represent.

- Asked how much the other coins must form after using a two-dollar coin toward eleven, you correctly answered nine.

- Given a stored minimum of three coins for nine, you correctly added the chosen two-dollar coin to obtain four coins for eleven. You then asked what happens if the answer for nine has not been stored.

- You confirmed that processing amounts in increasing order computes nine before eleven, and connected this to a bottom-up approach after the coach's ordering question.
- You proposed representing unreachable amounts with infinity, also mentioned amount + 1 as a sentinel, and described returning -1 when the final answer remains unreachable. Your explanation suggested unreachable smaller amounts might keep later amounts unreachable; this still needs clarification with a concrete example.
- You offered your code, but the available screen context did not contain an editor or submitted code.

- You submitted a complete Python implementation with an amount + 1 sentinel, a zero base case, increasing amount order, a minimum over valid coin remainders, and -1 for an unchanged final sentinel.
- You correctly stated that denomination two cannot form amount one.

- You dry-ran coins [2] with target four and correctly gave stored counts of five, one, five, and two for amounts one through four. You explained the zero base case for two, compared the unreachable candidate six against sentinel five for three, and combined one chosen coin with the stored one-coin answer for two to form four.

- You explained that a nonzero amount requires a chosen coin plus coins for its remainder, and that the stored minimum for the remainder supplies the best count for that choice. Your explanation did not yet clearly articulate why considering all denominations covers every possible optimal solution.
- You initially gave O(n) time, revised it to O(n*m) with n as amount and m as denomination count, then reverted to O(n) because you thought the coins were checked only once. You gave O(n) space. The repeated inner loop still needs clarification.

- After a concrete loop-count question, you recognized that each amount checks every denomination and stated time as amount times denomination count. Your variable names shifted, but the verbal product was correct.
- You asked what to do next in the interview.

- In the transfer question about using each denomination at most once, you correctly said the current code would not work and explained that choosing two again can reuse a denomination already used in the stored remainder. Your example did not yet specify a complete input and output.

- For coins [2] and target four, you initially mixed the two outcomes, then correctly clarified that the current code returns two while the once-only variation must return -1.

- For the once-only variation, you proposed skipping a coin when subtracting it leaves a remainder equal to that same denomination. This catches a direct pair but does not yet address reuse inside a remainder containing multiple denominations.

- Given denominations [2, 3] and target seven, the coach pointed out that choosing two leaves five, whose stored combination already uses two. You correctly recognized that your proposed equality check would not prevent that reuse.

- You proposed removing a denomination from the coins list after using it to track that it is no longer available. It remains unclear whether this removal is local to one candidate combination or shared across the entire computation.

- You clarified that an alternative combination should start with all coins available and proposed resetting the list when exploring a different alternative.

- Asked whether one stored answer for remaining amount three could represent both an available and an already-used three-dollar coin, you answered yes. The effect of available coins on the state remains unresolved.

- With only a three-dollar coin and remaining amount three, you correctly answered one when the coin is available and -1 when it has already been used. The coach explained that amount alone cannot represent both states; asked what extra state dimension could model availability, you said you did not know.

- The coach suggested processing coins in a fixed order and storing answers restricted to the first few coins. You said you did not know how to continue and asked why these follow-up questions mattered and whether an interviewer would ask them.

## Feedback

**Advance this person to the next round?**
Yes

For an internship interview, your correct implementation, accurate dry run, and eventual explanation support advancing you. This is a mock-interview recommendation. You needed several focused questions to distinguish the current amount from the final target, so this was not a fully independent solve.

**Technical: 3 out of 4.**
You completed a working Python solution with no unresolved implementation defects. Your base case, remainder lookup, minimum update, and impossible-result handling are correct. You accurately dry-ran coins [2] with target four. You corrected time complexity to amount times denomination count after a loop-count question; your space estimate was correct.

**Problem solving: 2 out of 4.**
You proposed building stored answers from smaller amounts before receiving the remainder questions. However, you mixed the final target, current amount, and chosen denomination, and needed repeated concrete questions to resolve which stored answer to use. You then explained one chosen coin plus the minimum for its remainder and demonstrated that unreachable smaller amounts do not prevent later reachable ones. Your correctness explanation still needs a clearer statement that every valid solution has a last coin, and checking all denominations covers that choice.

**Communication: 2 out of 4.**
Your problem restatement and final dry run were clear. Your approach explanation switched between amounts two and eleven, making the state difficult to follow. Your complexity variable names also shifted, although your final verbal product was correct. You appropriately pointed out that you had already explained your approach and costs when the coach asked you to repeat them.

**Things you did well:**

- You explicitly included minimizing the count and returning -1 in your restatement.
- You translated the approach into concise, correct Python code.
- You explained why amount three retains the sentinel while four becomes reachable in your dry run.

**Areas of improvement:**

- Keep the final target, current amount, denomination, and remainder distinct. Mixing them initially led you to look up the chosen denomination instead of the remainder.
- Complete the correctness argument by explaining why every possible optimal solution is represented by one of the coin choices.
- Count nested-loop work before stating complexity. You briefly found the correct product, then incorrectly dropped the inner loop.

**My advice:**

- Highest priority next attempt: define the stored entry in one sentence before describing an update, then use one consistent amount throughout your example.
- For the next three problems with nested loops, state what each loop ranges over and multiply their iteration counts before giving the time bound.
- Revisit this problem with denominations that cannot form every smaller amount, explaining which stored answers remain unreachable and which later ones become reachable.














