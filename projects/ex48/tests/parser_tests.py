from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def test_parser():
    sentence = "the bear eat the honey"
    word_list = lexicon.scan(sentence)
    sen = parser.parse_sentence(word_list)
    assert_equal(sen.subject,'bear')
    assert_equal(sen.verb,'eat')
    assert_equal(sen.object,'honey')
