- Confidence: 2/5
- Result: need review
- Workon: Explain the deque invariant and the lifetime of one index before coding.

# 239. Sliding Window Maximum

## Code

[Python working file](0239-sliding-window-maximum-v2.py)

## Session summary

1. Started November 28, 2026 at 11:31:19 AM EST (America/Toronto).

2. You recalled the rescan baseline and described its quadratic worst-case time and linear output space.
   The interviewer confirmed those bounds and clarified that auxiliary space excluding the output is constant.
3. You recalled the monotonic queue idea from the previous session, but did not settle what the queue stores or how entries are removed.
   You ended the attempt and said you planned to watch a video before returning.

4. You returned after watching a video and chose to trace the opening example before implementing.
5. You requested a spaced-repetition retry even if you finish this attempt.
   Earliest retry: November 29, 2026 at 11:54 AM EST (America/Toronto), or 24 hours after any later solve or solution review, whichever is later.

6. You traced the opening example to [4, 5, 5] and described removing smaller candidates from the right.
   You called the maximum the tail even though the trace read it from the left.
   Your example of several ones followed by a two exposed that the left entry should not be removed on every slide.
   The interviewer confirmed that maximum lookup is from the left and prompted you to identify what would tell you whether the left entry had expired.

7. After the expiration prompt, you proposed storing each candidate as a value and index pair.
   The interviewer confirmed that the front expires when its index is strictly before the window's left edge.
8. You considered starting the right pointer at the first full window and identified that this would require preloading its earlier elements.
   When you asked for help, the interviewer suggested starting at zero and asked when to append the first maximum.

9. You identified the first full window at right index k minus one and then said you would return to the video.
10. You chose to store only indices and wrote the deque loop.
    The interviewer asked what would happen when the first expiration check read the empty deque, then prompted you to consider what should be appended on every iteration.
11. You traced the opening example to [4, 5, 5], using right-side removal for smaller candidates and left-side removal for expiration.
    The interviewer pointed out an argumentless append before the loop, which you removed, and flagged the reversed comparison operator.

12. You traced expiration on a descending input, then accounted for the trailing zero after the interviewer asked about the final iteration.
    You explained which index expired and why the final maximum was one.
13. You gave linear time and linear output space, then identified window-sized auxiliary space after the interviewer separated it from the output.
    You initially said each index could be processed k times, then corrected that to once after the interviewer explained the total work.

## Feedback

- **Advance this person to the next round? No.** You completed the optimized solution and traced expiration, but relied on a video and prompts to finish and justify it.
- **Technical: 3 out of 4.** The deque logic handles valid inputs, though the saved method name differs from LeetCode's required entry point.
- **Problem solving: 2 out of 4.** You identified the expiration issue and chose an index-only deque, with help needed to finish the loop and justify its total cost.
- **Communication: 3 out of 4.** You walked through concrete indices and distinguished the two removal conditions in your final trace.
- **Things you did well:** You chose a descending input that exercised expiration without a larger arrival.
- **Areas of improvement:** Check the saved initialization before tracing and explain how many times each index enters and leaves the deque.
- **My advice:** In the spaced retry, explain the deque invariant and the lifetime of one index before coding.
