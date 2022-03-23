import re, random
from pathlib import Path
from typing import List
import pickle
import json
from pprint import pprint
import os, sys


orig_file = 'data/EN/wiki_quality_orig.txt'
addi_file = 'data/EN/dict_core_expand.txt'
out_file = 'data/EN/wiki_quality.txt'


def merge_dictionary():
    items = []
    with open(orig_file, 'r', encoding='utf-8') as f:
        items.extend(f.readlines())
    with open(addi_file, 'r', encoding='utf-8') as f:
        for lines in f:
            words = lines.split(maxsplit=1)
            if len(words) > 1:
                items.append(words[1])
    with open(out_file, 'w', encoding='utf-8') as f:
        for item in items:
            f.write(f'{item}')


if __name__ == "__main__":
    merge_dictionary()        
