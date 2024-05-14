import sys
import whisper

if len(sys.argv) != 2:
    print("Usage: python AudioToText.py <audio_file>")
    sys.exit(1)

audio_file = sys.argv[1]

model = whisper.load_model("base")
result = model.transcribe(audio_file)

# Write the transcribed text to a file
output_file = "Parsing text from audio file.txt"
with open(output_file, 'w') as output:
    output.write(result["text"])

print(f"Transcribed text has been written to '{output_file}'")
