from indicnlp.tokenize import indic_tokenize
from nltk.tokenize import word_tokenize
import random

class DataPreProcessing:

    def __init__(self, combinedfilename:str = 'Test'):
        self.combinedfilename=combinedfilename

    def get_lines(self):
            with open(self.combinedfilename+'.ta', 'r', encoding='utf-8') as tafile:
                    tlines = tafile.readlines()
            with open(self.combinedfilename+'.en', 'r', encoding='utf-8') as mafile:
                    mlines = mafile.readlines()
            print(len(mlines), len(tlines))
            return mlines, tlines

    def append_lines(self, tlines:list[str] = None, mlines:list[str] = None):
        with open(self.combinedfilename+'.ta', 'w', encoding='utf-8') as afile:
            for line in tlines:
                afile.write(line.strip())
                if line != tlines[-1]:
                    afile.write('\n')
        with open(self.combinedfilename+'.en', 'w', encoding='utf-8') as mafile:
            for line in mlines:
                mafile.write(line.strip())
                if line != mlines[-1]:
                    mafile.write('\n')

    def remove_empty_lines(self, mlines, tlines):
        print('removing empty lines')
        print('Before Empty - ', len(mlines), len(tlines))
        remove_indices = []
        for line in tlines:
            if line.isspace() or line.isnumeric() or not line or line == '\n' or line.strip()=="":
                remove_indices.append(tlines.index(line))
                tlines.remove(line)
        for index in sorted(remove_indices,reverse=True):
            del mlines[index]
        remove_indices = []
        for line in mlines:
            if line.isspace() or line.isnumeric() or not line or line == '\n':
                remove_indices.append(mlines.index(line))
                mlines.remove(line)
        print(remove_indices)
        for index in sorted(remove_indices, reverse=True):
            del tlines[index]
        print('After Empty - ', len(mlines), len(tlines))
        return mlines, tlines

    def remove_non_utf_char(self, mlines, tlines):
        print('removing non-utf')
        print('Before non-utf - ', len(mlines), len(tlines))
        mlines = [line.replace('�', '') for line in mlines]
        tlines = [line.replace('�', '') for line in tlines]
        print('After utf - ', len(mlines), len(tlines))
        return mlines, tlines

    def check_duplicates(self, mlines, tlines):
        print('removing duplicates')
        print('Before duplicates - ', len(mlines), len(tlines))
        if(set(tlines)==tlines):
            print('no duplicates')
        else:
            indices=[]
            #indices = [idx for idx, item in enumerate(tlines) if item in tlines[:idx]]
            for idx,item in enumerate(tlines):
                if item in tlines[:idx]:
                    indices.append(idx)
            print(len(indices))
            for index in sorted(indices,reverse=True):
                del mlines[index]
                del tlines[index]
        print('After duplicates - ', len(mlines), len(tlines))
        return mlines, tlines

    def tokenise(self, mlines, tlines):
        for line in tlines:
            words = indic_tokenize.trivial_tokenize_indic(line)
            line = " ".join(words)
        for line in mlines:
            words = word_tokenize(line)
            line = " ".join(words)
        return mlines, tlines

    def remove_untranslated(self, mlines, tlines):
        indices = []
        print('Before untranslated', len(mlines), len(tlines))
        for idx, item in enumerate(tlines):
            tamil_words=indic_tokenize.trivial_tokenize_indic(item)
            english_words=word_tokenize(mlines[idx])
            for word in english_words:
                if word in tamil_words:
                    print(idx)
                    item.replace(word, "")
                    mlines[idx].replace(word,"")
        print('After untranslated',len(mlines), len(tlines))
        return mlines, tlines

if __name__ == '__main__':
    corpus = ['OpenSubtitles.en-ta', 'en-tam-v2-parallel']
    for c in corpus:
        print(c)
        dp = DataPreProcessing(combinedfilename='D:/Projects/TamilYTube-Dataset/combined-corpus/{co}'.format(co=c))
        mlines, tlines = dp.get_lines()
        mlines, tlines = dp.remove_untranslated(mlines=mlines, tlines=tlines)
        mlines, tlines = dp.remove_empty_lines(mlines=mlines,tlines=tlines)
        mlines, tlines = dp.check_duplicates(mlines=mlines,tlines=tlines)
        mlines, tlines = dp.remove_non_utf_char(mlines=mlines, tlines=tlines)
        mlines, tlines = dp.tokenise(mlines=mlines, tlines=tlines)
        dp.append_lines(mlines=mlines,tlines=tlines)
