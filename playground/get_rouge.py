import datasets


source_file = 'test.source'
hypo_file = 'outdir/formatted-test.txt'
label_file = 'test.target'

# hypo_file = 'outdir/giga4/formatted-test.txt'
# label_file = '/scratch/tw2112/codes/ablation/giga/giga_raw/test.target'

rouge = datasets.load_metric('rouge')
with open(label_file,'r') as reffile:
    refs = []
    for i in reffile:
        refs.append(i.strip())


with open(hypo_file,'r') as outputfile:
    preds = []
    for i in outputfile:
        preds.append(i.strip())

r = datasets.load_metric('rouge')
rouge_res = r.compute(predictions=preds,references=refs,use_stemmer=True)
print(rouge_res['rouge1'])
print(rouge_res['rouge1'].mid.fmeasure*100)
print(rouge_res['rouge2'].mid.fmeasure*100)
print(rouge_res['rougeL'].mid.fmeasure*100)