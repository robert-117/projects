
import argparse
parser = argparse.ArgumentParser(description="calculated X to the power  of Y")
group = parser.add_mutually_exclusive_group()

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
group.add_argument("-v", "--verbose", action="count")
group.add_argument("-q", "--quiet", action="store_true")

args = parser.parse_args()
answer = args.x**args.y

def first(answer):
    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power {args.y} equals {answer}")
    else:
        print(f"{args.x}^{args.y} == {answer}")

first(answer)