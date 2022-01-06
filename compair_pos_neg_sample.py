from questeval.questeval_metric import QuestEval
from datasets import load_metric
import pandas as pd
questeval = QuestEval(no_cuda=False,use_cache=True,task='summarization', do_weighter=True)

neg_csv_path = "/home/tw2112/codes/s2s/src/xsum_data/xsum_negative.csv"
doc_col = "document"
pos_col = "true_summary"
neg_col = "summary"
keep = 1000
df = pd.read_csv(neg_csv_path)
df = df.head(keep)
score = questeval.corpus_questeval(
    hypothesis=df[pos_col].to_list(),
    sources=df[doc_col].to_list(),
    # list_references=refs
)

print(score['corpus_score'])


score = questeval.corpus_questeval(
    hypothesis=df[neg_col].to_list(),
    sources=df[doc_col].to_list(),
    # list_references=refs
)

print(score['corpus_score'])