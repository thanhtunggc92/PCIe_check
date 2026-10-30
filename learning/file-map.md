# File map

<!-- Every file/folder is either explained or parked — no mystery boxes. -->
<!-- known: explained in the learner's own words | parked: honest one-liner for now, deep dive scheduled | generated: machine-made, never edit, always rebuildable -->

## /
- pcie_check.py — known (2026-10-27) — the script itself; the one file that goes to the test servers. Reads the component name from the command line with argparse and prints `Checking: <name>`, all inside `main()`. `--help` shows your description and help text. Then it runs `lspci` through `subprocess`, captures its text, splits stdout into a list of lines called `devices`, then hands the lowercased name and `devices` to `find_bus_ids`. That function, above `main()`, loops over the lines and, for lines containing the name (line lowercased too, so `micron` finds `Micron`), splits the line at spaces, collects the first piece, the bus ID, and returns the list. `main()` keeps it in `bus_ID` and prints it and its length (2026-10-29, lessons 4.1–4.3; the stdout/stderr and device-list prints are commented out for now) → [[return-values]]. The main guard at the bottom runs `main()` only when the file is run directly, so tests can import it → [[running-a-python-script]] [[functions]] [[argparse]] [[main-guard]] [[subprocess]]
- .gitignore — known (2026-10-27) — names Git should ignore; for now just `__pycache__/` → [[gitignore]]
- .claude/settings.local.json — parked (2026-10-29) — Claude Code's saved permission choices for this folder (commands the tutor may run without asking). Not part of the script. Committed in 2b5422a; "local" files usually stay out of Git, so decide whether to add `.claude/` to `.gitignore` the next time we touch it
- __pycache__/ (root and learning/scratch/) — generated (2026-10-27) — Python's compiled copies, made on import. Never edit, ignored by Git, always rebuildable
- learning/scratch/main-guard.py — known (2026-10-27) — drill: print `__name__` and run a fan check only under the main guard → [[main-guard]]
- learning/scratch/fan_tools.py — known (2026-10-27) — drill 2: same as main-guard.py, with an importable name → [[main-guard]]
- learning/scratch/run_fans.py — known (2026-10-27) — drill 2: imports fan_tools to show `__name__` becomes `fan_tools`. Found empty (0 bytes) on 2026-10-29, cause unknown → [[main-guard]]
- learning/scratch/ — known (2026-10-26) — your practice files for drills; never part of the real script
- learning/scratch/variables.py — known (2026-10-26) — drill: build a PCIe address like `3b:00.1` from variables → [[strings]]
- learning/scratch/functions.py — known (2026-10-27) — drill: one function that prints a line per slot number, called three times → [[functions]]
- learning/scratch/argparse_drill.py — known (2026-10-27) — drill: read one bus ID from the command line and print it in capitals. Not named `argparse.py`, which would hide the real module → [[argparse]]
- learning/scratch/argparse_link.py — known (2026-10-27) — drill: two command-line arguments (bus ID, link speed) in one sentence → [[argparse]]
- learning/scratch/lists.py — known (2026-10-29) — drill: a list of fan speeds, printing the count, first and last → [[lists]]
- learning/scratch/splitting-strings.py — known (2026-10-29) — drill: split a fan sensor reading into pieces, print the count and the speed → [[splitting-strings]]
- learning/scratch/building-lists.py — known (2026-10-29) — drill: build a new list of fan names in capitals, print it and its count → [[building-lists]]
- learning/scratch/return-values.py — known (2026-10-29) — drill: a function that returns a link width as a percentage of the maximum; the caller stores and prints it → [[return-values]]
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

