import argparse

def main():
    print("PCIe link check")
    
    parse = argparse.ArgumentParser(description="Check the link speed of the component")
    
    parse.add_argument("component", help="Type the name of the component. EX nvme,mellanox ...")
    args = parse.parse_args()
    print(f"Checking: {args.component.lower()}")

if __name__ == "__main__":
    main()