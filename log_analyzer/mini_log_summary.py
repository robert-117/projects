
# parse two formats from logs (json-per-line + syslog text)

# normalize each line into a common dict

'''
output summary.json with
- total lines
- counts by level
- top 5 repeated messages
- errors-per-minute (bucketed)

output timeline.txt with
- first/last timestamp
- a short list of notable events (WARN/ERROR, sorted by time)
'''
import json, argparse, datetime, re
from collections import Counter

dt = datetime
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-p", "--print", help="Print to stdout", action="store_true")
parser.add_argument("-o", "--output", help="Output to file in current working directory", action="store_true")
args = parser.parse_args()

def format_detector():
    with open(args.file) as f:
        line = f.readline()
        match = re.search(r"^\d{4}-\d{2}-\d{2}", line)
        if line[0] == "{":
            return "json"
        elif match is not None:
            return "syslog"
        else:
            return "error"

def main():
   if format_detector() == "json":
       json_parser()
       # if args.output is True:
       #     with open("summary.json", "w") as f:
       #         f.write(json_parser())
   elif format_detector() == "syslog":
       syslog_parser()
   else:
       print(format_detector())

def syslog_parser():
    pass

def json_parser():
    with open(args.file) as f:
        line_count = 0
        level_list = []
        msg_list = []
        ts_list = []
        for line in f:
            data = json.loads(line)
            line_count += 1
            level_list.append(data["level"])
            msg_list.append(data["msg"])
            ts_list.append(data["ts"])

            if args.print is True:
                print(data)
        level_count = Counter(level_list)
        ts_list.sort()

        print(f"\nNumber of lines found in file: {line_count} lines")
        print(f"\nFound the following number of response codes:")
        for k, v in level_count.items():
            print(f"{k}: {v}")
        print(f"\nFound top 5 most common messges: ")
        for k, num in Counter(msg_list).most_common(5):
            print(f"{num}: {k}")
        print(f"\nFirst timestamp found at {ts_list[0]}\nLast timestamp found at  {ts_list[-1]}")

        return data

print(type(json_parser()))

def json_summary(data):
    pass
    # counter = 0
    # level_list = []
    # for line in data:
    #     counter += 1
    #     level_list.append(data["level"])

if __name__ == "__main__":
    main()
