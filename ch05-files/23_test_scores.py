#!/usr/bin/env python3

import json
import glob

scores = {}

for filename in glob.glob("scores/*.json"):
    scores[filename] = {}

    with open(filename) as f:
        for result in json.load(f):
            for subject, score in result.items():
                scores[filename].setdefault(subject, [])
                scores[filename][subject].append(score)

for one_class in scores:
    print(one_class)
    for subject, subject_scores in scores[one_class].items():
        min_score = min(subject_scores)
        max_score = max(subject_scores)
        average_score = float(sum(subject_scores)) / len(subject_scores)

        print(
            f"\t{subject}: min {min_score}, max {max_score}, average {average_score}")
