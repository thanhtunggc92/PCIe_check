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
- status: practicing
- depends-on: standard-library, terminal-commands
- introduced: 2026-10-26
- last-reviewed: 2026-10-28
- evidence: decision 2. Thought logic carries the load; corrected — choosing lspci shifts work to parsing text. Lesson 3.1 (2026-10-27/28): wrote `import subprocess` and `subprocess.run([...], capture_output=True, text=True)` + `print(.stdout)` themselves; first put a shell pipe in the list (`"lspci","|","grep",...`) → empty stdout. Printed `.stderr` when asked and saw lspci's usage text; told the pipe is a shell feature. Fixed to `["lspci"]`, predicted correctly it prints the lspci output. Forward check (remove capture_output): said "same output as before" — half right (screen shows the list, but missed that `.stdout` becomes None).

## argparse
- status: practicing
- depends-on: standard-library, strings
- introduced: 2026-10-26
- last-reviewed: 2026-10-27
- evidence: decision 3. Answered a scope question instead of the forward check; explained how argparse makes multi-name input cheap. 2026-10-27 (lesson 2.3): said they had never used it. Drill 1 (scratch/argparse_drill.py): one positional + `.upper()`, predicted output correctly (named the arg `component` though it held a bus ID). Drill 2 (scratch/argparse_link.py): two positionals; predicted correctly that leaving one out gives an error about the missing one. Project: wrote `import argparse` and the parser/add_argument/parse_args lines in `main()` themselves, replacing `input()`; ran `python3 pcie_check.py nvme` → `Checking: nvme`. Predicted correctly that two words give an error ("unrecognized arguments"). Names the parser `parse` (tip: `parser`). 2026-10-27 (lesson 2.4): said "not sure" what `--help` would print. Added `description=` and `help=` (with examples nvme, mellanox) themselves; ran `--help` and saw both.

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
- status: practicing
- depends-on: git-commit
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: correctly reasoned: clone where servers have internet, USB where not. Created PCIe_check on GitHub and pushed to it on their own; checked that pcie_check.py on GitHub matched the laptop after pushing 7fbde41.

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
- evidence: predicted commit would push to GitHub (wrong; corrected: commit is local, push needs a remote). Hit "pathspec" error from missing `-m`, fixed it after a pointer to the example. Made two practice commits, read `git log --oneline`. Chose to commit `learning/` publicly ("people will understand my process"). Made first project commit c2159f5. Forward check: correctly said the commit would be lost if the disk died because it lives only on the laptop. 2026-10-26 (lesson 1.4): staged and committed 4 files as 7fbde41 with their own message ("second commit"; tip given to describe the change). 2026-10-29 (lesson 3.4): unprompted, committed 7 files as 2b5422a with a descriptive message ("print out the component output"), pushed, and showed `git status` as clean. Included `.claude/settings.local.json` without checking what it was.

## git-push
- status: understood
- depends-on: git-commit, git-remote
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: self-reported prior knowledge. Did 1.3 on their own (`git push -u origin main`). Own explanation: push copies the project to GitHub so it survives a dead laptop — did not say "commits only". Drill: pushed git-practice to a local bare repo; predicted correctly that an uncommitted edit would not be pushed ("Everything up-to-date"). Pushed 7fbde41 and checked the file on GitHub.

## git-remote
- status: practicing
- depends-on: git-init
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: 2026-10-29: pushed 2b5422a to origin on their own (`018dd34..2b5422a main -> main`). Earlier: listed init → add → commit → push without the `git remote add` step. When asked what a push from a fresh repo would do, said Git would read `origin` as master/main (confused remote with branch); corrected. Then ran `git remote add origin ../fake-github.git` and pushed in the drill.

## git-status
- status: introduced
- depends-on: git-commit
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: predicted every tracked file would show as modified (wrong); then guessed project.md was missing because it is "hidden" (wrong). Corrected: modified = changed since last commit.

