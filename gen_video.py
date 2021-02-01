import os
import video_utils
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--frame_dir', default='', type=str, help='frame directory')
parser.add_argument('--video_path', default='', type=str, help='path for saving video')
parser.add_argument('--fps', default=24, type=str, help='frame per second')

opts = parser.parse_args()

#if os.path.isdir(opts.frame_dir):
#    shutil.rmtree(opts.frame_dir)
#os.mkdir(opts.frame_dir)

video_utils.video_from_frame_directory(
    opts.frame_dir,
    opts.video_path,
    frame_file_glob=r"frame-%06d.jpg",
    framerate=opts.fps,
    crop_to_720p=True,
    reverse=False
)

print("video ready:\n%s" % opts.video_path)
