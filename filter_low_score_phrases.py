import re, random
from pathlib import Path
from typing import List
import pickle
import json
from pprint import pprint
import os, sys


input_dir = Path('models/pathway')
high_quality_phrases = []
abnormal_end_words_pat = re.compile(r'\s*=+$')

thresholds = {
    'AutoPhrase_multi-words': 0.5,
    'AutoPhrase_single-word': 0.9,
}

for file in Path(input_dir).glob('*.txt'):

    if file.stem in thresholds:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                items = line.strip().split(maxsplit=1)
                if len(items) == 2:
                    score = float(items[0])
                    if score > thresholds[file.stem]:
                        phrase = items[1]
                        if abnormal_end_words_pat.search(phrase):
                            print(phrase)
                            phrase = abnormal_end_words_pat.sub('', phrase)
                            if len(phrase) > 1:
                                print(phrase)
                                high_quality_phrases.append(phrase)
                        else:
                            high_quality_phrases.append(phrase)

out_file = input_dir / 'high_quality_phrases.txt'
with open(out_file, 'w', encoding='utf-8') as f:
    for item in high_quality_phrases:
        f.write(f'{item}\n')
