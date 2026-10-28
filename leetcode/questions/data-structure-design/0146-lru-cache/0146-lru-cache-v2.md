- Confidence: 3/5
- Result: need review
- Workon: Independently verify operation paths and list-map consistency before declaring completion.

# 146. LRU Cache

## Code

[Python working file](0146-lru-cache-v2.py)

## Session summary

1. Attempt started October 28, 2026 at 5:00:10 PM EDT (America/Toronto).
2. Initially described expiration counters; interviewer clarified recency order rather than elapsed time.
3. Asked about implementation responsibilities, lookup input and return value, runtime requirements, key/value bounds, capacity bounds, repeated writes, and read recency.
4. Independently proposed a node hash map and doubly linked list, then settled on tail as most recently used and head as the eviction end after a question about inconsistent ordering.
5. Proposed add/remove helpers and independently identified the need to store keys in nodes for map deletion during eviction.
6. Discussed replacement versus reuse; interviewer noted allocations and asked whether unlinking destroys the map reference.
7. Explained average constant-time operations through map access and fixed pointer changes, and capacity-proportional storage with two sentinels.
8. An interviewer question about existing-key writes prompted discovery of missing read recency updates; corrected their indentation after a specific interviewer prompt.
9. Added an early return for existing-key writes after interviewer questions and an interviewer-supplied repeated-key scenario exposed fall-through into insertion.
10. Declined an eviction dry run; interviewer respected this and used focused review questions instead.
11. Corrected the eviction map assignment and reversed constructor argument order after interviewer prompts identifying those locations.
12. Declared implementation complete, then requested remaining defects; interviewer identified constructor syntax, sentinel construction, an undefined local tail reference, and helper-name mismatches.
13. Corrected the colon, tail assignment, and helper names; requested exact sentinel-call syntax, received two assisted lines, and applied them.
14. Final saved operations were consistent with the intended cache behavior on inspection.

## Feedback

**Advance this person to the next round?** No for this mock: your core design was appropriate, but completion required meaningful guidance on operation correctness and independent verification was limited.

**Technical: 3 out of 4.** Your final operations are coherent on inspection and your time/space analysis is sound; minor syntax/reference slips carry little weight, but read recency and update fall-through required correction.

**Problem solving: 2 out of 4.** You independently chose the map/list design and key-bearing nodes, but needed repeated prompts to distinguish update from insertion and align the saved implementation with your stated behavior.

**Communication: 3 out of 4.** You drove clarification and explained pointer operations and complexity, though inconsistent end labels and broad descriptions sometimes obscured the exact execution path.

**Things you did well:**

- You asked for runtime requirements and numeric bounds before committing to the design.
- You connected map lookup with direct node access and fixed pointer changes.
- You independently recognized that eviction needs the node's key.

**Areas of improvement:**

- Check that an existing-key write changes neither entry count nor remaining capacity.
- Verify that every successful read actually performs the recency update you describe.
- Separate intended behavior from saved control flow before declaring completion; an eviction walkthrough was declined and no user-reported testing was provided.
- Use consistent most-recent and least-recent labels when describing list operations.

**My advice:** Before declaring completion next time, independently check one existing-key update and one eviction, tracking both the map and list.
