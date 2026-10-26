# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a quiz -->

## terminal-commands
- status: practicing
- depends-on: none
- introduced: 2026-10-16
- last-reviewed: 2026-10-26
- evidence: uses `lspci`, `grep`, pipes and `dmesg` daily at work. 2026-10-26 review: correctly said `grep nvme` without `-i` finds nothing because NVMe is uppercase. Used `mv`, `cd`, `cd ..` correctly.

## pcie-link-status
- status: introduced
- depends-on: terminal-commands
- introduced: 2026-10-16
- last-reviewed: 2026-10-16
- evidence: explained on their own that `(ok)` next to Speed = pass, otherwise downgraded. Width downgrade not yet discussed by them.

## language-choice-python
- status: introduced
- depends-on: none
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: picked Python over Bash (reason: never wrote Bash). Did not answer when Bash would fit; explained: summary/counting tips it to Python.

## standard-library
- status: introduced
- depends-on: language-choice-python
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: explained as part of decision 1.

## subprocess
- status: introduced
- depends-on: standard-library, terminal-commands
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: decision 2. Thought logic carries the load; corrected — choosing lspci shifts work to parsing text. Revisit in section 3.

## argparse
- status: introduced
- depends-on: standard-library, strings
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: decision 3. Answered a scope question instead of the forward check; explained how argparse makes multi-name input cheap. Revisit in section 2.

## pytest
- status: introduced
- depends-on: functions, virtual-environment
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: decision 4. Could not name sample cases unaided; given six cases.

## sample-data
- status: introduced
- depends-on: pytest, lspci-output-format
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: decision 4 — saving real lspci output to test FAIL paths.

## github-repo
- status: introduced
- depends-on: git-commit
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: correctly reasoned: clone where servers have internet, USB where not.

## copying-to-servers
- status: introduced
- depends-on: github-repo
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: proposed clone/USB on their own; scp mentioned by tutor.

## python-version-compatibility
- status: introduced
- depends-on: language-choice-python
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: checked servers, oldest is Python 3.9. Told 3.10+ features (e.g. `match`) won't run. Note: laptop has Python 3.10.12 — newer than servers; handle in section 5 (venv) / section 8.

## lspci-root-access
- status: introduced
- depends-on: lspci-output-format
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: told that non-root `lspci -vv` shows `<access denied>` and no LnkSta. Needs a real saved sample.

## running-a-python-script
- status: practicing
- depends-on: terminal-commands
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: wrote `print(...)` unprompted (in learning/, moved it to project root). Predicted that running from `learning/` fails because the file isn't there; ran it, saw the "can't open file" error, then ran from project root. Edited the print text and re-ran.

## git-init
- status: practicing
- depends-on: terminal-commands
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: said Git was used long ago, needs relearning. Set global user.name/email/defaultBranch. Ran `git init` in a practice folder and in the project; predicted correctly that all project files would be untracked before `git add`. Renamed `master` → `main` with `git branch -m main`.

## git-commit
- status: practicing
- depends-on: git-init
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: predicted commit would push to GitHub (wrong; corrected: commit is local, push needs a remote). Hit "pathspec" error from missing `-m`, fixed it after a pointer to the example. Made two practice commits, read `git log --oneline`. Chose to commit `learning/` publicly ("people will understand my process"). Made first project commit c2159f5. Forward check: correctly said the commit would be lost if the disk died because it lives only on the laptop.

## git-push
- status: seed
- depends-on: git-commit, github-repo
- introduced: —
- last-reviewed: —
- evidence: —

## variables
- status: seed
- depends-on: running-a-python-script
- introduced: —
- last-reviewed: —
- evidence: —

## strings
- status: seed
- depends-on: variables
- introduced: —
- last-reviewed: —
- evidence: —

## functions
- status: seed
- depends-on: variables
- introduced: —
- last-reviewed: —
- evidence: —

## main-guard
- status: seed
- depends-on: functions
- introduced: —
- last-reviewed: —
- evidence: —

## lists
- status: seed
- depends-on: variables
- introduced: —
- last-reviewed: —
- evidence: —

## for-loops
- status: seed
- depends-on: lists
- introduced: —
- last-reviewed: —
- evidence: —

## case-insensitive-matching
- status: seed
- depends-on: strings
- introduced: —
- last-reviewed: —
- evidence: —

## splitting-strings
- status: seed
- depends-on: strings, lists
- introduced: —
- last-reviewed: —
- evidence: —

## building-lists
- status: seed
- depends-on: lists, for-loops
- introduced: —
- last-reviewed: —
- evidence: —

## return-values
- status: seed
- depends-on: functions
- introduced: —
- last-reviewed: —
- evidence: —

## virtual-environment
- status: seed
- depends-on: running-a-python-script
- introduced: —
- last-reviewed: —
- evidence: —

## test-files
- status: seed
- depends-on: pytest
- introduced: —
- last-reviewed: —
- evidence: —

## lspci-output-format
- status: seed
- depends-on: terminal-commands, pcie-link-status
- introduced: —
- last-reviewed: —
- evidence: —

## substring-search
- status: seed
- depends-on: strings
- introduced: —
- last-reviewed: —
- evidence: —

## if-else
- status: seed
- depends-on: booleans
- introduced: —
- last-reviewed: —
- evidence: —

## booleans
- status: seed
- depends-on: variables
- introduced: —
- last-reviewed: —
- evidence: —

## f-strings
- status: seed
- depends-on: strings
- introduced: —
- last-reviewed: —
- evidence: —

## exit-codes
- status: seed
- depends-on: running-a-python-script
- introduced: —
- last-reviewed: —
- evidence: —

## exceptions
- status: seed
- depends-on: functions
- introduced: —
- last-reviewed: —
- evidence: —

## sys-exit
- status: seed
- depends-on: exit-codes
- introduced: —
- last-reviewed: —
- evidence: —

## readme
- status: seed
- depends-on: github-repo
- introduced: —
- last-reviewed: —
- evidence: —

## verifying-against-manual-method
- status: seed
- depends-on: copying-to-servers
- introduced: —
- last-reviewed: —
- evidence: —

## reading-a-diff
- status: seed
- depends-on: git-commit
- introduced: —
- last-reviewed: —
- evidence: —

## claude-md-agent-memory
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —
