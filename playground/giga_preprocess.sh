DATA=/scratch/tw2112/codes/ablation/giga
for SPLIT in train valid test
do
  for LANG in source target
  do
    python  -m examples.roberta.multiprocessing_bpe_encoder \
            --encoder-json encoder.json  \
            --vocab-bpe vocab.bpe \
            --inputs "$DATA/giga_raw/$SPLIT.$LANG" \
            --outputs "$DATA/giga_raw/$SPLIT.bpe.$LANG" \
            --workers 60 \
            --keep-empty;
  done
done

fairseq-preprocess --source-lang source --target-lang target \
 --trainpref $DATA/giga_raw/train.bpe \
 --validpref $DATA/giga_raw/valid.bpe \
 --testpref $DATA/giga_raw/test.bpe \
 --destdir $DATA/giga_binarized \
 --workers 60 \
 --srcdict dict.txt \
 --tgtdict dict.txt

