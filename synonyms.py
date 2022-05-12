import re
from nltk.corpus import wordnet


def replaceWord(w):
    return re.sub("[_-]", " ", w)


# for ss in wordnet.synsets('Smoke'):
#     # x = re.sub("[_-]", " ", txt)
#     for x in ss.lemma_names():
#         print(replaceWord(x))


def find_synonyms(arr):
    tag0 = []
    tag1 = []
    for ss in wordnet.synsets(arr[0]):
        for x in ss.lemma_names():
            w = replaceWord(x)
            if w.upper().strip() not in tag0:
                tag0.append(w.upper().strip())

    for ss in wordnet.synsets(arr[1]):
        for x in ss.lemma_names():
            w = replaceWord(x)
            if w.upper().strip() not in tag1:
                tag1.append(w.upper().strip())
    combine = tag0 + tag1
    results = [x.upper() for x in arr if x.upper() not in combine] + combine
    return results


# print(find_synonyms(['Smoke', 'Ideas']))
# dataArr = ['ANH YEU', 'em nhieu']
# print([x.title() for x in dataArr])
