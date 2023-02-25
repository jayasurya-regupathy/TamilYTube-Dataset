import copy
from typing import List
import random
import os

class DataSplitter:

    def splitter(self, path: str = '', lang:str = 'en', corpus_list: List[str] = None, corpus_name:str = 'combined'):
        for corpus in corpus_list:
                with open(path+'{c}'.format(c=corpus), 'r', encoding='utf-8') as rf:
                    lines = rf.readlines()
                    print(len(lines))
                    with open('combined-corpus/{co}.{l}'.format(l=lang, co=corpus_name), 'a', encoding='utf-8') as wf:
                        for line in lines:
                            if line != lines[-1]:
                                wf.write(line)
                            else:
                                wf.write(line.strip())

    def shuffle_lines(self, corpus_name: str):
        with open('combined-corpus/{co}.en'.format(co=corpus_name), 'r', encoding='utf-8') as rf:
            mlines = rf.readlines()
        with open('combined-corpus/{co}.ta'.format(co=corpus_name), 'r', encoding='utf-8') as rf:
            tlines = rf.readlines()
        temp = list(zip(mlines, tlines))
        random.shuffle(temp)
        mlines, tlines = zip(*temp)
        mlines, tlines = list(mlines), list(tlines)
        with open('combined-corpus/{co}.en'.format(co=corpus_name), 'w', encoding='utf-8') as wf:
            for line in mlines:
                wf.write(line)
        with open('combined-corpus/{co}.ta'.format(co=corpus_name), 'w', encoding='utf-8') as wf1:
            for line in tlines:
                wf1.write(line)

    def train_test_split(self, lang:str = 'en', filename:str=None, corpus:str=None, test:bool = True, val:bool = True):
        if not os.path.exists('data/{corpus_name}'.format(corpus_name=corpus)):
            os.makedirs('data/{corpus_name}'.format(corpus_name=corpus))
        with open(filename, 'r', encoding='utf-8') as rf:
            lines = rf.readlines()
        random.seed(3)
        split_indices = random.sample(range(len(lines)-1), 2000)
        test_lines=[]
        val_lines = []
        for index in split_indices:
            test_lines.append(lines[index])
        for index in sorted(split_indices, reverse=True):
            del lines[index]
        val_indices = random.sample(range(len(lines)-1), 1000)
        for index in val_indices:
            val_lines.append(lines[index])
        for index in sorted(val_indices, reverse=True):
            del lines[index]
        print(len(lines), len(val_lines), len(test_lines))
        with open('data/{corpus_name}/train.{lang}'.format(corpus_name=corpus, lang=lang), 'w', encoding='utf-8') as trf:
            for line in lines:
                if line!=lines[-1]:
                    trf.write(line)
                else:
                    trf.write(line.strip())
        with open('data/{corpus_name}/val.{lang}'.format(corpus_name=corpus, lang=lang), 'w', encoding='utf-8') as vf:
            for line in val_lines:
                if line!=val_lines[-1]:
                    vf.write(line)
                else:
                    vf.write(line.strip())
        with open('data/{corpus_name}/test.{lang}'.format(corpus_name=corpus, lang=lang), 'w', encoding='utf-8') as tef:
            for line in test_lines:
                if line!=test_lines[-1]:
                    tef.write(line)
                else:
                    tef.write(line.strip())

if __name__ == '__main__':
    corpus_list_en = ['asr-yt-cook.en']
    corpus_list_ta = ['asr-yt-cook.ta']
    # corpus_list_en = ['corpus.bcn.dev.en', 'corpus.bcn.test.en', 'corpus.bcn.train.en']
    # corpus_list_ta = ['corpus.bcn.dev.ta', 'corpus.bcn.test.ta', 'corpus.bcn.train.ta']
    ds = DataSplitter()
    ds.splitter(path='combined-corpus/', lang='en', corpus_list=corpus_list_en, corpus_name='asr-yt-only')
    ds.splitter(path='combined-corpus/', lang='ta', corpus_list=corpus_list_ta, corpus_name='asr-yt-only')
    ds.shuffle_lines(corpus_name='asr-yt-only')
    # # with open('D:/Projects/TamilYTube-Dataset/combined-corpus/en-ta-v2-parallel.en', 'r' , encoding='utf-8') as f:
    # #     print(len(f.readlines()))
    ds.train_test_split(filename='combined-corpus/asr-yt-only.en', corpus ='asr-yt-only')
    ds.train_test_split(filename='combined-corpus/asr-yt-only.ta', lang='ta', corpus='asr-yt-only')