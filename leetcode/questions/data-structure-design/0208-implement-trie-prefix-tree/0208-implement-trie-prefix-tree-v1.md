- Confidence: 2/5
- Result: incorrect
- Workon: Keep traversal state consistent and trace the written implementation through each operation.

# 208. Implement Trie (Prefix Tree)

## Code

[Python working file](0208-implement-trie-prefix-tree-v1.py)

## Session summary

1. Started November 6, 2026 at 7:07:28 PM EST (America/Toronto).
2. Asked about call count, character set, maximum word length, empty words, complexity requirements, missing words, and exact prefix matches.
3. Proposed a trie and described the operation costs; after a prompt, explained marking complete words and distinguishing exact searches from prefix checks.
4. Chose an array of 26 child slots; after prompts about absent children, used None and requested character code points.
5. Implemented the operations and traced an insertion and searches, independently adding the missing end-of-word mark during the trace.
6. After prompts about the initial reference and traversal state, revised insert and search; the session ended before tracing the revised implementation.

## Feedback

**Advance this person to the next round?** No for this mock: the saved prefix operation has a state mismatch, and completing the traversal required guidance; this is a mock recommendation, not a hiring prediction.

**Technical: 2 out of 4.** The core insert and search logic is present, but the prefix operation starts with a list and accesses it as a node, and the revised code was not traced.

**Problem solving: 2 out of 4.** You chose a suitable structure and independently caught the missing word marker, but needed prompts to clarify child slots and maintain consistent traversal state.

**Communication: 3 out of 4.** You asked useful contract questions and explained your decisions and corrections clearly.

**Things you did well:** You clarified the input bounds and exact-match behavior, and identified the missing word marker during your own trace.

**Areas of improvement:** Define what the current variable holds at every step, then trace each written operation through a complete case; distinguish per-operation space from the total space retained by all inserted words.

**My advice:** Before declaring completion, trace each operation using the actual variables and attributes in the code.
