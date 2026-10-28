import argparse

parser = argparse.ArgumentParser()
parser.add_argument('component')
args= parser.parse_args()
print(f"Bus ID:{args.component.upper()}")