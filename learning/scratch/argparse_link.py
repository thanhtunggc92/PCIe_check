import argparse


parser = argparse.ArgumentParser()
parser.add_argument("busid")
parser.add_argument("link")
args= parser.parse_args()

print(f"{args.busid} runs at {args.link}")
