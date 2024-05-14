import sys
import os
import moviepy.editor as mp
import whisper

if len(sys.argv) != 2:
    print("Usage: python VideoToText.py <video_file>")
    sys.exit(1)

video_file = sys.argv[1]

# If file does not exist
if not os.path.isfile(video_file):
    print("Error: File not found!")
    sys.exit(1)

# Convert video to audio
video_clip = mp.VideoFileClip(video_file)
audio_clip = video_clip.audio

# Save audio to a temporary file
temp_audio_file = "temp_audio.wav"
audio_clip.write_audiofile(temp_audio_file)

# Transcribe the audio
model = whisper.load_model("base")
result = model.transcribe(temp_audio_file)

# Write the transcribed text to a file
output_file = "Parsing text from video file.txt"
with open(output_file, 'w') as output:
    output.write(result["text"])

print(f"Transcribed text from the video has been written to '{output_file}'")

# Remove the temporary audio file
os.remove(temp_audio_file)
