#!/bin/bash

NAMES=(DRDG-XS-3-7/INCOMPLETE1 DRDG-XS-3-0/INCOMPLETE1 DRDG-XS-3-9/INCOMPLETE1 RDG-S-3-6/INCOMPLETE1 RDG-XS-3-1/INCOMPLETE1 DRDG-S-2-3/INCOMPLETE1 RDG-S-3-1/INCOMPLETE1 DRDG-S-2-4/INCOMPLETE1 RDG-XS-3-6/INCOMPLETE1 RDG-S-3-8/INCOMPLETE1 RDG-XS-3-8/INCOMPLETE1 DRDG-XS-3-8/INCOMPLETE1 DRDG-XS-3-1/INCOMPLETE1 DRDG-XS-3-6/INCOMPLETE1 RDG-XS-3-9/INCOMPLETE1 RDG-S-3-9/INCOMPLETE1 RDG-S-3-0/INCOMPLETE1 RDG-XS-3-7/INCOMPLETE1 DRDG-S-2-5/INCOMPLETE1 DRDG-XS-3-10/INCOMPLETE1 RDG-S-3-7/INCOMPLETE1 DRDG-S-2-2/INCOMPLETE1 RDG-XS-3-0/INCOMPLETE1 DRDG-XS-2-10/INCOMPLETE1 DRDG-S-3-9/INCOMPLETE1 DRDG-S-3-0/INCOMPLETE1 RDG-XS-2-2/INCOMPLETE1 RDG-XS-3-10/INCOMPLETE1 RDG-S-2-5/INCOMPLETE1 RDG-XS-2-5/INCOMPLETE1 DRDG-S-3-7/INCOMPLETE1 RDG-S-2-2/INCOMPLETE1 DRDG-XS-2-4/INCOMPLETE1 DRDG-XS-2-3/INCOMPLETE1 DRDG-S-3-6/INCOMPLETE1 RDG-XS-2-4/INCOMPLETE1 RDG-S-2-3/INCOMPLETE1 RDG-XS-2-3/INCOMPLETE1 DRDG-S-3-1/INCOMPLETE1 RDG-S-2-4/INCOMPLETE1 DRDG-S-3-8/INCOMPLETE1 DRDG-XS-2-2/INCOMPLETE1 DRDG-XS-2-5/INCOMPLETE1 RDG-XS-2-10/INCOMPLETE1 RDG-S-3-2/INCOMPLETE1 DRDG-S-3-10/INCOMPLETE1 RDG-XS-3-5/INCOMPLETE1 DRDG-S-2-7/INCOMPLETE1 RDG-S-3-5/INCOMPLETE1 DRDG-S-2-0/INCOMPLETE1 RDG-XS-3-2/INCOMPLETE1 DRDG-S-2-9/INCOMPLETE1 DRDG-XS-3-3/INCOMPLETE1 DRDG-XS-3-4/INCOMPLETE1 DRDG-S-2-8/INCOMPLETE1 RDG-S-3-4/INCOMPLETE1 RDG-XS-3-3/INCOMPLETE1 DRDG-S-2-1/INCOMPLETE1 RDG-S-3-3/INCOMPLETE1 DRDG-S-2-6/INCOMPLETE1 RDG-XS-3-4/INCOMPLETE1 DRDG-XS-3-5/INCOMPLETE1 RDG-S-3-10/INCOMPLETE1 DRDG-XS-3-2/INCOMPLETE1 RDG-XS-2/INCOMPLETE1 DRDG-XS-3/INCOMPLETE1 RDG-S-2-10/INCOMPLETE1 DRDG-S-2-10/INCOMPLETE1 RDG-XS-3/INCOMPLETE1 DRDG-XS-2/INCOMPLETE1 DRDG-XS-2-9/INCOMPLETE1 DRDG-S-2/INCOMPLETE1 DRDG-XS-2-0/INCOMPLETE1 DRDG-XS-2-7/INCOMPLETE1 RDG-XS-2-8/INCOMPLETE1 RDG-S-2-8/INCOMPLETE1 DRDG-S-3-4/INCOMPLETE1 RDG-XS-2-6/INCOMPLETE1 RDG-S-2-1/INCOMPLETE1 RDG-XS-2-1/INCOMPLETE1 DRDG-S-3-3/INCOMPLETE1 RDG-S-2-6/INCOMPLETE1 DRDG-XS-2-6/INCOMPLETE1 DRDG-XS-2-1/INCOMPLETE1 DRDG-XS-2-8/INCOMPLETE1 DRDG-S-3/INCOMPLETE1 DRDG-S-3-2/INCOMPLETE1 RDG-XS-2-0/INCOMPLETE1 RDG-S-2-7/INCOMPLETE1 RDG-XS-2-7/INCOMPLETE1 DRDG-S-3-5/INCOMPLETE1 RDG-S-2-0/INCOMPLETE1 RDG-S-2-9/INCOMPLETE1 RDG-XS-2-9/INCOMPLETE1 RDG-S-3/INCOMPLETE1 RDG-S-2/INCOMPLETE1 )
TESTS=exp1

DIR=`dirname $0`
SYSDIR=$DIR/../systems
DATA=$DIR/../data/$TESTS/

for NAME in ${NAMES[@]}
do

SYSTEM=Neural-LP
echo "Running Neural-LP..."
source activate $SYSTEM
python $SYSDIR/$SYSTEM/src/main.py --datadir=$DATA/$SYSTEM/$NAME --exps_dir=$DIR/../output/$TESTS/$SYSTEM --exp_name=$NAME > $DIR/../output/$TESTS/$SYSTEM/$NAME/log.txt 2> $DIR/../output/$TESTS/$SYSTEM/$NAME/err.txt
echo "done."

SYSTEM=ntp
echo "Running ntp..."
source activate $SYSTEM
export PYTHONPATH=$PYTHONPATH:$SYSDIR/$SYSTEM
python $SYSDIR/$SYSTEM/ntp/experiments/learn.py $DATA/$SYSTEM/$NAME/run.conf > $DIR/../output/$TESTS/$SYSTEM/$NAME/log.txt 2> $DIR/../output/$TESTS/$SYSTEM/$NAME/err.txt
mv out/$NAME/* $DIR/../output/$TESTS/$SYSTEM/$NAME/
rm -r out/$NAME
echo "done."

SYSTEM=amiep
echo "Running amiep..."
java -jar $SYSDIR/$SYSTEM/amie_plus.jar -mins 3 -minis 3 -minpca 0.25 -oute  $DATA/$SYSTEM/$NAME/train.txt > $DIR/../output/$TESTS/$SYSTEM/$NAME/results.txt 2> $DIR/../output/$TESTS/$SYSTEM/$NAME/err.txt
echo "done."

SYSTEM=FOIL
echo "Running FOIL..."
# ADD "-m 200000" if the max tuples are exceeded
../systems/FOIL/./foil6 -v0 -n <$DATA/$SYSTEM/$NAME/train_FOIL.d >$DIR/../output/$TESTS/$SYSTEM/$NAME/FOIL_out.txt 2> $DIR/../output/$TESTS/$SYSTEM/$NAME/err.txt
echo "done."

done
exit 0

