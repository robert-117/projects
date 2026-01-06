
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

parser = argparse.ArgumentParser()
parser.add_argument("file")
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
   elif format_detector() == "syslog": # perform logic from
       syslog_parser()
   else:
       print(format_detector())

def syslog_parser():
    pass

def json_parser():
    with open(args.file) as f:
        for line in f:
            data = json.loads(line)
        return data



if __name__ == "__main__":
    main()
