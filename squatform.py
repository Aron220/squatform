# Project: Squat form analysis with Open CV

# what to evaluate:
# depth, back angle (rounding, arching), foot placement, neck position, knee position, hip rotation, inward/outward knees

import cv2
import imageio

def play_local_video(video_path):
    video = imageio.get_reader(video_path)
    for frame in video:
        cv2.imshow('Local Video', frame[:, :, ::-1])  # Convert from RGB to BGR
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Example usage
video_path = 'squat_videos/good/squat_1_good.mp4'
play_local_video(video_path)


#Defining path to data

data = ('squat_videos/bad', 'squat_videos/good')
bad_squat_videos_path = data[0]
good_squat_videos_path = data[1]