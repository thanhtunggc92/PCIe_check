import argparse
import subprocess

def main():
    print("PCIe link check")
    
    parse = argparse.ArgumentParser(description="Check the link speed of the component")
    
    parse.add_argument("component", help="Type the name of the component. EX nvme,mellanox ...")
    args = parse.parse_args()
    print(f"Checking: {args.component.lower()}")
    command = subprocess.run(["lspci"], capture_output=True, text=True)
    # print(command.stdout)
    # print(command.stderr)

    devices= command.stdout.splitlines()
    # print(devices)
    # print(len(devices))
    for c in devices:
        if args.component.lower() in c.lower():
            print(c)
if __name__ == "__main__":
    main()