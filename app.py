from model import LectureSummarizerGensim
from transcribe import VideoTranscriber

transcriber = VideoTranscriber(model_name="base")  # you can switch model here

video_file = "test.mp4"
output_folder = "transcripts"

transcript_path, transcript_text = transcriber.transcribe_video(video_file, output_folder)

print(f"Transcript saved at: {transcript_path}")
print("Transcript preview:")

# Load transcript
with open(transcript_path, "r", encoding="utf-8") as f:
    transcript = f.read()

# Summarize
summarizer = LectureSummarizerGensim()
summary = summarizer.summarize(transcript)

# Output
print("\n📚 Summary:\n")
print(summary)
