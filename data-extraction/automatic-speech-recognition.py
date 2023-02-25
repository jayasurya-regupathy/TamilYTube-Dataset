import speech_recognition as sr
import os
import re
from indicnlp.tokenize import indic_tokenize

class SpeechRecognition:

    def __init__(self, filename):
        with open(filename, 'r') as inputfile:
            self.video_ids = inputfile.readlines()

    def sorted_alphanumeric(self, data):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(data, key=alphanum_key)

    def extract_transcript(self):
        r = sr.Recognizer()
        for video in self.video_ids:
            video = video.rstrip()
            files = self.sorted_alphanumeric(os.listdir("d:/Projects/TamilYTube-Dataset/data/audio_segments/{video_id}".format(video_id=video)))
            for filename in files:
                print(filename)
                with sr.AudioFile("d:/Projects/TamilYTube-Dataset/data/audio_segments/{video_id}/{file}".format(video_id=video, file=filename)) as source:
                    audio_data = r.record(source)
                    try:
                        text = r.recognize_google(audio_data, language="ta-IN")
                        words = indic_tokenize.trivial_tokenize_indic(text)
                        text = " ".join(words)
                    except (sr.UnknownValueError, sr.RequestError) as e:
                        text= " "
                    with open('D:/Projects/TamilYTube-Dataset/data/transcript/asr_transcripts/{id}.txt'.format(id=video), 'a', encoding='utf-8') as text_file:
                        text_file.write(text)
                        if filename!=files[-1]:
                            text_file.write('\n')

    def combine(self):
        for video_id in self.video_ids:
            video_id = video_id.rstrip()
            print(video_id)
            with open('D:/Projects/TamilYTube-Dataset/data/combined_transcripts/asr_combined/asr-yt-cook.en', 'a', encoding='utf-8') as outfile:
                with open('D:/Projects/TamilYTube-Dataset/data/transcript/manual/{id}.txt'.format(id=video_id), encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    if not video_id == self.video_ids[-1]:
                        outfile.write("\n")
            with open('D:/Projects/TamilYTube-Dataset/data/combined_transcripts/asr_combined/asr-yt-cook.ta', 'a', encoding='utf-8') as outfile:
                with open('D:/Projects/TamilYTube-Dataset/data/transcript/asr_transcripts/{id}.txt'.format(id=video_id), encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    if not video_id == self.video_ids[-1]:
                        outfile.write("\n")


if __name__ == '__main__':
    speech_recog = SpeechRecognition('D:/Projects/TamilYTube-Dataset/asr-video-ids.txt')
    #video_dict = speech_recog.extract_transcript()
    speech_recog.combine()












