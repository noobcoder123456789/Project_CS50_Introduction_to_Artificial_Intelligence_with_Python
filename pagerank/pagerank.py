import os
import random
import re
import sys
import copy
import numpy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    res = dict()

    if len(corpus[page]) == 0:
        for page in corpus.keys():
            res[page] = 1 / len(corpus)
        
        return res

    for i in corpus.keys():
        res[i] = (1 - damping_factor) / len(corpus)

    for i in corpus[page]:
        res[i] += damping_factor / len(corpus[page])

    return res
    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    res = {page: 0 for page in corpus.keys()}
    page = random.choice(list(corpus.keys()))
    
    for i in range(1, n):
        res[page] += 1
        transModel = transition_model(corpus, page, damping_factor)        
        page = (numpy.random.choice(list(transModel.keys()), 1, p=list(transModel.values())))[0]
    
    return {page: (visit / n) for page, visit in res.items()}
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    oldPR = dict()
    newPR = dict()
    for page in corpus.keys():
        newPR[page] = oldPR[page] = 1 / len(corpus)
    
    while True:                
        for p in corpus:
            temp = 0
            newPR[p] = (1 - damping_factor) / len(corpus)
            for i in corpus:
                if len(corpus[i]) == 0:
                    temp += oldPR[i] / len(corpus)
                elif p in corpus[i]:
                    temp += oldPR[i] / len(corpus[i])
            newPR[p] += temp * damping_factor
        
        check = True
        for page in newPR:
            check = abs(newPR[page] - oldPR[page]) <= 0.001
            if not check:
                break
        oldPR = copy.deepcopy(newPR)
        if check:
            break

    return newPR
    raise NotImplementedError


if __name__ == "__main__":
    main()
