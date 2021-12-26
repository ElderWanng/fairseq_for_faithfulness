import datasets
x = datasets.load_dataset('xsum')
with open('train.source','w') as inputfile1:
    with open('train.target','w') as inputfile2:
        for e in x["train"]:
            source = e['document']
            source = source.replace('\n',' ')
            target = e['summary']
            target = target.replace('\n',' ')

            source = '[ent] '+ source
            inputfile1.write(source+"\n")
            inputfile2.write(target+"\n")

with open('val.source', 'w') as inputfile1:
    with open('val.target', 'w') as inputfile2:
        for e in x["validation"]:
            source = e['document']
            source = source.replace('\n',' ')
            target = e['summary']
            target = target.replace('\n',' ')

            source = '[ent] ' + source
            inputfile1.write(source + "\n")
            inputfile2.write(target + "\n")

with open('test.source', 'w') as inputfile1:
    with open('test.target', 'w') as inputfile2:
        for e in x["test"]:
            source = e['document']
            source = source.replace('\n',' ')
            target = e['summary']
            target = target.replace('\n',' ')

            source = '[ent] ' + source
            inputfile1.write(source + "\n")
            inputfile2.write(target + "\n")
