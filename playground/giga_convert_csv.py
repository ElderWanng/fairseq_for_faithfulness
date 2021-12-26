import pandas as pd
import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--csvfile',type=str)
# args = parser.parse_args()
# train_csv = args.csvfile
df = pd.read_csv('/home/tw2112/codes/s2s/aux_with_neg_giga/data/giga_train_with_neg.csv')
source = df.source.tolist()
target = df.target.tolist()
source = [str(i) for i in source]
target = [str(i) for i in target]
with open('giga/train.source','w') as outfile:
    for i in source:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('giga/train.target','w') as outfile:
    for i in target:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df.columns)
print(len(source))

validation_csv = '/home/tw2112/codes/s2s/aux_with_neg_giga/data/giga_val_ent.csv'
df = pd.read_csv(validation_csv)
source = df.source.tolist()
target = df.target.tolist()
source = [str(i) for i in source]
target = [str(i) for i in target]
with open('giga/valid.source', 'w') as outfile:
    for i in source:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('giga/valid.target', 'w') as outfile:
    for i in target:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df.columns)
print(len(source))


test_csv = '/home/tw2112/codes/s2s/aux_with_neg_giga/data/giga_test_ent.csv'
df = pd.read_csv(test_csv)
source = df.source.tolist()
target = df.target.tolist()
source = [str(i) for i in source]
target = [str(i) for i in target]
with open('giga/test.source', 'w') as outfile:
    for i in source:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

with open('giga/test.target', 'w') as outfile:
    for i in target:
        sent = i.replace('\n',' ')
        outfile.write(sent+'\n')

print(df.columns)
print(len(source))