## variables
- status: understood
- depends-on: running-a-python-script
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: self-reported prior knowledge ("used them before, small Python projects"). Drill (scratch/variables.py): stored bus/device/function in variables and joined them. Lesson 2.1: first named the variable after its value (`NVMe`); after two nudges renamed it to `Componet`, describing its job.

## strings
- status: understood
- depends-on: variables
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: self-reported prior knowledge. Drill: joined strings with `+`, first wrote `:` where `.` was needed, spotted and fixed it; predicted `len()` = 7 correctly. Predicted `Checking: nvme` correctly before running pcie_check.py.

## keyboard-input
- status: practicing
- depends-on: variables, strings
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: switched pcie_check.py to `input()` on their own in lesson 2.1; ran it and typed `nvme`. Replaced by argparse in 2.3 (2026-10-27); no longer in the script.

## functions
- status: understood
- depends-on: variables
- introduced: 2026-10-27
- last-reviewed: 2026-10-27
- evidence: self-reported prior knowledge ("used function before on my old script"). Drill (scratch/functions.py): wrote `slot_num(n)` and called it with 3 values — worked; stored the calls in variables (holds None — return values come in section 4). Lesson 2.2: wrote `def main():`, indented the body, added the `main()` call; typed under the TODO markers instead of replacing them, removed them when asked. Predicted correctly that deleting `main()` would print nothing because the function is never called.

## main-guard
- status: practicing
- depends-on: functions
- introduced: 2026-10-27
- last-reviewed: 2026-10-27
- evidence: said it was new. Drill 1 (scratch/main-guard.py): first printed `"__name__"` in quotes (text, not the value); then assigned `__name__="nvme"` and saw the guard go false — could not say why, walked through it. Fixed it; predicted `__name__` + "Fan check" correctly. Drill 2 (fan_tools.py + run_fans.py): predicted `__main__` + "Fan check" on import (wrong, got `fan_tools`); then explained in own words: imported, not run directly, so `__name__` isn't `__main__` and the function isn't called. Project: wrapped `main()` in `if __name__ == "__main__":` themselves; predicted correctly that `import pcie_check` prints nothing.

## gitignore
- status: introduced
- depends-on: git-status
- introduced: 2026-10-27
- last-reviewed: 2026-10-27
- evidence: tutor dictated `.gitignore` with `__pycache__/`; learner created it and saw both `__pycache__/` folders drop out of `git status`.

## stdout-stderr
- status: introduced
- depends-on: subprocess
- introduced: 2026-10-27
- last-reviewed: 2026-10-27
- evidence: lesson 3.1: tutor explained the two output streams; learner printed `.stderr` and read lspci's usage text from it.

## lists
- status: understood
- depends-on: variables
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: self-reported prior knowledge ("not new on using the list"). Drill (scratch/lists.py): list of 4 fan speeds (as strings), printed `RPM[0]`, `RPM[-1]`, `len(RPM)`; prediction held. Lesson 3.2: wrote `devices = command.stdout.splitlines()` + `print(devices)` + `print(len(devices))` themselves; predicted correctly that the list prints as separate items instead of one text block (22 devices). Forward check: said empty lspci output would give `None` (wrong — `[]` and `0`; shown and explained).

## for-loops
- status: understood
- depends-on: lists
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: self-reported prior knowledge ("also not new on a for loop"). Drill (scratch/for-loops.py): looped over 3 temperature readings, printed one line each; predicted "one element per line" correctly. Lesson 3.3: replaced the TODO with `for c in devices:` + `if` + indented `print(c)` themselves. Forward check: said correctly that an empty list makes the loop print nothing.

## case-insensitive-matching
- status: practicing
- depends-on: strings
- introduced: 2026-10-26
- last-reviewed: 2026-10-29
- evidence: added `.lower()` to the printed name on their own in lesson 2.1 (normalising "NVMe" → "nvme"). 2026-10-29 (lesson 3.3): unprompted, lowercased both sides of the match (`args.component.lower() in c.lower()`). 2026-10-29 (lesson 3.4): broke it on purpose — removed `.lower()` from the line side themselves and predicted correctly that `micron` would match nothing (line says `Micron`); restored it and saw the drive line. The why (m ≠ M) was explained by the tutor, not in their own words yet.

