#!/usr/bin/env python

# Simple feature extractor for CRFsuite. Based on example/ner.py in the
# CRFsuite distribution (https://github.com/chokkan/crfsuite).

import crfutils

input_columns = 'word lemma soundex pos chunk y'

attribute_templates = [
    [['word',     0]], [['word', -1]], [['word', 1]],
    [['lemma',    0]],
    [['soundex',  0]],
    [['pos',      0]],
    [['chunk',    0]],
]

def feature_extractor(sentence):
    crfutils.apply_templates(sentence, attribute_templates)

crfutils.main(feature_extractor, fields=input_columns, sep='\t')
