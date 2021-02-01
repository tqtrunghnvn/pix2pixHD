NAME=$1
DATASET=$2
EPOCH=$3
NUMBER=$4

python generate_video.py --name ${NAME} --dataroot ${DATASET} --fps 24 --ngf 32 --which_epoch ${EPOCH} --how_many ${NUMBER}
