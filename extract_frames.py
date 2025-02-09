import os
import cv2


def extract_frames(video_path, output_folder, frame_rate=1):
    """Extracts frames from a video file and saves them in the specified output folder."""
   
    if not os.path.exists(video_path):
        print(f"Error: Video file not found - {video_path}")
        return


    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    cap = cv2.VideoCapture(video_path)


    if not cap.isOpened():
        print(f"Error: Unable to open video {video_path}. Skipping...")
        return


    print(f"Processing video: {video_path}")


    frame_id = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Get total frame count


    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if end of video or error


        # Save every `frame_rate` seconds
        fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get frames per second
        frame_interval = fps * frame_rate  # Extract every `frame_rate` seconds


        if frame_id % frame_interval == 0:
            frame_name = os.path.join(output_folder, f"frame_{frame_id}.jpg")
            cv2.imwrite(frame_name, frame)
            print(f"Saved: {frame_name}")


        frame_id += 1


    cap.release()
    print(f"Finished extracting frames from: {video_path}\n")


# Define dataset paths
violence_folder = "dataset/Violence"
non_violence_folder = "dataset/NonViolence"
frames_folder = "dataset/frames"


# Ensure dataset folders exist
if not os.path.exists(violence_folder) or not os.path.exists(non_violence_folder):
    print("❌ Error: Dataset folders not found. Please check your dataset structure.")
    exit()


# Extract frames from violence videos
for video_file in os.listdir(violence_folder):
    video_path = os.path.join(violence_folder, video_file)
    output_folder = os.path.join(frames_folder, "violence", os.path.splitext(video_file)[0])
    extract_frames(video_path, output_folder)


# Extract frames from non-violence videos
for video_file in os.listdir(non_violence_folder):
    video_path = os.path.join(non_violence_folder, video_file)
    output_folder = os.path.join(frames_folder, "non_violence", os.path.splitext(video_file)[0])
    extract_frames(video_path, output_folder)


print("Frame extraction process completed!")
print(f"Total frames extracted: {len(os.listdir(frames_folder))}")
