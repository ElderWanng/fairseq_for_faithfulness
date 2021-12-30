from questeval.questeval_metric import QuestEval
questeval = QuestEval(no_cuda=False)
# #xsum
#
hypo_file = './outdir/xsum_ablation_weight/formatted-test.txt'
label_file = '/scratch/tw2112/codes/ablation/xsum_weight/pos_raw/test.target'

source_file = '/scratch/tw2112/codes/ablation/xsum_weight/pos_raw/test.source'



# giga
# source_file = '/scratch/tw2112/codes/ablation/giga_weight/pos_raw/test.source'
# hypo_file = './outdir/giga_weight/formatted-test.txt'
# label_file = '/scratch/tw2112/codes/ablation/giga_weight/pos_raw/test.target'

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






