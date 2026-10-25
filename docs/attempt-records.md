# Attempt records

Each new LeetCode attempt has a Python working file and a separate Markdown record of observations, feedback, and assistance received.

## Why

Preserving retries and distinguishing independent work from assistance makes progress assessments reliable.

## How it works

- Create `leetcode/questions/<category>/<number>-<kebab-case-title>/<number>-<kebab-case-title>-v<N>.md` when an attempt starts.
- For interviewer-selected problems, use a neutral folder and basename such as `leetcode/questions/uncategorized/interview-<timestamp>/interview-<timestamp>-v<N>` during the interview so paths do not reveal the problem or technique.
- Create a `.py` working file beside the Markdown record with the same basename; follow [Interview startup](interview-sessions.md#interview-startup) for prompt contents and presentation.
- After the interview, file both records under the problem's normal category, title, and next available version; preserve the user's Python content unchanged.
- Search existing folders first; reuse the problem's category and increment the highest version for retries.
- Continue the same attempt in its existing files; preserve previous attempts and useful earlier submitted code.
- Keep personal notes in Python comments when the user writes or requests them; do not require a notes section or copy personal notes into Markdown.
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

1. `Code` - a relative link to the attempt's `.py` file, without duplicating code in Markdown; save assistant code only on explicit request, labeled assisted.
2. `Session summary` - concise chronological account of user reasoning, actions, hints, and corrections; distinguish assistance from independent insight.
3. `Feedback` - the interview evaluation when conducted; keep chronology in the summary rather than duplicating it here.

Historical attempts use the same paired-file format.
When migrating an inline record, move existing personal notes into Python comments and preserve earlier code revisions as labeled comments before the latest implementation.
Retain revision descriptions and assistance labels, and leave the latest implementation unchanged.
If no code was submitted, leave the Python file empty rather than inventing an implementation.

In `Session summary`, distinguish user-selected dry runs from interviewer-supplied cases and record what each corrective prompt or hint revealed.
Include observed clarifications and omissions in `Feedback`, especially input bounds, approach tradeoffs, boundary reasoning, and implementation evidence.

### Recording checkpoints

- At startup, initialize the required bullets, title, sections, relative Python link, and start timestamp without invented observations or feedback.
- During the interview, batch observations in context rather than rewriting the record after every exchange.
  Save significant hints, interviewer-supplied corrections or counterexamples, and user corrections about assistance at the next natural pause.
  Flush pending observations before a context handoff or session pause so attribution is preserved.
- At evaluation or session end, read the current saved code as specified in [Interview sessions](interview-sessions.md#during-the-interview), then finalize the assessment bullets, chronology, and feedback once.
  For a paused or unfinished attempt, save only observed progress and keep its status accurate.
- Keep each event in the chronology once; feedback references its impact without repeating the walkthrough.
  Reopen or revise finalized records only for new evidence, corrections, or an explicit request.

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
