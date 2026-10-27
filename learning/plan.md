# Learning plan: PCIe Link Check

## Locked decisions
- Language: Python 3, standard library only — already on every server, common in hardware test/validation jobs, nothing to install on servers without internet.
- Data source: run `lspci` via `subprocess` and parse its text — mirrors the manual workflow, and lspci already gives the `(ok)` / downgraded verdict.
- Command-line input: `argparse` — free `--help` and error messages; makes the v2 "several components at once" feature cheap.
- Testing: `pytest` (laptop only) with saved `lspci` output as sample files — the only way to test FAIL paths without a broken server.
- Code hosting: Git + GitHub — backup, and proof of work for the job switch.
- Shape and deployment: one file, `pcie_check.py`, compatible with Python 3.9 (oldest seen on test servers); copied by `git clone`, `scp`, or USB.

## Sections
### 1. Setup  [x] done
**Deliverable:** `python3 pcie_check.py` prints a line, and the project is committed and pushed to GitHub.
**Concepts:** running-a-python-script, git-init, git-commit, git-push, github-repo
- [x] 1.1 Create `pcie_check.py` and run it — it prints one line in your terminal
- [x] 1.2 Turn the folder into a Git repository and make your first commit
- [x] 1.3 Create the GitHub repo and push your first commit to it
- [x] 1.4 The daily loop: change the script, commit, push — see it on GitHub

### 2. Reading your input  [ ] in progress
**Deliverable:** `python3 pcie_check.py nvme` prints `Checking: nvme`, and `--help` shows usage.
**Concepts:** variables, strings, functions, argparse, main-guard
- [x] 2.1 Variables and strings: the script keeps the component name in a variable and prints `Checking: nvme` from it
- [ ] 2.2 Functions: move the printing into a `main()` function and call it — output unchanged
- [ ] 2.3 argparse: read the component name from the command line — `python3 pcie_check.py nvme` prints `Checking: nvme`
- [ ] 2.4 `--help` and the main guard: add help text, protect `main()` with `if __name__ == "__main__":`, commit and push

### 3. Running lspci from Python  [ ] not started
**Deliverable:** `python3 pcie_check.py ethernet` prints the matching lspci lines.
**Concepts:** subprocess, lists, for-loops, case-insensitive-matching

### 4. Pulling out bus IDs  [ ] not started
**Deliverable:** the script prints just the bus IDs (`17:00.0`, `17:00.1`, ...).
**Concepts:** splitting-strings, building-lists, return-values

### 5. Your first tests  [ ] not started
**Deliverable:** `pytest` checks the bus-ID code against saved sample files, all green.
**Concepts:** virtual-environment, pytest, test-files, sample-data

### 6. Reading link status  [ ] not started
**Deliverable:** each device prints PASS or FAIL, including width-only downgrades, with tests for the five sample cases.
**Concepts:** lspci-output-format, substring-search, if-else, booleans, pcie-link-status

### 7. Summary and safety rails  [ ] not started
**Deliverable:** summary line like `1 of 4 FAILED: 3b:00.0`, plus loud errors for no match, not root, or lspci missing.
**Concepts:** f-strings, exit-codes, exceptions, sys-exit, lspci-root-access

### 8. Going live  [ ] not started
**Deliverable:** the script runs on a real test server and matches the result of the manual method.
**Concepts:** copying-to-servers, readme, verifying-against-manual-method, python-version-compatibility

## Test sample cases (for sections 5–7)
1. Healthy output (the X710 sample)
2. One link speed downgraded
3. Width-only downgrade (`Speed ... (ok), Width x4 (downgraded)`)
4. Mixed: 3 ok, 1 downgraded
5. No match (empty output)
6. Not root: `Capabilities: <access denied>`, no `LnkSta` line — must NOT report PASS
