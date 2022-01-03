from newsroom.analyze import Fragments
from questeval.questeval_metric import QuestEval
from datasets import load_metric
questeval = QuestEval(no_cuda=False,use_cache=True,task='summarization', do_weighter=True)
# questeval = QuestEval(no_cuda=False)
# #xsum
# source_file = 'test.source'
# hypo_file = 'outdir/formatted-test.txt'
# label_file = 'test.target'


# giga
source_file = '/scratch/tw2112/codes/ablation/giga/giga_raw/test.source'
hypo_file = 'outdir/giga4/formatted-test.txt'
label_file = '/scratch/tw2112/codes/ablation/giga/giga_raw/test.target'




keep = 2000
with open(label_file,'r') as reffile:
    refs = []
    for i in reffile:
        # i = i.replace("[ent] ", "")
        refs.append(i.strip())


with open(hypo_file,'r') as outputfile:
    preds = []
    for i in outputfile:
        # i = i.replace("[ent] ", "")
        preds.append(i.strip())

with open(source_file,'r') as outputfile:
    srcs = []
    for i in outputfile:
        i = i.replace("[ent] ", "")
        srcs.append(i.strip())


rouge_metric = load_metric("rouge")
result = rouge_metric.compute(predictions=preds, references=refs, use_stemmer=True)
result = {key: value.mid.fmeasure * 100 for key, value in result.items()}
result = {k: round(v, 2) for k, v in result.items()}
result = [score for name, score in result.items()]
print(result)

coverage = []
den = []
for i in range(len(srcs)):
    fragments = Fragments(preds[i], srcs[i])
    coverage.append(fragments.coverage())
    den.append(fragments.density())
print(sum(coverage)/len(coverage))
print(sum(den)/len(den))

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
hypo_file = 'outdir/formatted-test.txt'
label_file = 'test.target'



with open(label_file,'r') as reffile:
    refs = []
    for i in reffile:
        # i = i.replace("[ent] ", "")
        refs.append(i.strip())


with open(hypo_file,'r') as outputfile:
    preds = []
    for i in outputfile:
        # i = i.replace("[ent] ", "")
        preds.append(i.strip())

with open(source_file,'r') as outputfile:
    srcs = []
    for i in outputfile:
        # i = i.replace("[ent] ", "")
        srcs.append(i.strip())
rouge_metric = load_metric("rouge")
result = rouge_metric.compute(predictions=preds, references=refs, use_stemmer=True)
result = {key: value.mid.fmeasure * 100 for key, value in result.items()}
result = {k: round(v, 2) for k, v in result.items()}
result = [score for name, score in result.items()]
print(result)


# coverage = []
# den = []
# for i in range(len(srcs)):
#     fragments = Fragments(preds[i], srcs[i])
#     coverage.append(fragments.coverage())
#     den.append(fragments.density())
# print(sum(coverage)/len(coverage))
# print(sum(den)/len(den))


preds = preds[:keep]
srcs = srcs[:keep]
refs = refs[:keep]

score = questeval.corpus_questeval(
    hypothesis=preds,
    sources=srcs,
    list_references=refs
)

print(score['corpus_score'])

# score = questeval.corpus_questeval(
#     hypothesis=refs,
#     sources=srcs,
#     list_references=refs
# )
#
# print(score['corpus_score'])