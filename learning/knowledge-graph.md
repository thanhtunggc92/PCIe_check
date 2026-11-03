# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a quiz -->

## terminal-commands
- status: practicing
- depends-on: none
- introduced: 2026-10-16
- last-reviewed: 2026-11-02
- evidence: 2026-11-02 review (show only LnkSta for 00:1c.0): answered `lspci -s 00:1c -vv | grep -i lnksta` — correct; told that leaving off `.0` matches every function of the device. Lesson 6.1: used `sudo chown user:group` (dictated) to take back a file made in a root shell. Uses `lspci`, `grep`, pipes and `dmesg` daily at work. 2026-10-26 review: correctly said `grep nvme` without `-i` finds nothing because NVMe is uppercase. Used `mv`, `cd`, `cd ..` correctly.

## pcie-link-status
- status: practicing
- depends-on: terminal-commands
- introduced: 2026-10-16
- last-reviewed: 2026-11-02
- evidence: explained on their own that `(ok)` next to Speed = pass, otherwise downgraded. Width downgrade not yet discussed by them. 2026-11-02 (lesson 6.1): compared LnkCap and LnkSta on 00:1c.0 and reported they match (5GT/s, x1). Predicted correctly that 02:00.0's LnkSta would show `(ok)` on both Speed and Width.

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
- status: practicing
- depends-on: functions, virtual-environment, pip-install
- introduced: 2026-10-26
- last-reviewed: 2026-11-02
- evidence: 2026-11-02 (lesson 5.5): ran `pytest` on scratch and project files themselves through three failures and a green run → [[pytest-failure-report]]. 2026-10-30 (lesson 5.4): ran `pytest <file>` on a scratch file and on test_pcie_check.py themselves; read `collected`, the `.` per passing test and the `passed` summary. decision 4. Could not name sample cases unaided; given six cases. 2026-10-30 (lesson 5.2): ran `pip install pytest` in the active venv themselves (pytest 9.2.0 + 7 dependencies). Said "no idea" what `pytest` would print with no tests; ran it, saw `collected 0 items` / `no tests ran`; told pytest only collects `test_*.py` / `*_test.py`. Forward check (new terminal, no activation, type `pytest`): said correctly it won't find it because it's only installed in `.venv`. Note: an older pytest 9.1.1 also sits in `~/.local` (user install, 2026-10-05); the `platform` line shows which one ran.

## pytest-failure-report
- status: practicing
- depends-on: pytest, test-files
- introduced: 2026-11-02
- last-reviewed: 2026-11-02
- evidence: lesson 5.5: said it was new. Drill 1 (scratch/test-files.py): changed `test_fan_num`'s expected value to 3 themselves, ran pytest before predicting, got `.F` / `assert 2 == 3`. Drill 2: broke the function (`< 3000` → `> 3000`), ran before predicting, got `assert 1 == 2`; told the report can't say which side is wrong. Project: chose their own break (`line[1]` in `find_bus_ids`); predicted the left side would still be bus IDs (wrong — `['Host', 'PCI', ..., 'ISA']`, with `At index 0 diff`). Asked why: described what happened (function returned words, test compared) but not the cause; tutor explained `.split()` index 1 = first word of the device type. Restored `line[0]` themselves; `pytest` → 1 passed (ran before predicting). Skipped predictions 3 of 4 times.

## sample-data
- status: practicing
- depends-on: pytest, lspci-output-format, output-redirection
- introduced: 2026-10-26
- last-reviewed: 2026-10-30
- evidence: decision 4 — saving real lspci output to test FAIL paths. 2026-10-30 (lesson 5.3): ran `mkdir samples` (dictated) and wrote `lspci > samples/lspci_laptop.txt` themselves; predicted 22 lines for `wc -l`, reasoning from lesson 3.2's device count — held. Forward check (re-save on a server with the same filename, then run pytest once a test exists): answered about today's state ("zero pass, no tests yet"), missed that the overwritten input would fail the test; told that a sample file is fixed once a test depends on it, so a new machine gets a new filename.

