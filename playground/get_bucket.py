import tqdm
from newsroom.analyze import Fragments


source_file = 'test.source'
hypo_file = 'outdir/formatted-test.txt'
label_file = 'test.target'

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


temp1 = []
temp2 = []
for i in tqdm.tqdm(range(len(srcs))):
    src = srcs[i]
    ref = refs[i]
    hypo = preds[i]


    fragments1 = Fragments(src, hypo)


    temp1.append(fragments1.coverage())
    temp2.append(fragments1.density())



print(sum(temp1)/len(temp1))
print(sum(temp2)/len(temp2))

