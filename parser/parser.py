import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> SS

SS -> NP VP | NP VP CV
CV -> Conj NP VP | Conj VP
AP -> Adj | AP Adj
NP -> N | DN | PP
DN -> Det N | Det AP N
PP -> P NP | NP P NP
VP -> V | VP NP | V NP Adv | V Adv | Adv VP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    s = ""
    for x in sentence:
        if x != '.':
            s += x
    return nltk.tokenize.word_tokenize(s.lower())
    raise NotImplementedError


def check(tree):
    i = tree.height() - 1
    while i > 1:
        for subtree in tree.subtrees(lambda t: t.height() == i):
            i = subtree.height()
            if subtree.label() == 'NP':
                return False
        
        i -= 1
        if i <= 1:
            break        
    
    return True


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunk_list = list()
    for subtree in tree.subtrees():
        if subtree.label() == 'NP' and check(subtree):
            np_chunk_list.append(subtree)
    return np_chunk_list
    raise NotImplementedError


if __name__ == "__main__":
    main()
