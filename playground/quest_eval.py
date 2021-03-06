from questeval.questeval_metric import QuestEval
questeval = QuestEval(no_cuda=False)
# #xsum
# source_file = 'test.source'
# hypo_file = 'outdir/formatted-test.txt'
# label_file = 'test.target'


# giga
source_file = 'giga/test.source'
hypo_file = 'outdir/giga2/formatted-test.txt'
label_file = 'giga/test.target'

import  pandas as pd

keep = 2000
with open(label_file,'r') as reffile:
    refs = []
    for i in reffile:
        refs.append(i.strip())


with open(hypo_file,'r') as outputfile:
    preds = []
    for i in outputfile:
        preds.append(i.strip())

with open(source_file,'r') as outputfile:
    srcs = []
    for i in outputfile:
        srcs.append(i.strip())

preds = preds[:keep]
srcs = srcs[:keep]
refs = refs[:keep]

score = questeval.corpus_questeval(
    hypothesis=preds,
    sources=srcs,
    list_references=refs
)

print(score['corpus_score'])






source_file = 'test.source'
hypo_file = 'outdir/xsum_concate4/formatted-test.txt'
label_file = 'test.target'

import  pandas as pd


with open(label_file,'r') as reffile:
    refs = []
    for i in reffile:
        refs.append(i.strip())


with open(hypo_file,'r') as outputfile:
    preds = []
    for i in outputfile:
        preds.append(i.strip())

with open(source_file,'r') as outputfile:
    srcs = []
    for i in outputfile:
        srcs.append(i.strip())

preds = preds[:keep]
srcs = srcs[:keep]
refs = refs[:keep]

score = questeval.corpus_questeval(
    hypothesis=preds,
    sources=srcs,
    list_references=refs
)

print(score['corpus_score'])