NAME=$1
DATASET=$2
PSTART=$3
PSTOP=$4

python generate_progress_video.py --name ${NAME} --dataroot ${DATASET} --fps 24 --ngf 32 --pstart ${PSTART} --pstop ${PSTOP}
