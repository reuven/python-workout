#!/usr/bin/env python3
"""Solution to chapter 5, exercise 23: test_scores"""

import json
import glob


def print_scores(dirname):
    """Takes the name of a directory containing
one or more JSON files with a ".json" suffix.
The files contain test scores in a variety of
subjects.

For each class, the function prints the min,
max, and average score for each subject.
"""

    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) /
                             len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')
