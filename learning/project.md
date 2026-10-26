# Project: PCIe Link Check

## About me
- I test servers. Each morning I read the logs from the overnight or weekend stress test, decide pass or fail, and report the result.
- After a stress test I check PCIe link speed by hand: `lspci | grep -i <component>` to get bus IDs, then `lspci -s <busID> -vv | grep -i lnksta` on each. I also check `dmesg` for anything strange.
- `lspci` marks the link `(ok)` when it matches what the device supports and shows a downgrade otherwise. That is my pass/fail signal.
- A card with several functions (e.g. Intel X710 at 65:00.0 to 65:00.3) shows up as several lines. I want every function printed.
- I'm comfortable in the terminal and know basic Python, but I can't write code from a blank file yet.
- I want to solve a real work problem and build coding confidence for a job switch.
- I have about 1 hour per day.

## The idea
A Python command-line script. I type `python pcie_check.py nvme` and it finds every matching PCIe device, reads each one's link status, and prints PASS or FAIL per device, with a summary of the failures. It works for any component name (nvme, ethernet, vga, ...).

## MVP
### In
- Run `python pcie_check.py <name>` with any component name.
- Find all matching devices and their bus IDs from `lspci`.
- Read link speed and width (`LnkSta`) for each device, one line per function.
- PASS if the link is `(ok)`, FAIL if downgraded.
- Final summary line: number of failed devices and the bus IDs of the failed ones (e.g. `1 of 4 FAILED: 3b:00.0`).
- Clear message and failure exit status when nothing matches (never fail silently).
- Works on the real test servers (run as root).

### Parking lot (v2)
- Check `dmesg` for PCIe errors.
- Check several components, or all of them, in one run.
- Save a report file / CSV to paste into the daily report.
- Compare against a known-good baseline from before the stress test.
- Colored output.
- Run across many servers at once.

## The trunk — core components
### Git (source control)
The save-and-undo system professionals use. In from day one; also proof of work for job applications.

### Terminal and system commands
The script doesn't read hardware itself. It runs `lspci` and captures what it prints.

### Parsing text
`lspci` output is plain text. The script pulls the bus ID from one line and the `(ok)` or downgraded word from another.

### Logic (pass/fail decisions)
Turning what was read into PASS or FAIL per device, and counting the failures.

### Command-line input
Reading the component name typed after the script name, and handling a missing one.

### Error handling
No matches, `lspci` missing, not running as root. The script must say so loudly, because silence looks like "all good" in a pass/fail report.

### Output
A readable line per device plus the failure summary.

### Running it on the real servers
Getting the script onto the test machines and running it there. This is the deployment step for this project.

How they connect: input → run `lspci` to find bus IDs → run `lspci` per bus ID → parse → decide → print summary.
