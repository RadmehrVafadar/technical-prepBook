- Confidence: 3/5
- Result: need review
- Workon: Trace a state-changing call followed by a query against the written code before attempting optimization.

# 1472. Design Browser History

## Code

[Python working file](1472-design-browser-history-v1.py)

## Session summary

1. Started November 18, 2026 at 5:03:34 PM EST (America/Toronto).

2. You walked through navigation in both directions and asked about URL validity, starting state, navigation at the boundary, operation frequency, performance targets, and the steps argument.

3. The interviewer supplied the rule that a new visit after going back clears the forward history.

4. You proposed a list and a current index, with visits removing entries after the current page before appending.

5. The interviewer prompted you to check the direction of index changes after you initially described forward as decreasing the index.

6. You replaced repeated pops with a slice and initially called the visit constant time.
   When asked about the slice, you identified that it could copy all N entries.

7. You described navigation that would raise an exception for an out-of-range destination.
   After a prompted forward example, you changed the plan to leave the current page unchanged for an out-of-range destination.

8. The interviewer initially affirmed that behavior in the example with one available step and two requested steps, then corrected the example to require moving to the last available page.
   You traced your current logic and identified that it would leave the page unchanged.

9. You revised forward and backward navigation to stop at the appropriate end of the list.

10. In an interviewer-supplied trace of a visit from the homepage, you identified the missing index update, added it, and traced the revised end-of-list branch.

11. In an interviewer-supplied visit after going back, you traced both the back call and the branch that discards forward history, but treated append as returning the updated list.
    After the interviewer prompted you about the return value, you separated the slice assignment and append.

12. You clarified that you traced the calls by hand.

13. When asked how the caller would supply a different homepage, you revised the constructor to take and store the supplied URL.

14. In a prompted continuation of the visit trace, you explained that going forward after replacing the forward history returns the new page because the index stops at the end.

15. For the optimization follow-up, you proposed replacing the next link in a linked history, then recognized after a question that navigation would take time proportional to the steps moved.

16. You ruled out repeated pops because clearing many entries could still take linear time.

17. The interviewer suggested leaving old entries in the list and overwriting the next slot.
    After a follow-up about unused slots, you distinguished the physical end of the list from the last reachable page and described updating the logical end on each visit.

18. You explained that the optimized list can retain entries beyond the reachable history and distinguished linear total work across many visits from work per navigation call.
    The interviewer named amortized constant time per visit.

19. You ended the mock at your time limit.
    The final file retained the slice-based baseline and an unused maximum-index field.

## Feedback

1. **Advance this person to the next round?** No for this mock.
   The baseline became coherent with multiple interventions on state updates and the append assignment.

2. **Technical: 2 out of 4.** Your final list-and-index logic handles history replacement and clamps navigation, following prompts to correct its state changes and use the supplied homepage.

3. **Problem solving: 2 out of 4.** You chose a viable baseline and identified the navigation cost of linked nodes, then needed hints to reuse list slots and track the last reachable page.

4. **Communication: 3 out of 4.** You clarified important inputs and narrated concrete state values during the hand trace.

5. **Things you did well.** You distinguished the end of the allocated list from the last reachable page and recognized the cost of repeated pops.

6. **Areas of improvement.** Your first trace followed the intended list instead of the value actually assigned by append.
   The final class and back method also use different names from the fixed interface.
   The interviewer initially described the class as optional and confirmed the wrong result for a partial move, so the resulting confusion was not counted against you.

7. **My advice.** Before optimizing, trace a state-changing call and the next query through the written code, naming the values assigned and returned.
