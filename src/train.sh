#! /bin/bash

VEC_FILE=samples.vec
DATA_DIR=data
POS_IMAGES=2000
NEG_IMAGES=1000
STAGES=10
FEATURE_TYPE=LBP

opencv_traincascade -data $DATA_DIR \
    -vec $VEC_FILE \
    -bg bg.txt \
    -numPos $POS_IMAGES -numNeg $NEG_IMAGES -numStages $STAGES \
    -precalcValBufSize 1024 -precalcIdxBufSize 1024 \
    -featureType $FEATURE_TYPE \
    -w 50 -h 50

    # -minHitRate 0.995 -maxFalseAlarmRate 0.5 \
