import os
from moviepy.editor import VideoFileClip
import whisper

class VideoTranscriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def extract_audio(self, video_path, audio_path="temp_audio.wav"):
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path, verbose=False, logger=None)
        return audio_path

    def transcribe_audio(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]

    def transcribe_video(self, video_path, output_folder):
        os.makedirs(output_folder, exist_ok=True)
        audio_path = self.extract_audio(video_path)

        transcript_text = self.transcribe_audio(audio_path)

        base_name = os.path.splitext(os.path.basename(video_path))[0]
        transcript_path = os.path.join(output_folder, f"{base_name}.txt")

        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript_text)

        os.remove(audio_path)
        return transcript_path, transcript_text