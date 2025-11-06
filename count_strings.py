import argparse
import os
from os import close

argparser = argparse.ArgumentParser()

argparser.add_argument('file')
argparser.add_argument('word', type=str)
args = argparser.parse_args()

file_name = args.file
word = args.word

def open_file(file_name, word):
    w = 0
    with open(file_name) as f:
        for line in f:
            if line == word:
                w += 1
    f.close()
    return w

print(open_file(file_name, word))
