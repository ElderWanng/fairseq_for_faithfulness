DATA=/home/tw2112/codes/fairseq/playground/data/xsum
for SPLIT in train valid test
do
  for LANG in source target
  do
    python  -m examples.roberta.multiprocessing_bpe_encoder \
            --encoder-json encoder.json  \
            --vocab-bpe vocab.bpe \
            --inputs "$DATA/raw/$SPLIT.$LANG" \
            --outputs "$DATA/raw/$SPLIT.bpe.$LANG" \
            --workers 60 \
            --keep-empty;
  done
done

fairseq-preprocess --source-lang source --target-lang target \
 --trainpref $DATA/raw/train.bpe \
 --validpref $DATA/raw/valid.bpe \
 --testpref $DATA/raw/test.bpe \
 --destdir $DATA/binarized \
 --workers 60 \
 --srcdict dict.txt \
 --tgtdict dict.txt

