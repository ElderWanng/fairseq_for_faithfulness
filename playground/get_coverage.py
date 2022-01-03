import datasets
import pandas as pd
import tqdm
from newsroom.analyze import Fragments

# hypo_file = './outdir/xsum_nli_weight/formatted-test.txt'
# source_file = '/scratch/tw2112/codes/ablation/xsum_weight/pos_raw/test.source'
# label_file = '/scratch/tw2112/codes/ablation/xsum_weight/pos_raw/test.target'

source_file = '/scratch/tw2112/codes/ablation/giga/giga_raw/test.source'
hypo_file = 'outdir/giga4/formatted-test.txt'
label_file = '/scratch/tw2112/codes/ablation/giga/giga_raw/test.target'

source_file = 'test.source'
hypo_file = 'outdir/formatted-test.txt'
label_file = 'test.target'


with open(label_file,'r') as reffile:
    refs = []
    for i in reffile:
        i = i.replace("[ent] ", "")
        refs.append(i.strip())


with open(hypo_file,'r') as outputfile:
    preds = []
    for i in outputfile:
        i = i.replace("[ent] ", "")
        preds.append(i.strip())

with open(source_file,'r') as outputfile:
    srcs = []
    for i in outputfile:
        i = i.replace("[ent] ", "")
        srcs.append(i.strip())

coverage = []
den = []
for i in range(len(srcs)):
    fragments = Fragments(preds[i], srcs[i])
    coverage.append(fragments.coverage())
    den.append(fragments.density())
print(sum(coverage)/len(coverage))
print(sum(den)/len(den))