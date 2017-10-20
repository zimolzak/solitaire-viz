#!/usr/bin/env python3
deck = (list(range(1,14)) + ['j1'] + 
        list(range(14,40)) + ['j2'] +
        list(range(40,53)))
print(deck)

def move_card(d, card, how_far):
    top_half = d[ : d.index(card)]
    bottom_half = d[d.index(card) + 1 : ]
    if len(bottom_half) >= how_far:
        middle = bottom_half[ : how_far]
        very_bottom = bottom_half[how_far : ]
        return top_half + middle + [card] + very_bottom
    else:
        raise Exception("Card needs to wrap, len", len(bottom_half), 
                        'how_far', how_far)

def move_jokers(d0):
    d1 = move_card(d0, 'j1', 1)
    d2 = move_card(d1, 'j2', 2)
    return d2

def triple_cut(d):
    x = d.index('j1')
    y = d.index('j2')
    ja = min(x,y)
    jb = max(x,y)
    top = d[:ja]
    middle = d[ja : jb+1]
    bottom = d[jb+1 : ]
    return bottom + middle + top

mj = move_jokers(deck)
print(mj)
tc = triple_cut(mj)
print(tc)