## splitting-strings
- status: practicing
- depends-on: strings, lists
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: lesson 3.2: tutor named `.splitlines()` (cuts text at line breaks, returns a list); learner used it on `command.stdout`. Lesson 4.1 (2026-10-29): said they had used `.split()` "before but not much". Drill (scratch/splitting-strings.py): split `"Fan2 RPM 5400 ok"` with `.split(" ")`, printed `len(...)` and `[2]`; predicted 4 and the index-2 item correctly. Project: wrote `split_device = c.split()` + `print(split_device[0])` themselves; predicted correctly that `bridge` prints the 5 bus IDs. Forward check (`[1]` on `00:00.0 Host bridge: ...`): said "the next item, the other part" — right idea, not specific; told it is just `Host` because split cuts at every space. Typed under the TODO marker again instead of replacing it.

## building-lists
- status: understood
- depends-on: lists, for-loops
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: self-reported prior knowledge ("I knew them before"). Drill (scratch/building-lists.py): empty list + `.append()` in a loop over 3 fan names, first used `.title()` and left out the count; fixed both to `.upper()` + `len()`, predicted "all in capitals and 3" correctly. Lesson 4.2: wrote `bus_ID=[]` above the loop, `bus_ID.append(split_device[0])` inside the `if`, and both prints after the loop themselves; predicted correctly that `bridge` gives a list of 5 IDs and `5`. Forward check (empty list moved inside the loop): said it resets every pass so the list ends empty. Right mechanism, but missed that the last pass can leave one item.

## return-values
- status: understood
- depends-on: functions
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: self-reported prior knowledge ("I used the return in a function before"). Asked for a clearer drill spec. Drill (scratch/return-values.py): `link_width(current, max)` returns the percentage, caller stores and prints it; predicted `50.0 %` exactly. Lesson 4.3: wrote the body of `find_bus_ids(component, lines)` (moved the loop, switched to `lines`, `return bus_ID`) and the call `bus_ID = find_bus_ids(args.component.lower(), devices)` themselves; typed under the second TODO marker and deleted the two prints, fixed both when pointed out. Predicted the unchanged `bridge` output (5 IDs, 5) correctly. Forward check (delete `return`): said everything shows None. Half right: `bus_ID` is None and prints None, but `len(None)` crashes with TypeError (shown). Note: the function only lowercases the line side; it relies on the caller lowercasing `component`.

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
- status: practicing
- depends-on: strings
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: lesson 3.3: tutor dictated `if ... in line:`; learner wrote `==` instead. Predicted the bridge lines would print (wrong — nothing printed); when asked why, gave an unclear answer. Tutor explained `==` = whole line equals vs `in` = appears inside; learner switched to `in` and saw the 5 bridge lines. Lesson 3.4: predicted `nvme` prints no device line (right, but thought the laptop had no NVMe drive). Shown the `Non-Volatile memory controller` line, explained in own words: the script only prints lines containing the text `nvme`, and this line doesn't contain it. Full teaching in section 6.

## if-else
- status: introduced
- depends-on: booleans
- introduced: 2026-10-29
- last-reviewed: 2026-10-29
- evidence: lesson 3.3: tutor dictated a one-line `if` (glossed: runs the indented lines only when true); learner indented the `print` under it correctly. Not taught yet; section 6.

## booleans
- status: seed
- depends-on: variables
- introduced: —
- last-reviewed: —
- evidence: —

## f-strings
- status: practicing
- depends-on: strings
- introduced: 2026-10-26
- last-reviewed: 2026-10-26
- evidence: wrote `print(f"Checking: {...}")` unprompted in lesson 2.1, ahead of section 7; worked first time.

## exit-codes
- status: seed
- depends-on: running-a-python-script
- introduced: —
- last-reviewed: —
- evidence: 2026-10-27: tutor glossed it when argparse's missing-argument error exited with code 2. Not taught; comes due in section 7.

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
