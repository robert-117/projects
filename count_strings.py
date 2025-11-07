import argparse

argparser = argparse.ArgumentParser()

argparser.add_argument('file', help='designated file to search in')
argparser.add_argument('word', help='search for word in file',type=str)
argparser.add_argument('-s', '--case-sensitive', help='enables case sensitivity when searching', action='store_false')
argparser.add_argument('-v', '--verbose', action="store_true")
args = argparser.parse_args()

file_name = args.file
word = args.word
verbose = args.verbose
case = args.case_sensitive

def search_file(file_name, word):
    w = 0
    if case is True:
        word = word.lower()
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip().lower()
                if line == word:
                    w += 1
    else:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line == word:
                    w += 1
    return w

answer = search_file(file_name, word)

if answer == 0:
    print(f"'{word}' was not found in {file_name}")
elif verbose:
    print(f"there are {answer} occurrences of {word} in {file_name}")
elif verbose & case: #TODO: fix output message
    print(f"there are {answer} occurrences of {word} in {file_name} with case sensitivity")
else:
    print(answer)