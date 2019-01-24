#!/usr/bin/env python
from collections import defaultdict
from argparse import ArgumentParser
import random
import glob
import re
import os


# Read the raw files into data
def readFolder(folder_loc):
    data_sets = []
    folder_loc += "/*"

    # Run on all files in the given folder and set every file as a set where the
    #   name of the file is its label.
    for file_loc in glob.glob(folder_loc):
        # Get the label of the data from the file name.
        label = file_loc.split("\\")[1].split(".")[0]

        file_data = ""
        for line in open(file_loc, "r", encoding="utf8"):
            if line != "\n":
                line = line.strip()

                # If the line contain this word its mean its a line describing the following
                #   chapter index (first, second...) thus not part of the text itself.
                if "הלכות" in line:
                    continue
                else:
                    # Take out the index mark.
                    line = line.split("  ", 1)[1]

                    # Take out the symbols in the line
                    line = re.sub('[,.;:)("]', '', line)
                    line = line.replace("--", " ")
                    line = line.replace("-", " ")
                    line = line.replace("  ", " ")

                    # Take out the notes and references marks.
                    line = re.sub(r'\s\([^()]*\)', '', line)
                    line = re.sub(r'\[[^()]*\]\s', '', line)

                    # add to the current words.
                    if file_data:
                        file_data += " " + line
                    else:
                        file_data = line

        data_sets.append((label, file_data))

    return(data_sets)


# The function create a divide function that divide a data into x size sets.
def divideByAmount(word_per_set):
    def ReturnFunc(data):
        data = data.split()
        cur_data = data[0]
        return_data = []

        # Split the data to sets of size word_per_set
        for i, word in enumerate(data[1:], 1):
            if not i % word_per_set:
                return_data.append(cur_data)
                cur_data = word
            else:
                cur_data += " " + word

        # Add the last set if it is bellow word_per_set size and did not added
        #   in the loop
        if cur_data:
            return_data.append(cur_data)
        return return_data

    return ReturnFunc


# The function create a divide function that create a set every x words (some words
#   overlap between sets)
def divideWithOverlap(word_per_set, set_every):
    # Make sure that the parameters will not skip any word
    if set_every > word_per_set:
        raise TypeError("set_every need to be lower than word_per_set or else there are unused words in the data")

    # Make the divide function
    def ReturnFunc(data):
        data = data.split()
        cur_data = data[0]
        return_data = []
        data_size = len(data)

        # Take every set_every word and make a set of size word_per_set
        for i in range(0, data_size, set_every):
            # Handle the last words in the data
            if i + word_per_set >= data_size:
                return_data.append(" ".join(data[i:]))
            else:
                return_data.append(" ".join(data[i:i + word_per_set]))
        return return_data

    return ReturnFunc


# The function divided the data to sets and build the train and test sets.
# NOTE: the shuffle is per label and not on the all set.
def buildSets(data_set, to_shuffle, train_ratio, divide):
    train_set = defaultdict(list)
    test_set = defaultdict(list)

    # Split to train and test sets.
    for label, data in data_set:
        data = divide(data)
        if to_shuffle:
            random.shuffle(data)

        # Spliting to train and test sets
        train_set[label].extend(data[:int(len(data) * train_ratio)])
        test_set[label].extend(data[int(len(data) * train_ratio):])

    return train_set, test_set


# The function write the sets to files
def writeFiles(train_set, test_set, files_loc):
    def writeSet(a_set, loc):
        # Create the folder containing current set.
        if not os.path.isdir(loc):
            os.mkdir(loc)

        # Wrinting the files of the current set.
        for label in a_set:
            label_loc = loc + label + "/"
            if not os.path.isdir(label_loc):
                os.mkdir(label_loc)

            for i, data in enumerate(a_set[label]):
                f = open(label_loc + "#" + str(i) + ".txt", "w", encoding="utf8")
                f.write(data)
                f.close()

    # Create the folder containing the sets.
    if not os.path.isdir(files_loc):
        os.mkdir(files_loc)

    train_loc = files_loc + "/train/"
    writeSet(train_set, train_loc)

    test_loc = files_loc + "/test/"
    writeSet(test_set, test_loc)


# The function run the program and make the sets
# NOTE: the shuffle is per label and not on the all set.
def main(folder_loc, files_loc, to_shuffle, train_ratio, divide):
    raw_data = readFolder(folder_loc)
    train_set, test_set = buildSets(raw_data, to_shuffle, train_ratio, divide)
    writeFiles(train_set, test_set, files_loc)


if __name__ == '__main__':
    parser = ArgumentParser(description="Rambam data handler")
    parser.add_argument("--folder_loc",
                        type=str,
                        default="./data/raw_data",
                        help="the location of the raw files (i.e. before turn to train/test sets)")
    parser.add_argument("--files_loc",
                        type=str,
                        default="./data",
                        help="the location for the train/test sets")
    parser.add_argument("--to_shuffle",
                        action="store_true",
                        help="whether to shuffle the files sets (per label) before splitting theme into train and test sets")
    parser.add_argument("--train_ratio",
                        type=float,
                        default=0.85,
                        help="the percentage of the files sets that will go into the train set (between 0.5 to 0.95)")
    parser.add_argument("--divide",
                        type=str,
                        choices=["divideByAmount", "divideWithOverlap"],
                        default="divideByAmount",
                        help="the function according to which the files will be divided into sets")
    parser.add_argument("--word_per_set",
                        type=int,
                        default=100,
                        help="the number of words in a single set")
    parser.add_argument("--set_every",
                        type=int,
                        default=50,
                        help="the number of words to skip when setting a set (or how many words will be overlap from the previous set)")
    parser = parser.parse_args()

    # Check that the train_ratio is in the limits
    if (parser.train_ratio < 0.5) or (parser.train_ratio > 0.95):
        raise ValueError("train_ratio need to be between 0.5 to 0.95")

    # Make the divide function
    if parser.divide=="divideByAmount":
        divide = divideByAmount(parser.word_per_set)
    elif parser.divide=="divideWithOverlap":
        divide = divideWithOverlap(parser.word_per_set, parser.set_every)

    # Run the program itself with the parameters
    main(parser.folder_loc, parser.files_loc, parser.to_shuffle, parser.train_ratio, divide)