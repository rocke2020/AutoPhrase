import re, random
from pathlib import Path
from typing import List
import pickle
import json
from pprint import pprint
import os, sys
import string

orig_file = 'data/EN/wiki_quality.txt'
orig_file2 = 'data/EN/wiki_quality_orig.txt'
dictionaries_dir = '/home/qcdong/codes/pathway-autoner/data/dictionaries'

alpha_pat = re.compile(r'[a-zA-Z]')
punctuation_pat = re.compile(r'[\W_]')
blank_pat = re.compile(r'\s+')
alpha_or_digits = list(string.digits+string.ascii_letters)


def clean_wiki_quality_phrase():
    items = []
    with open(orig_file, 'r', encoding='utf-8') as orig_f:
        for line in orig_f:
            if len(line.strip()) > 1:
                items.append(line)
    with open(orig_file2, 'w', encoding='utf-8') as f:
        for line in items:
            f.write(line)

def merge_quality_phrases():
    with open(orig_file, 'a', encoding='utf-8') as orig_f:
        for txt_file in Path(dictionaries_dir).glob('*.txt'):
            with open(txt_file, 'r', encoding='utf-8') as f:
                for line in f:
                    orig_f.write(line)


if __name__ == "__main__":
    merge_quality_phrases()
    # clean_wiki_quality_phrase()
    pass
