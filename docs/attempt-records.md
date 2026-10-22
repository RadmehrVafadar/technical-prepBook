# Attempt records

Each LeetCode attempt is a separate Markdown record of the user's work and assistance received.

## Why

Preserving retries and distinguishing independent work from assistance makes progress assessments reliable.

## How it works

- Create `leetcode/questions/<category>/<number>-<kebab-case-title>/<number>-<kebab-case-title>-v<N>.md` when an attempt starts.
- Search existing folders first; reuse the problem's category and increment the highest version for retries.
- Continue the same attempt in its existing file; preserve previous attempts and useful earlier submitted code.
- Use the title alone if the number is unknown; use `uncategorized` until the technique is established, then move the whole problem folder without revealing the technique early.
- Treat an unversioned historical file as v1; do not rename or split history unless asked.
- Convert a plain-text attempt to Markdown when continuing it.
- Record each attempt's start in `Session summary`, using America/Toronto with its timezone abbreviation.
- If the start is unknown, record when tracking began and state that the earlier start was not captured.

Start every record with exactly these assessment bullets, followed by `# <number>. <Title>`:

- `Confidence: N/5` - 1 = little evidence/heavy help, 2 = major gaps, 3 = likely with a hint, 4 = mostly independent, 5 = clear independent command; start at 1 without treating it as failure.
- `Result: ...` - `not finished` for unfinished work, `incorrect` for unresolved wrong code, `need review` for substantial help or missing understanding, `can get with hint` for limited help, `clean` for independent correctness and justification.
- `Workon: ...` - one sentence naming the highest-priority observed improvement, or the next reasoning task for a new attempt.

Use these sections in order, leaving them empty until content exists:

1. `Users Own notes` - only the user's comments or explicitly requested notes; preserve wording.
2. `Code` - user-submitted code in fenced blocks; save assistant code only on explicit request and label it assisted.
3. `Session summary` - concise chronological account of user reasoning, actions, hints, and corrections; distinguish assistance from independent insight.
4. `Feedback` - the interview evaluation when conducted; keep chronology in the summary rather than duplicating it here.

## Key files

- `leetcode/questions/` - versioned attempt records.

## Decisions and gotchas

Do not invent user statements, test results, or independent understanding.
Save test results only when user-reported; omit assistant-only test cases, outputs, counts, and verification reports, including from feedback.
Examples discussed with the user may document their reasoning.
Do not label submitted code untested or add assistant-authored proofs, standalone solution explanations, or complexity derivations as session content.
Do not add administrative metadata, placeholders, background, time breakdowns, or self-review sections beyond the required bullets and start timestamp.

## Related

- [Interview sessions](interview-sessions.md)
