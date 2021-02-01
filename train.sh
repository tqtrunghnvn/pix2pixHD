NAME=$1
DATASET=$2

python -u train_video.py --name ${NAME} --dataroot ${DATASET} --save_epoch_freq 1 --ngf 32
