from __future__ import unicode_literals
from typing import Dict, Any, List
import youtube_dl
import os
from pydub import AudioSegment
from youtube_transcript_api import YouTubeTranscriptApi

class AudioExtraction:
    video_ids: List[str]

    def __init__(self, filename):
        with open(filename, 'r') as inputfile:
            self.video_ids = inputfile.readlines()

    def extract_transcript(self, video_id):
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_manually_created_transcript(['en-IN', 'en', 'en-GB', 'en-US'])
        transcript = transcript.fetch()
        return transcript

    def extract_full_audio(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'd:/Projects/TamilYTube-Dataset/data/full_audios/%(id)s.%(ext)s',
            'cookiefile': 'D:/Projects/TamilYTube-Dataset/youtube.com_cookies.txt',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        }
        undownloaded=[]
        for video in self.video_ids:
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.cache.remove()
                    ydl.download(['http://www.youtube.com/watch?v='+video])
            except Exception:
                print(video+'added to unloaded list')
                undownloaded.append(video)

    def extract_audio_segments(self):
        for video in self.video_ids:
            video = video.rstrip()
            count = 0
            filename = 'd:/Projects/TamilYTube-Dataset/data/full_audios/{video_id}.wav'.format(video_id=video)
            if not os.path.exists('d:/Projects/TamilYTube-Dataset/data/audio_segments/{video_id}'.format(video_id=video)):
                    os.makedirs('d:/Projects/TamilYTube-Dataset/data/audio_segments/{video_id}'.format(video_id=video))
            transcript = self.extract_transcript(video)
            for t in transcript:
                new_audio = AudioSegment.from_wav(filename)
                start = t['start'] * 1000
                end = ((t['start']+t['duration']) * 1000) + 100
                new_audio = new_audio[start:end]
                count += 1
                new_audio.export('d:/Projects/TamilYTube-Dataset/data/audio_segments/{video_id}/{video_id}_{num}.wav'.format(video_id=video, num=count), format="wav")


if __name__ == '__main__':
    audio_extract = AudioExtraction('D:/Projects/TamilYTube-Dataset/asr-video-ids.txt')
    #audio_extract.extract_full_audio()
    audio_extract.extract_audio_segments()