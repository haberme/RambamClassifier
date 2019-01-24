from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC,SVC, NuSVC
from sklearn.datasets import load_files
from sklearn.pipeline import Pipeline
import numpy as np


def runPipe(svm_name, pipe, param, train_set, test_set, output):
    print("\nstart serching best parameters for {}".format(svm_name))
    grid_search = GridSearchCV(pipe, param, cv=5, error_score=0, n_jobs=-1)
    print("\nfit the train set")
    grid_search.fit(train_set.data, train_set.target)

    out_file = open(output, "a")
    out_file.write("{}\n##############\n".format(svm_name))
    for i in range(len(grid_search.cv_results_['params'])):
        out_file.write("{} #{} param: {}, mean: {:.3f}, std: {:.3f}.\n\n".format(
              svm_name, (i +  1), grid_search.cv_results_['params'][i],
              grid_search.cv_results_['mean_test_score'][i],
              grid_search.cv_results_['std_test_score'][i]))


    predicted = grid_search.predict(test_set.data)
    test_result = np.mean(predicted == test_set.target)
    out_file.write("\n\n test set: {:.2f}\n\n\n\n".format(test_result))

    out_file.close()
    print("the result printed in {}".format(output))
    return grid_search


def main():
    train_loc = "./data/train"
    test_loc = "./data/test"
    output = "output_overlap_50.txt"

    train_set = load_files(train_loc, description="Train", shuffle=False, encoding="utf8", decode_error="ignore", random_state=42)
    test_set = load_files(test_loc, description="Test", shuffle=False, encoding="utf8", decode_error="ignore", random_state=42)

    # Check SVC options
    pipe = Pipeline([
        ('vect', TfidfVectorizer(min_df=3, max_df=0.85)),
        ('clf', SVC()),
    ])
    param = {
        'vect__ngram_range': [(1, 1), (1, 2)],
        'vect__use_idf' : [True, False],
        'clf__C' : [10, 100],
        'clf__kernel' : ['linear', 'poly', 'rbf', 'sigmoid'],
    }
    runPipe("SVC", pipe, param, train_set, test_set, output)

    # Check LinearSVC options
    pipe = Pipeline([
        ('vect', TfidfVectorizer(min_df=3, max_df=0.85)),
        ('clf', LinearSVC()),
    ])
    param = {
        'vect__ngram_range': [(1, 1), (1, 2)],
        'vect__use_idf' : [True, False],
        'clf__C' : [10, 100, 1000],
        'clf__loss' : ['hinge', 'squared_hinge'],
    }
    runPipe("LinearSVC", pipe, param, train_set, test_set, output)


if __name__ == '__main__':
    main()