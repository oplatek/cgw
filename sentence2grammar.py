#!/usr/bin/env python3.9
"""
Could be used as
  python3.9 sentence2grammar.py example_sentences.txt filtered.txt S1_new.gr ; cat S1_new.gr
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


input_sentences_file = sys.argv[1]
out_filtered_file = sys.argv[2]
# print(input_sentences_file)
# print(terminals)
filtered_sentences = []
with open(out_filtered_file, "wt") as w:
    for line in open(input_sentences_file):
        line = line.strip()
        line_words = line.split()
        unknown_words = [w for w in line_words if w not in terminals]
        if len(unknown_words) == 0:
            filtered_sentences.append(line_words)
            w.write(line)
            w.write("\n")
        else:
            print(f"WARNING {unknown_words}")


S2_file = sys.argv[3]
with open(S2_file, "wt") as g:
    g.write("50  TOP  S1\n")
    g.write("50   TOP  S2\n")
    for i, sentence_words in enumerate(filtered_sentences):
        g.write(f"1   S1    EXAMPLE_SENTENCE_{i}_0\n")
        for j, w in enumerate(sentence_words):
            if j + 1 < len(sentence_words):
                g.write(f"1     EXAMPLE_SENTENCE_{i}_{j}    {w} EXAMPLE_SENTENCE_{i}_{j+1}\n")
            else:
                g.write(f"1     EXAMPLE_SENTENCE_{i}_{j}    {w}\n")




