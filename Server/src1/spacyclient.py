
# pip3 install spacy
# python3 -m spacy download en_core_web_lg


import spacy
import json
from collections import OrderedDict

class Sclient:
  # print('loading model')
  # nlp = spacy.load('en_core_web_lg')  # will take some time to load
  # print('model loaded')

  def __init__(self):
    print('loading model')
    self.nlp = spacy.load('en_core_web_lg')  # will take some time to load
    print('model loaded')

  # { cmd: foo, text: sometext }
  # @see https://github.com/kengz/spacy-nlp/blob/master/src/py/nlp.py

  def process (self, jsonText) :
    print('A ', jsonText)
    # b'{"cmd": "foo", "text": "co2 causes climate change"}'
    validJson = jsonText # jsonText.decode() #'[' + jsonText.decode() + ']'
    print('B ', validJson)

    # B  {'cmd': 'foo', 'text': 'The pandemic of obesity, type 2 diabetes mellitus (T2DM) and nonalcoholic fatty liver disease (NAFLD) has frequently been associated with dietary intake of saturated fats (1) and specifically with dietary palm oil (PO) (2).'}
    jsonData = jsonText #json.loads(validJson)
    print('C ', jsonData)
    sentence = jsonData["text"]
    doc = self.nlp(sentence)
    reply = OrderedDict([
        ("text", doc.text),
        ("len", len(doc)),
        ("tokens", [token.text for token in doc]),
        ("noun_phrases", [token.text for token in doc.noun_chunks]),
        ("parse_tree", parse_tree(doc)),
        ("parse_list", parse_list(doc))
    ])
    return reply


def merge_ents(doc):
    '''Helper: merge adjacent entities into single tokens; modifies the doc.'''
    for ent in doc.ents:
        ent.merge(ent.root.tag_, ent.text, ent.label_)
    return doc


def format_POS(token, light=False, flat=False):
    '''helper: form the POS output for a token'''
    subtree = OrderedDict([
        ("word", token.text),
        ("lemma", token.lemma_),  # trigger
        ("NE", token.ent_type_),  # trigger
        ("POS_fine", token.tag_),
        ("POS_coarse", token.pos_),
        ("arc", token.dep_),
        ("modifiers", [])
    ])
    if light:
        subtree.pop("lemma")
        subtree.pop("NE")
    if flat:
        subtree.pop("arc")
        subtree.pop("modifiers")
    return subtree


def POS_tree_(root, light=False):
    '''
    Helper: generate a POS tree for a root token.
    The doc must have merge_ents(doc) ran on it.
    '''
    subtree = format_POS(root, light=light)
    for c in root.children:
        subtree["modifiers"].append(POS_tree_(c))
    return subtree


def parse_tree(doc, light=False):
    '''generate the POS tree for all sentences in a doc'''
    merge_ents(doc)  # merge the entities into single tokens first
    return [POS_tree_(sent.root, light=light) for sent in doc.sents]


def parse_list(doc, light=False):
    '''tag the doc first by NER (merged as tokens) then
    POS. Can be seen as the flat version of parse_tree'''
    merge_ents(doc)  # merge the entities into single tokens first
    return [format_POS(token, light=light, flat=True) for token in doc]