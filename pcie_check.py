import argparse
import subprocess

def find_bus_ids(component, lines):
    bus_ID=[]
    for c in lines:
            if  component in c.lower():
    
                line= c.split()
                
                bus_ID.append(line[0])
    return bus_ID
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

    
    bus_ID = find_bus_ids(args.component.lower(),devices)
    print(bus_ID)
    print(len(bus_ID))
    
if __name__ == "__main__":
    main()