#!/usr/bin/env python3
deck = (list(range(1,14)) + ['j1'] + 
        list(range(14,40)) + ['j2'] +
        list(range(40,53)))

#deck = (list(range(1,14)) + ['j1'] + 
#        list(range(14,40)) + ['j2'] +
#        list(range(40,43)))

def move_card(d, card, how_far):
    top_half = d[ : d.index(card)]
    bottom_half = d[d.index(card) + 1 : ]
    if len(bottom_half) >= how_far:
        middle = bottom_half[ : how_far]
        very_bottom = bottom_half[how_far : ]
        return top_half + middle + [card] + very_bottom
    else:
        how_much_further = how_far - len(bottom_half)
        very_top = top_half[ : 1+how_much_further]
        middle = top_half[1+how_much_further : ]
        return very_top + [card] + middle + bottom_half

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

def prettier_list(L):
    SL = [str(e) for e in L]
    S = ''
    for f in SL:
        if len(f) == 1:
            S = S + ' ' + f + ' '
        else:
            S = S + f + ' '
    return S

def one_cycle(d0, print_what = False):
    mj = move_jokers(d0)
    tc = triple_cut(mj)
    cc = count_cut(tc)
    if print_what == 'all':
        print(prettier_list(mj))
        print(prettier_list(tc))
    if print_what == 'all':
        print(prettier_list(cc), '\n')
    if print_what == 'final':
        print(prettier_list(cc))
    return cc

def longest_run(L):
    record_len = 0
    current_len = 0
    for (i, e) in enumerate(L):
        if i == 0 or type(L[i-1]) == str:
            continue
        elif type(e) == str and current_len > record_len:
            record_len = current_len
            current_len = 0
        elif e == L[i-1] + 1:
            current_len += 1
        elif current_len > record_len:
            record_len = current_len
            current_len = 0
        else:
            current_len = 0
    return record_len

print(prettier_list(deck), '\n')
for i in range(40):
    deck = one_cycle(deck, print_what = 'final')
    print('    Iter ' + str(i+1) + ', Longest run:', longest_run(deck), '\n')
