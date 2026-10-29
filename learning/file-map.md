# File map

<!-- Every file/folder is either explained or parked — no mystery boxes. -->
<!-- known: explained in the learner's own words | parked: honest one-liner for now, deep dive scheduled | generated: machine-made, never edit, always rebuildable -->

## /
- pcie_check.py — known (2026-10-27) — the script itself; the one file that goes to the test servers. Reads the component name from the command line with argparse and prints `Checking: <name>`, all inside `main()`. `--help` shows your description and help text. Then it runs `lspci` through `subprocess`, captures its text, splits stdout into a list of lines called `devices`, then loops over it and prints only the lines containing the component name, compared in lowercase (2026-10-29; the stdout/stderr, list and count prints are commented out for now). The main guard at the bottom runs `main()` only when the file is run directly, so tests can import it → [[running-a-python-script]] [[functions]] [[argparse]] [[main-guard]] [[subprocess]]
- .gitignore — known (2026-10-27) — names Git should ignore; for now just `__pycache__/` → [[gitignore]]
- __pycache__/ (root and learning/scratch/) — generated (2026-10-27) — Python's compiled copies, made on import. Never edit, ignored by Git, always rebuildable
- learning/scratch/main-guard.py — known (2026-10-27) — drill: print `__name__` and run a fan check only under the main guard → [[main-guard]]
- learning/scratch/fan_tools.py — known (2026-10-27) — drill 2: same as main-guard.py, with an importable name → [[main-guard]]
- learning/scratch/run_fans.py — known (2026-10-27) — drill 2: imports fan_tools to show `__name__` becomes `fan_tools` → [[main-guard]]
- learning/scratch/ — known (2026-10-26) — your practice files for drills; never part of the real script
- learning/scratch/variables.py — known (2026-10-26) — drill: build a PCIe address like `3b:00.1` from variables → [[strings]]
- learning/scratch/functions.py — known (2026-10-27) — drill: one function that prints a line per slot number, called three times → [[functions]]
- learning/scratch/argparse_drill.py — known (2026-10-27) — drill: read one bus ID from the command line and print it in capitals. Not named `argparse.py`, which would hide the real module → [[argparse]]
- learning/scratch/argparse_link.py — known (2026-10-27) — drill: two command-line arguments (bus ID, link speed) in one sentence → [[argparse]]
- learning/scratch/lists.py — known (2026-10-29) — drill: a list of fan speeds, printing the count, first and last → [[lists]]
- learning/scratch/for-loops.py — known (2026-10-29) — drill: loop over three temperature readings and print one line each → [[for-loops]]
- learning/project.md — known (2026-10-16) — your project, MVP, and trunk
- learning/plan.md — known (2026-10-26) — the build plan and locked decisions
- learning/knowledge-graph.md — known (2026-10-26) — the living map of what you actually know
- learning/file-map.md — known (2026-10-26) — this file: why every file in the repo exists
- .git/ — generated (2026-10-26) — hidden folder where Git stores every commit; this is what makes the folder a repo. Never edit by hand → [[git-init]]

<!-- Outside the project: ../git-practice/ is a throwaway Git practice repo, not part of this project. -->
<!-- Outside the project: ../fake-github.git/ is a bare repo acting as git-practice's "GitHub" (its origin). Throwaway. -->

## GitHub
- origin → https://github.com/thanhtunggc92/PCIe_check — the online copy of this repo; `git push` sends commits here → [[git-remote]]