## output-redirection
- status: practicing
- depends-on: terminal-commands
- introduced: 2026-10-30
- last-reviewed: 2026-10-30
- evidence: lesson 5.3: said it was new. Drill 1 (scratch/output-redirection.txt): wrote `ls learning/scratch/ > learning/scratch/output-redirection.txt` + `cat` themselves (ran before predicting); saw the file listed in its own output, told that the shell creates the file before the command runs. Drill 2: predicted correctly that `whoami` into the same file would overwrite the list, leaving only the username. Project: first wrote `lspci > samples/` and got "Is a directory", then fixed it to `samples/lspci_laptop.txt` without help.

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
- status: practicing
- depends-on: lspci-output-format
- introduced: 2026-10-26
- last-reviewed: 2026-11-02
- evidence: told that non-root `lspci -vv` shows `<access denied>` and no LnkSta. Needs a real saved sample. 2026-11-02 (lesson 6.1): asked what "without root" means (told: root = admin account, `sudo` runs one command as root). Ran `lspci -s 2:00.0 -vv` without sudo (called it "the output with root") and noted on their own that there is no LnkCap or LnkSta; tutor pointed to `Capabilities: <access denied>` replacing every capability section. Not saved to a file yet. Worked in a root shell; a file made there was owned by root.

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
- status: understood
- depends-on: git-init
- introduced: 2026-10-26
- last-reviewed: 2026-11-02
- evidence: 2026-11-02 review (commit without `git add` while files are untracked/modified): said nothing new goes in because nothing was fed to the "saving stage" — correct. Earlier: predicted commit would push to GitHub (wrong; corrected: commit is local, push needs a remote). Hit "pathspec" error from missing `-m`, fixed it after a pointer to the example. Made two practice commits, read `git log --oneline`. Chose to commit `learning/` publicly ("people will understand my process"). Made first project commit c2159f5. Forward check: correctly said the commit would be lost if the disk died because it lives only on the laptop. 2026-10-26 (lesson 1.4): staged and committed 4 files as 7fbde41 with their own message ("second commit"; tip given to describe the change). 2026-10-29 (lesson 3.4): unprompted, committed 7 files as 2b5422a with a descriptive message ("print out the component output"), pushed, and showed `git status` as clean. Included `.claude/settings.local.json` without checking what it was. 2026-10-29 (lesson 4.4): unprompted, committed section 4 as 750b930 with a descriptive message ("add find bus id function and return the bus id list") and pushed; showed it with `git log --oneline -3`.

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
- last-reviewed: 2026-10-29
- evidence: 2026-10-29 (lesson 4.4): pushed 750b930. Forward check (commit without push: where do `HEAD -> main` and `origin/main` sit in `git log`?): "not sure"; told that `HEAD -> main` moves to the new commit and `origin/main` stays on 750b930 until the push. Earlier, 2026-10-29: pushed 2b5422a to origin on their own (`018dd34..2b5422a main -> main`). Earlier: listed init → add → commit → push without the `git remote add` step. When asked what a push from a fresh repo would do, said Git would read `origin` as master/main (confused remote with branch); corrected. Then ran `git remote add origin ../fake-github.git` and pushed in the drill.

