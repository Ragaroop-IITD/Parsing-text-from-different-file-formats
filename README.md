# Parsing-text-from-different-file-formats
Extracting text from PDF's, Audio and Video files.

# Report

## Programming Language and Libraries/Frameworks Used

### PDF to Text Conversion:
- **Programming Language:** Python
- **Libraries/Frameworks:** PyPDF2

### Audio to Text Conversion:
- **Programming Language:** Python
- **Libraries/Frameworks:** whisper (custom library for audio transcription)

### Video to Text Conversion:
- **Programming Language:** Python
- **Libraries/Frameworks:** moviepy, whisper

## Insights and Techniques Implemented

### PDF to Text Conversion:
- Utilized PyPDF2 library for parsing PDF files and extracting text.
- Implemented a loop to iterate through each page of the PDF document for extraction.
- No additional performance optimization techniques applied.

### Audio to Text Conversion:
- Employed whisper library for transcribing audio files to text.
- Loaded a pre-trained model ("base") for audio transcription.
- Wrote the transcribed text to a file.
- No additional performance optimization techniques applied.

### Video to Text Conversion:
- Utilized moviepy library to extract audio from the video file.
- Converted the video file to an audio file (temporary WAV format).
- Employed whisper library for transcribing audio to text using a pre-trained model.
- Wrote the transcribed text to a file.
- Removed the temporary audio file.

## Challenges and Difficulties Faced

### PDF to Text Conversion:
**Inability to Read Images and Tables:** One significant challenge faced during the PDF to text conversion is the inability to extract text from images and tables embedded within the PDF files. Since the implemented method relies on text extraction from PDF content directly, it does not handle non-textual elements well. Images and tables often pose difficulties in extraction due to their graphical nature, which requires optical character recognition (OCR) techniques for conversion. Integrating OCR functionality into the conversion process could address this issue, but it would require additional libraries and more complex processing.

### Audio to Text Conversion:
**Limited Language Support:** The audio to text conversion process encountered limitations in reading languages other than English. This constraint restricts the versatility of the system, especially in multilingual contexts where transcripts may contain various languages. Integrating support for multiple languages would involve either utilizing multilingual models or implementing language detection mechanisms to adapt the transcription process accordingly.

**Background Noise Interference:** Another challenge is dealing with background noise, which can interfere with accurate transcription. Background voices or ambient sounds may cause inaccuracies or errors in the transcribed text. Implementing noise reduction techniques or utilizing models trained to handle noisy environments could help mitigate this issue.

### Video to Text Conversion:
**Similar Challenges as Audio to Text:** The video to text conversion process faces similar challenges to audio to text conversion, as both processes involve transcribing audio content. Therefore, issues such as language limitations and background noise interference persist in the video transcription workflow. Additionally, the complexity of video content, including varying audio qualities and multiple speakers, can further complicate transcription accuracy.


[Link to Results](https://drive.google.com/drive/folders/1kj_fGSpgqFGM5cIK5ychur_pb8BFK7QD)
