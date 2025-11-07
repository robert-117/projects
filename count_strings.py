import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument('file')
argparser.add_argument('word', type=str)
argparser.add_argument('-v', '--verbose', action="store_true")
args = argparser.parse_args()

file_name = args.file
word = args.word
verbose = args.verbose

def open_file(file_name, word):
    w = 0
    word = word.lower()
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip().lower()
            if line == word:
                w += 1
    return w

answer = open_file(file_name, word)

if answer == 0:
    print(f"'{word}' was not found in {file_name}")
elif verbose:
    print(f"there are {answer} occurrences of {word} in {file_name}")
else:
    print(answer)