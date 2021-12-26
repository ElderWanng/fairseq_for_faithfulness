import pandas as pd
import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--csvfile',type=str)
# args = parser.parse_args()
# train_csv = args.csvfile
df = pd.read_csv('/scratch/tw2112/TEMPCACHE/xsum_with_aux_and_negative_ablation/xsum_train_with_neg.csv')
source = df.source.tolist()
target = df.target.tolist()
with open('train.source','w') as outfile:
    for i in source:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('train.target','w') as outfile:
    for i in target:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df.columns)
print(len(source))

validation_csv = '/scratch/tw2112/TEMPCACHE/xsum_with_aux_and_negative_ablation/xsum_val_ent.csv'
df = pd.read_csv(validation_csv)
source = df.source.tolist()
target = df.target.tolist()
with open('valid.source', 'w') as outfile:
    for i in source:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('valid.target', 'w') as outfile:
    for i in target:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df.columns)
print(len(source))


test_csv = '/scratch/tw2112/TEMPCACHE/xsum_with_aux_and_negative_ablation/xsum_test_ent.csv'
df = pd.read_csv(test_csv)
source = df.source.tolist()
target = df.target.tolist()
with open('test.source', 'w') as outfile:
    for i in source:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('test.target', 'w') as outfile:
    for i in target:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df.columns)
print(len(source))



