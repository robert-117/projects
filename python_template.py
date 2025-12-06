import sys, json, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "file")
    args = parser.parse_args()
    with open(args.file) as f:
        for line in f:
            data = json.loads(line)
            # TODO: core logic

if __name__ == "__main__":
    main()
