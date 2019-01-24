#INTRODUCTION

The project aim to classify questions in Shut Arambam according to the Halacot that in them.
The goal is when the program take a passage from Shut Arambam it will output the Halaka in it.


# Dependencies
argparse v.1.1
sklearn v.0.20.1
numpy v.1.15.4


# Making The Sets
To make the set I used the Michna Tora from Mechon Mamre (https://www.mechon-mamre.org/i/0.htm) as Michna Tora divided by halacot while containing the Rambam distinctive way of writing.

The program `make_sets.py` build a train and dev sets from the unprocced data sit in `./data/raw data` in a form of folders.

Each folder is the name of one label, in our case one Halaka name.

Each file in the folder is a sample of 100 words from the Rambam (the data do not include chapter indicator).

### Divide the data
The program divide the Rambam into single set according to a divide funcion currently avilable

1. `divideByAmount` - divide the data into x size text sets
2. `divideWithOverlap` - make every x word a set of size y (some of the words will be in two sets or more)

To use a custom made divide function build a function according to the following specifiction.

```
divide funcion
in: data of type [(label, data), (label, data),...] each element diffrent label

out: train and test set. each of form {label:[data1, data2,...], label:[data1, data2,...]} with each label a
diffrent label and datak is the splited data.

```


### Run make_set.py:
To run simply run `python data_handler.py [-h]`.

The program can take the following parameters:

| param | explanation |
| :---: | :--- |
| folder_loc | the location of the raw files |
| files_loc | the location for the train/test sets |
| to_shuffle | whether to shuffle the files sets before splitting theme |
| train_ratio | the percentage of the files sets that will go into the train set |
| divide | the function according to which the files will be divided into sets |
| word_per_set | the number of words in a single set |
| set_every | the number of words to skip when setting a set |


# SVM classification
The program run SVM and LinearSVM on the data. to run use `python svm_classification.py`.

The program has been run on two data splits.
1. The first is a regular split every 100 words - the output in the file `output.txt`
2. The second is a `divideWithOverlap` split every 100 words with 50 overlap - the output in the file `output_overlap_50.txt`

