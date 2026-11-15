- Confidence: 2/5
- Result: incorrect
- Workon: Trace the exact dictionary lookup in the saved loop on a course with no dependents.

# 210. Course Schedule II

## Code

[Python working file](0210-course-schedule-ii-v1.py)

## Session summary

1. Started November 15, 2026 at 10:14:18 AM EST (America/Toronto).
2. You traced the first example and clarified impossible inputs, both input bounds, the input and output types, whether any valid order is accepted, and whether prerequisite pairs can repeat.
3. You proposed mapping each course to its prerequisites and walked through adding two prerequisite courses before their dependent course.
4. After an interviewer question about shared prerequisites, you proposed checking the output list for duplicates.
5. After prompts about the cost of that check, you identified its linear cost and proposed a set for membership alongside the ordered list.
6. You proposed time proportional to the course and prerequisite counts and revised your space bound to include both after prompts about how many entries the adjacency list stores.
7. You chose to avoid recursive traversal after connecting the course bound to Python's recursion limit.
8. When you asked how to resume a course after investigating an unfinished prerequisite, the interviewer suggested an explicit stack to retain the waiting course.
9. You described resuming the next prerequisite and raised cycle detection independently.
10. The interviewer supplied a two-course cycle and distinguished the active traversal stack from the set of completed courses after you asked which stack was meant.
11. After you asked how to recognize completion, the interviewer walked through keeping the dependent course on the stack and exploring one unfinished prerequisite at a time.
12. You stopped the voice walkthrough and said you would watch a video.
13. You resumed with Kahn's algorithm, using a queue of courses with zero remaining prerequisites and comparing the output length with the course count to detect a cycle.
14. At your request, the interviewer read your saved implementation and asked you to trace the membership check when two courses share a prerequisite.
15. You changed both count assignments to increments and, after a correction, switched the membership check from the input list to the dependents dictionary.
16. After the interviewer showed that checking readiness before decrementing misses the transition to zero, you explained the correct update order and changed the loop.
17. In an interviewer-supplied single-course dry run, you identified the missing dictionary key and attempted to guard the lookup.
18. You requested wrap-up and asked that incidental syntax slips be set aside.

## Feedback

- **Advance this person to the next round?** No. You reached a sound algorithm with assistance, but the saved implementation still fails a basic case.
- **Technical. 2 out of 4.** The queue and length check capture the intended algorithm, but the guard still indexes a missing key even with spelling slips set aside.
- **Problem solving. 2 out of 4.** You connected input scale to recursion depth and identified cycle detection, then needed corrections on the dictionary lookup and the order of count updates.
- **Communication. 3 out of 4.** You clarified the main input and output rules and narrated the single-course dry run clearly enough to identify a missing-key case.
- **Things you did well.** You connected the output length to cycle detection and spotted the empty dependents case during your trace.
- **Area of improvement.** Match the written guard and the returned course ID to your spoken dry run, and update the prerequisite bound in your notes for future reference.
- **My advice.** Trace the exact dictionary expression on a course with no dependents before wrapping up.
