#!/usr/bin/env python3
deck = (list(range(1,14)) + ['j1'] + 
        list(range(14,40)) + ['j2'] +
        list(range(40,53)))

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

def count_cut(d):
    end_val = d[len(d) - 1]
    if end_val == 'j1' or end_val == 'j2':
        end_val = 53
    top = d[ : end_val]
    middle = d[end_val : len(d)-1]
    return middle + top + [end_val]

mj = move_jokers(deck)
tc = triple_cut(mj)
cc = count_cut(tc)

print(deck, '\n')
print(mj, '\n')
print(tc, '\n')
print(cc, '\n')
