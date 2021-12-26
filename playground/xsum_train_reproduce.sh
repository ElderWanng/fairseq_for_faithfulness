set -e

DATA=/scratch/tw2112/codes/ablation/xsum

export BART_PATH=/scratch/tw2112/codes/models/bart.large/model.pt
TOTAL_NUM_UPDATES=22000
WARMUP_UPDATES=500
LR=3e-05
MAX_TOKENS=2048
UPDATE_FREQ=4
SAVE_PATH1=DATA/ckpt1

DATA_DIR=$DATA/binarized
LOGFILE=log/log5.txt

#fairseq-train $DATA_DIR \
#    --restore-file $BART_PATH \
#    --save-dir $SAVE_PATH1 \
#    --max-tokens $MAX_TOKENS \
#    --task translation \
#    --source-lang source --target-lang target \
#    --truncate-source \
#    --layernorm-embedding \
#    --share-all-embeddings \
#    --share-decoder-input-output-embed \
#    --reset-optimizer --reset-dataloader --reset-meters \
#    --required-batch-size-multiple 1 \
#    --arch bart_large \
#    --criterion label_smoothed_cross_entropy \
#    --label-smoothing 0.1 \
#    --dropout 0.1 --attention-dropout 0.1 \
#    --weight-decay 0.01 --optimizer adam --adam-betas "(0.9, 0.999)" --adam-eps 1e-08 \
#    --clip-norm 0.1 \
#    --lr-scheduler polynomial_decay --lr $LR --total-num-update $TOTAL_NUM_UPDATES --warmup-updates $WARMUP_UPDATES \
#    --fp16 --update-freq $UPDATE_FREQ \
#    --skip-invalid-size-inputs-valid-test \
#    --find-unused-parameters \
#    --log-file $LOGFILE \
#    --max-epoch 1;



export BART_PATH=/scratch/tw2112/codes/ablation/xsum/ckpt1/checkpoint1.pt
TOTAL_NUM_UPDATES=44000
WARMUP_UPDATES=500
LR=3e-05
MAX_TOKENS=2048
UPDATE_FREQ=4
SAVE_PATH=$DATA/ckpt2

DATA_DIR=$DATA/binarized
LOGFILE=log/log6.txt

fairseq-train $DATA_DIR \
    --restore-file $BART_PATH \
    --save-dir $SAVE_PATH \
    --max-tokens $MAX_TOKENS \
    --task translation \
    --source-lang source --target-lang target \
    --truncate-source \
    --layernorm-embedding \
    --share-all-embeddings \
    --share-decoder-input-output-embed \
    --reset-optimizer --reset-dataloader --reset-meters \
    --required-batch-size-multiple 1 \
    --arch bart_large \
    --criterion label_smoothed_cross_entropy \
    --label-smoothing 0.1 \
    --dropout 0.1 --attention-dropout 0.1 \
    --weight-decay 0.01 --optimizer adam --adam-betas "(0.9, 0.999)" --adam-eps 1e-08 \
    --clip-norm 0.1 \
    --lr-scheduler polynomial_decay --lr $LR --total-num-update $TOTAL_NUM_UPDATES --warmup-updates $WARMUP_UPDATES \
    --fp16 --update-freq $UPDATE_FREQ \
    --skip-invalid-size-inputs-valid-test \
    --find-unused-parameters \
    --log-file $LOGFILE \
    --max-epoch 1;