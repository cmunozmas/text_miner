#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 09:11:05 2020

@author: a33272
"""

# Importing necessary library
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
import os
import nltk.corpus# sample text for performing tokenization


text ='''
The Consolidated List of Authorized Vessels is updated daily and represents a dynamic snapshot of the authorized vessel databases at the day users access the CLAV; individual RFMO web sites should be consulted for their definitive lists.
Some vessels may have duplicate entries in the list. Accordingly, the number of entries in the Consolidated List of Authorized Vessels is likely to exceed the actual number of authorized vessels.
The Consolidated List of Authorized Vessels is a work in progress. Any references to it should specify the date on which it was accessed.

'''
# importing stopwors from nltk library
from nltk import word_tokenize
from nltk.corpus import stopwords
#a = set(stopwords.words('english'))
#text1 = word_tokenize(text.lower())
#stopwords = [x for x in text1 if x not in a]
#
## finding the frequency distinct in the tokens
## Importing FreqDist library from nltk and passing token into FreqDist
#from nltk.probability import FreqDist
#fdist = FreqDist(stopwords)
#fdist
#
## To find the frequency of top 10 words
#fdist1 = fdist.most_common(10)
#fdist1

#Tokenize the text
tex = word_tokenize(text)
tex_tag = []
for token in tex:
    tex_tag.append(nltk.pos_tag([token]))

tex_tag_filter = []

i = 0
while i <= len(tex_tag)-3:
    if tex_tag[i][0][1] == 'NN' or tex_tag[i][0][1] == 'NNS' or tex_tag[i][0][1] == 'NNP':
        if tex_tag[i+1][0][1] == 'NN' or tex_tag[i+1][0][1] == 'NNS' or tex_tag[i+1][0][1] == 'NNP' or tex_tag[i+1][0][1] == 'CC' or tex_tag[i+1][0][1] == 'JJ':
            if tex_tag[i+2][0][1] == 'NN' or tex_tag[i+2][0][1] == 'NNS' or tex_tag[i+2][0][1] == 'NNP' or tex_tag[i+1][0][1] == 'CC':
                if tex_tag[i+3][0][1] == 'NN' or tex_tag[i+3][0][1] == 'NNS' or tex_tag[i+3][0][1] == 'NNP':
                    tex_tag_filter.append(tex[i] + ' ' + tex[i+1] + ' ' + tex[i+2] + ' ' + tex[i+3])
                    i += 4
                    continue 
                else:
                    tex_tag_filter.append(tex[i] + ' ' + tex[i+1]+ ' ' + tex[i+2])
                    i += 3
                    continue
               
            else:
                tex_tag_filter.append(tex[i] + ' ' + tex[i+1])
                i += 2
                continue
        else:
            tex_tag_filter.append(tex[i])
            i += 1
            continue

#    if tex_tag[i][0][1] == 'VBN' or tex_tag[i][0][1] == 'VBG' or tex_tag[i][0][1] == 'JJ':
#        if tex_tag[i+1][0][1] == 'NN' or tex_tag[i+1][0][1] == 'NNS' or tex_tag[i+1][0][1] == 'NNP':
#                tex_tag_filter.append(tex[i] + ' ' + tex[i+1])
#                i += 2
#                continue
        
    i += 1
    continue

i = 0
while i <= len(tex_tag)-3:
    if tex_tag[i][0][1] == 'VBN' or tex_tag[i][0][1] == 'VBG' or tex_tag[i][0][1] == 'JJ':
        if tex_tag[i+1][0][1] == 'NN' or tex_tag[i+1][0][1] == 'NNS' or tex_tag[i+1][0][1] == 'NNP':
                tex_tag_filter.append(tex[i] + ' ' + tex[i+1])
                i += 2
                continue
        
    i += 1
    continue
# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(tex_tag_filter)
fdist

# To find the frequency of top 10 words
fdist1 = fdist.most_common(100)
fdist1
