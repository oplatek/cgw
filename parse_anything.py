#!/usr/bin/env python3.9
"""
Could be used as
  python3.9 sentence2grammar.py example_sentences.txt filtered.txt S2_new.gr ; cat S2_new.gr
"""
import sys
non_terminals = set([])
terminals = set([])

def is_nonterminal(x):
    return x in non_terminals

def is_terminal(x):
    return not is_nonterminal(x)

with open("Vocab.gr") as vocabf:
    vocab_lines = vocabf.readlines()
    for line in vocab_lines:
        line = line.strip()
        if line.startswith("#"):
            continue
        if len(line) == 0:
            continue
        non_terminals.add(line.split()[1])

    for line in vocab_lines:
        line = line.strip()
        terminals_candidates = line.split()[2:]
        for tc in terminals_candidates:
            if is_terminal(tc):
                terminals.add(tc)

S2_file = sys.argv[2]
with open(S2_file, "wt") as g:
    g.write("1    S2    N N\n")
    g.write("1    S2    N\n")
    for t in terminals:
        g.write(f"1    N {t}\n")
