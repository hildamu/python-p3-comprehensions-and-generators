#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens if evens else []

def test_return_empty_list_if_odds(self):
    '''returns empty list when num_list has no evens'''
    num_list = range(1,10,2)
    assert return_evens(num_list) == []

def make_exclamation(sentence_list):
    if not sentence_list:
        return []
    
    exclamation_sentences = []
    
    for sentence in sentence_list:
        exclamation_sentence = sentence + "!"
        exclamation_sentences.append(exclamation_sentence)
    return exclamation_sentences

assert make_exclamation([]) == []
assert make_exclamation(['I like computers', 'I require coffee', 'Live long and prosper']) == ['I like computers!', 'I require coffee!', 'Live long and prosper!']



def test_return_exclamation_list(self):
    '''returns list of sentences with exclamation marks'''
    sentence_list = [
        "I like computers!",
        "I require coffee!",
        "Live long and prosper!"
    ]
    assert(make_exclamation(sentence_list) == [
        "I like computers!",
            "I require coffee!",
            "Live long and prosper!",

    ])
