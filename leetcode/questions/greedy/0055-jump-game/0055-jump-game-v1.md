- Confidence: 3/5
- Result: can get with hint
- Workon: Practice turning reachability observations into an invariant and checking exact boundaries independently.

# 55. Jump Game

## Code

[Python working file](0055-jump-game-v1.py)

## Session summary

1. Started November 3, 2026 at 10:56 EST (America/Toronto).
2. Clarified input bounds, jump choices, mutation, and the single-element case.
3. Proposed iterative search and estimated complexity; interviewer asked about repeated indices and when an index is fully explored.
4. Considered marking unsuccessful positions and struggled with tracking completed children; interviewer suggested tracking stack progress and then tracking indices already added to the search.
5. Chose to explore another approach; after an interviewer question about reachable positions, derived a furthest-reach scan.
6. On an interviewer prompt, identified the unreachable-index condition and dry-ran the supplied examples and a single-element case.
7. Implemented the scan and corrected the ending boundary after an interviewer question; discussed linear time and constant space.
8. Interviewer also supplied the scan's initialization and conditions after the user had described them.

## Feedback

1. **Advance this person to the next round? Yes.** The completed implementation and reasoning demonstrate intern-level potential, with meaningful prompts needed to resolve search and boundary details.
2. **Technical: 3 out of 4.** The saved scan handles reachable and unreachable positions with linear time and constant extra space, and the user dry-ran examples and a single-element case.
3. **Problem solving: 2 out of 4.** The user developed a furthest-reach scan after a targeted question, but needed guidance on repeated search states and the ending boundary.
4. **Communication: 3 out of 4.** The user stated constraints, narrated tradeoffs, and explained dry runs, though the invariant and indexing could be more precise.
5. **Things you did well:** Asked about bounds and jump rules, considered recursion depth, and recovered from a difficult implementation by exploring another approach.
6. **Areas of improvement:** Distinguish visiting a state from proving it unsuccessful, and define the invariant and last-index boundary precisely before coding.
7. **My advice:** Practice stating what your tracked value guarantees before and after each iteration, then use that invariant to derive conditions.
