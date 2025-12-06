import os
import datetime
import argparse

## build argparser to check file extensions
## build out argparser to change between txt and json file extension

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument("x", type=str, help="FROM file extension")
parser.add_argument("y", type=str, help="TO file extension")
parser.add_argument("-t", "--timestamp", help="insert timestamp after file name", action="store_true")
group.add_argument("-v", "--verbose", help="increase verbosity", action="count")
group.add_argument("-q", "--quiet", help="return quietly", action="store_true")

args = parser.parse_args()
answer_x = args.x
answer_y = args.y
timestamp = args.timestamp

def return_file_list():
    pwd = os.getcwd()
    current = os.listdir(pwd)
    time = datetime.datetime.now().strftime("-%Y-%m-%dT%H%M%S")
    x = []
    for file in current:
        if file.endswith(answer_x):
            x.append(file)

    if timestamp == True:
        for stuff in x:
            idx = stuff.index(".")
            timefile = stuff[:idx] + time + stuff[idx:]
            x.append(timefile)
        print(x, timefile)
    return x

def convert_to(return_file_list):
    for file in return_file_list:
        base_name = os.path.splitext(file)[0]
        new_file_path = base_name + answer_y
        os.rename(file, new_file_path)

print(return_file_list())
convert_to(return_file_list())


if args.verbose:
    print(f"{answer_x} extension files have been renamed to {answer_y} extensions")
else:
    print("action completed")







