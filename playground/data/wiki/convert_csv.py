import pandas as pd
import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--csvfile',type=str)
# args = parser.parse_args()
# train_csv = args.csvfile
df_main = pd.read_csv('/scratch/tw2112/TEMPCACHE/wikihow_with_aux_and_negative/wiki_train_with_neg.csv')


df_nli = pd.read_csv('/scratch/tw2112/TEMPCACHE/wikihow_with_aux_and_negative/nli_train.csv')

df_main = df_main[["source",'target']]
df_nli = df_nli[["source",'target']]

df_train = pd.concat([df_main,df_nli])
df_train = df_train.sample(frac=1)
source = df_train.source.tolist()
target = df_train.target.tolist()
with open('train.source','w') as outfile:
    for i in source:
        i = str(i)
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('train.target','w') as outfile:
    for i in target:
        i = str(i)
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df_train.columns)
print(len(source))

validation_csv = '/scratch/tw2112/TEMPCACHE/wikihow_with_aux_and_negative/wiki_val_ent.csv'
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


test_csv = '/scratch/tw2112/TEMPCACHE/wikihow_with_aux_and_negative/wiki_test_ent.csv'
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



