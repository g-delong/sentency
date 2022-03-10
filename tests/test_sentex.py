#!/usr/bin/env python

"""Tests for `sentency` package."""
import spacy
from sentency.sentency import Sentex
from sentency.regex import regexize_keywords

from .config import aaa_keywords, ignore_keywords

def test_sentex():
    text = """
    Screening for abdominal aortic aneurysm. 
    Impression: There is evidence of a fusiform 
    abdominal aortic aneurysm measuring 3.4 cm.
    """
    keyword_regex = regexize_keywords(aaa_keywords)
    ignore_regex = regexize_keywords(ignore_keywords)
    
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('sentex', config={"sentence_regex": keyword_regex, "ignore_regex": ignore_regex})

    doc = nlp(text)

    assert len(doc._.sentex) == 1