## git-status
- status: practicing
- depends-on: git-commit
- introduced: 2026-10-26
- last-reviewed: 2026-10-29
- evidence: 2026-10-29 (lesson 4.4): predicted correctly that the three new drill files would show as untracked; did not mention the modified files. Ran `git status` themselves and pasted "nothing to commit, working tree clean" after committing. Earlier: predicted every tracked file would show as modified (wrong); then guessed project.md was missing because it is "hidden" (wrong). Corrected: modified = changed since last commit.

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
- status: practicing
- depends-on: git-status
- introduced: 2026-10-27
- last-reviewed: 2026-10-30
- evidence: 2026-10-30 (lesson 5.1): ran `git status` before predicting, saw `.venv/` untracked; added `.venv` to `.gitignore` themselves (asked only "in the same style") and reported `.venv` gone from untracked. Earlier: tutor dictated `.gitignore` with `__pycache__/`; learner created it and saw both `__pycache__/` folders drop out of `git status`.

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
- evidence: lesson 3.2: tutor named `.splitlines()` (cuts text at line breaks, returns a list); learner used it on `command.stdout`. Lesson 4.1 (2026-10-29): said they had used `.split()` "before but not much". Drill (scratch/splitting-strings.py): split `"Fan2 RPM 5400 ok"` with `.split(" ")`, printed `len(...)` and `[2]`; predicted 4 and the index-2 item correctly. Project: wrote `split_device = c.split()` + `print(split_device[0])` themselves; predicted correctly that `bridge` prints the 5 bus IDs. Forward check (`[1]` on `00:00.0 Host bridge: ...`): said "the next item, the other part" — right idea, not specific; told it is just `Host` because split cuts at every space. Typed under the TODO marker again instead of replacing it. 2026-11-02 (lesson 5.5): broke `find_bus_ids` with `line[1]` and still predicted bus IDs; the result (`Host`, `PCI`, `ISA`) showed index 1 is the first word of the device type — explained by the tutor.

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
- status: practicing
- depends-on: running-a-python-script
- introduced: 2026-10-30
- last-reviewed: 2026-10-30
- evidence: 2026-10-30 (lesson 5.2): drill (scratch/pip-install.py): predicted `/usr/bin/python3` would find the same pip as the venv (wrong — `/usr/lib/python3/dist-packages`); then said `python` uses `.venv` and `python3` the system (half: it's which Python runs, not the name — `.venv/bin/python3` exists too). Forward check correct: a fresh terminal without activation can't see the venv's pytest. Lesson 5.1: said it was new. Drill 1 (scratch/virtual-environment.py): first printed `sys.version`, then `sys.path`, then `sys.executable`; predicted `/bin/python3` correctly. Drill 2 (scratch/venv-home.py): printed `sys.prefix` / `sys.base_prefix` (no labels); predicted both `/usr` outside a venv correctly. Project: ran `python3 -m venv .venv`, listed `.venv` and `.venv/bin`, activated it. Predicted the drill wouldn't run because the file is "outside the box" (wrong — venv isolates Python and packages, not your files). Predicted both prefixes stay `/usr` inside the venv (half: prefix moved to `.venv`); then explained in own words: prefix = from `.venv`, base_prefix = from the laptop. Forward check (new terminal, run `python ...`): said it prints the `.venv` path (wrong — activation is per terminal; plain `python` doesn't exist outside the venv on this laptop).

## pip-install
- status: understood
- depends-on: virtual-environment
- introduced: 2026-10-30
- last-reviewed: 2026-10-30
- evidence: self-reported prior knowledge ("i used it before"). Drill (scratch/pip-install.py): wrote `import pip` + `print(pip.__file__)` correctly, ran it in the venv themselves. Lesson 5.2: ran `pip install pytest` in the active venv and pasted the result.

## python-sys-module
- status: introduced
- depends-on: standard-library
- introduced: 2026-10-30
- last-reviewed: 2026-10-30
- evidence: lesson 5.1: tutor named `sys.executable`, `sys.version`, `sys.prefix`, `sys.base_prefix`; learner found `sys.path` on their own and used the others in drills.

## test-files
- status: practicing
- depends-on: pytest
- introduced: 2026-10-30
- last-reviewed: 2026-10-30
- evidence: lesson 5.4: said it was new. Drill 1 (scratch/test-files.py): wrote `component_value()` returning 4000 + `test_fan_rpm` with `assert ... == 4000` themselves; ran pytest before predicting, 1 passed. Drill 2: wrote `fan_speed_list(fan_list)` (counts speeds < 3000) + `test_fan_num` with a made-up list, asserting 2; skipped the prediction; 2 passed. Project (test_pcie_check.py): first asserted only `len(find_bus_ids("bridge", devices)) == 5`; said correctly that it would not catch a `line[1]` bug. Then built the expected list by re-running the same loop as `find_bus_ids`; when asked what that means, answered off the point ("I can design what the output looks like"); tutor explained that the expected answer must come from outside the code. Then typed the five bridge IDs by hand from the sample; `pytest test_pcie_check.py` → 1 passed. Typed under the TODO marker again. Reads the sample at module level, outside the test function.

## reading-files
- status: practicing
- depends-on: strings, lists
- introduced: 2026-10-30
- last-reviewed: 2026-10-30
- evidence: lesson 5.4: said it was new. Drill 1 (scratch/reading-files.py + temps.txt): wrote `with open("learning/scratch/temps.txt") as f:` + `f.read()` with the correct project-root path; ran it before predicting and asked why `len(temp)` gave 21, not 3; told `len` on a string counts characters; fixed it to `len(temp.splitlines())` → 3 themselves. Drill 2: printed only sensor names using `.split()` + `isalpha()` (own approach, works for these names, misses names with digits); predicted "a new list with only the names" correctly. Project: read samples/lspci_laptop.txt and split it into lines themselves.

## lspci-output-format
- status: practicing
- depends-on: terminal-commands, pcie-link-status
- introduced: 2026-11-02
- last-reviewed: 2026-11-02
- evidence: lesson 6.1: said they only ever read LnkSta, never the full block. Tutor explained: header line, indented block, Capabilities sections, LnkCap vs LnkSta inside Express. Drill 1 (scratch/lspci-output-format.txt): saved `-vv` of 00:1c.0 as root, ran before predicting, pasted LnkCap/LnkSta (including continuation lines). Told: verdict is on the `LnkSta:` line, the indented next line belongs to it; `LnkSta2` also contains "LnkSta", so the script must match `LnkSta:` with the colon. Project: first printed 02:00.0's `-vv` to screen only, then saved it to the project root, then moved it into samples/ (lspci_0200_output.txt).

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
- status: introduced
- depends-on: variables
- introduced: 2026-11-02
- last-reviewed: 2026-11-02
- evidence: lesson 6.2 (in progress): said it was new. Drill 1 (scratch/booleans.py): wrote `link_speed_check(lspeed)` with if/else; predicted "8 fail, 16 pass" (held). First used `== 16`; asked about 32, said on their own that it fails every case except exactly 16, and fixed it to `>=`. Ran before predicting the 32 call. Rewrote it as `return lspeed >= 16` after being shown the shortcut. Drill 2 (unfinished): `link_width_check(cap, sta)` should return True when the LnkSta width is narrower than the LnkCap width. Kept comparing each input to fixed numbers (`>= 16 and >= 4`, then `<= 16 and <= 4`, then 16/4 stored in variables). Explained `and` correctly in own words. Read `True` as "pass" rather than "yes to the function's question" (here, "narrower?"). Said they had been picturing a check against a fixed spec; then asked on their own whether the right check is current width vs LnkCap — yes. Shown a firmware example comparing two parameters. Paused mid-drill 2 to move to the home PC.

## f-strings
- status: practicing
- depends-on: strings
- introduced: 2026-10-26
- last-reviewed: 2026-11-02
- evidence: 2026-11-02 review (drop the `f` from the Checking line): said the value inside the curly brackets would not print. Right idea; told the braces and the code inside them print as plain text. Earlier: wrote `print(f"Checking: {...}")` unprompted in lesson 2.1, ahead of section 7; worked first time.

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
