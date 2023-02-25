from typing import Dict, Any, List
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from indicnlp.tokenize import indic_tokenize
from nltk.tokenize import word_tokenize
load_dotenv()


class TranscriptExtraction:
    video_ids: List[str]
    video_dict: Dict[str, str]

    def __init__(self, filename):
        with open(filename, 'r') as inputfile:
            self.video_ids = inputfile.readlines()
            self.youtube = build('youtube', 'v3', developerKey=os.getenv("API_KEY"))

    def extract(self):
        video_id: str
        for video_id in self.video_ids:
            video_id = video_id.rstrip()
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_manually_created_transcript(['en-IN', 'en', 'en-US', 'en-GB'])
            translated_transcript = transcript.translate('ta')
            transcript = transcript.fetch()
            for t in transcript:
                t['text'] = t['text'].replace('\n', ' ')
                words = word_tokenize(t['text'])
                t['text'] = " ".join(words)
                with open('D:/Projects/TamilYTube-Dataset/data/transcript/manual/{id}.txt'.format(id=video_id), 'a', encoding='utf-8') as text_file:
                    text_file.write(t['text'])
                    if t != transcript[-1]:
                        text_file.write("\n")
            translated_transcript = translated_transcript.fetch()
            if len(transcript) == len(translated_transcript):
                print(video_id)
            for t in translated_transcript:
                t['text'] = t['text'].replace('\n', ' ')
                tamil_words = indic_tokenize.trivial_tokenize_indic(t['text'])
                t['text'] = " ".join(tamil_words)
                with open('D:/Projects/TamilYTube-Dataset/data/transcript/translated/{id}.txt'.format(id=video_id), 'a', encoding='utf-8') as text_file:
                    text_file.write(t['text'])
                    if t != translated_transcript[-1]:
                        text_file.write("\n")

    def combine(self):
        for video_id in self.video_ids:
            video_id = video_id.rstrip()
            print(video_id)
            with open('D:/Projects/TamilYTube-Dataset/data/combined_transcripts/translated_combined/trans-yt-cook.en', 'a', encoding='utf-8') as outfile:
                with open('D:/Projects/TamilYTube-Dataset/data/transcript/manual/{id}.txt'.format(id=video_id), encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    if not video_id == self.video_ids[-1]:
                        outfile.write("\n")
            with open('D:/Projects/TamilYTube-Dataset/data/combined_transcripts/translated_combined/trans-yt-cook.ta', 'a', encoding='utf-8') as outfile:
                with open('D:/Projects/TamilYTube-Dataset/data/transcript/translated/{id}.txt'.format(id=video_id), encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    if not video_id == self.video_ids[-1]:
                        outfile.write("\n")


if __name__ == '__main__':
    trans_extract = TranscriptExtraction('D:/Projects/TamilYTube-Dataset/translate-video-ids.txt')
    #trans_extract.extract()
    trans_extract.combine()

