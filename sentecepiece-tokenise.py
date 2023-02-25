import sentencepiece as spm
from indicnlp.tokenize import indic_detokenize

#Creating combined training corpus
# corpus_trans = ['trans-yt-cook', 'en-tam-v2-parallel', 'train']
# corpus_asr = ['asr-yt-cook', 'en-tam-v2-parallel', 'train']
# corpus_full = ['en-tam-v2-parallel', 'train']
# with open('data/corpus/train.trans.txt.en', 'w', encoding='utf-8') as wf:
#     for corpus in corpus_trans:
#         with open('data/corpus/{co}.en'.format(co=corpus), 'r', encoding='utf-8') as rf:
#             lines = rf.readlines()
#             for line in lines:
#                 if line!=lines[-1]:
#                     wf.write(line)
#                 else:
#                     wf.write(line.strip())
#
# with open('data/corpus/train.trans.txt.ta', 'w', encoding='utf-8') as wf:
#     for corpus in corpus_trans:
#         with open('data/corpus/{co}.ta'.format(co=corpus), 'r', encoding='utf-8') as rf:
#             lines = rf.readlines()
#             for line in lines:
#                 if line!=lines[-1]:
#                     wf.write(line)
#                 else:
#                     wf.write(line.strip())
#
# with open('data/corpus/train.asr.txt.en', 'w', encoding='utf-8') as wf:
#     for corpus in corpus_asr:
#         with open('data/corpus/{co}.en'.format(co=corpus), 'r', encoding='utf-8') as rf:
#             lines = rf.readlines()
#             for line in lines:
#                 if line!=lines[-1]:
#                     wf.write(line)
#                 else:
#                     wf.write(line.strip())
# with open('data/corpus/train.asr.txt.ta', 'w', encoding='utf-8') as wf:
#     for corpus in corpus_asr:
#         with open('data/corpus/{co}.ta'.format(co=corpus), 'r', encoding='utf-8') as rf:
#             lines = rf.readlines()
#             for line in lines:
#                 if line!=lines[-1]:
#                     wf.write(line)
#                 else:
#                     wf.write(line.strip())
#
# with open('data/corpus/train.txt.en', 'w', encoding='utf-8') as wf:
#     for corpus in corpus_full:
#         with open('data/corpus/{co}.en'.format(co=corpus), 'r', encoding='utf-8') as rf:
#             lines = rf.readlines()
#             for line in lines:
#                 if line!=lines[-1]:
#                     wf.write(line)
#                 else:
#                     wf.write(line.strip())
# with open('data/corpus/train.txt.ta', 'w', encoding='utf-8') as wf:
#     for corpus in corpus_full:
#         with open('data/corpus/{co}.ta'.format(co=corpus), 'r', encoding='utf-8') as rf:
#             lines = rf.readlines()
#             for line in lines:
#                 if line!=lines[-1]:
#                     wf.write(line)
#                 else:
#                     wf.write(line.strip())
#
corpus = 'asr-yt-only'
#Creating SP model
# spm.SentencePieceTrainer.Train('--input=data/{co}/train.en --model_prefix=data/{co}/sp/en_model --model_type=bpe --character_coverage=1.0 --vocab_size=16000'.format(co=corpus))
# spm.SentencePieceTrainer.Train('--input=data/{co}/train.ta --model_prefix=data/{co}/sp/ta_model --model_type=bpe --vocab_size=16000'.format(co=corpus))

#Tokenisation for training
# sp = spm.SentencePieceProcessor(model_file='data/{co}/sp/en_model.model'.format(co=corpus))
# with open('data/{co}/test.en'.format(co=corpus), 'r', encoding='utf-8') as rf, open('data/{co}/test.en.sp'.format(co=corpus), 'w', encoding='utf-8') as wf:
#     for line in rf:
#         wf.write(' '.join(sp.encode(line, out_type=str)))
#         wf.write('\n')
#
# sp = spm.SentencePieceProcessor(model_file='data/{co}/sp/ta_model.model'.format(co=corpus))
# with open('data/{co}/test.ta'.format(co=corpus), 'r', encoding='utf-8') as rf, open('data/{co}/test.ta.sp'.format(co=corpus), 'w', encoding='utf-8') as wf:
#     for line in rf:
#         wf.write(' '.join(sp.encode(line, out_type=str)))
#         wf.write('\n')

# #De-Tokenisation for testing
# sp = spm.SentencePieceProcessor(model_file='data/{co}/sp/ta_model.model'.format(co=corpus))
# with open('data/{co}/test.ta'.format(co=corpus), 'r', encoding='utf-8') as rf:
#     lines = rf.readlines()
#     with open('data/{co}/test.ta'.format(co=corpus), 'w', encoding='utf-8') as wf:
#         for line in lines:
#             line = indic_detokenize.trivial_detokenize_indic(line)
#             print(line)
#             wf.write(line.strip())
#             if line != lines[-1]:
#                 wf.write('\n')
#
# sp = spm.SentencePieceProcessor(model_file='data/{co}/sp/ta_model.model'.format(co=corpus))
# with open('data/{co}/pred.ta.sp'.format(co=corpus), 'r', encoding='utf-8') as rf, open('data/{co}/pred.ta'.format(co=corpus), 'w', encoding='utf-8') as wf:
#     lines = rf.readlines()
#     for line in lines:
#         line = ''.join(sp.Decode(line)).replace(' ','').replace('▁', ' ')
#         #line = indic_detokenize.trivial_detokenize_indic(line)
#         wf.write(line.strip())
#         if line != lines[-1]:
#             wf.write('\n')