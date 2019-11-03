from soynlp.noun import NewsNounExtractor
from soynlp import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer

corpus_path = "text/news/articles.txt"
#corpus_path = "text/news/input5-1.txt"

corpus = DoublespaceLineCorpus(corpus_path, iter_sent=True)

#for n_sent, sent in enumerate(corpus):
#    print('sent %d: %s %s\n'%(n_sent, sent, '' ))

we = WordExtractor()
we.train(corpus)
scores = we.word_scores()
print(scores.keys())
'''
sentences = DoublespaceLineCorpus(corpus_path, iter_sent=False)
noun_extractor = LRNounExtractor()
nouns = noun_extractor.train_extract(sentences)
n = nouns.keys()
lists=""
for a in n:
	lists+=a
	lists+=" "
print(lists)
'''
#top = sorted(nouns.items(), key=lambda x:-x[1].frequency)[:1]
#print(top)

'''
word_extractor = WordExtractor()

nouns = word_extractor.train(sentences)

word_scores = word_extractor.extract()

top100  = sorted(nouns.items())

noun_extractor = LRNounExtractor()
nouns = noun_extractor.train_extract(sentences)
top100 = sorted(nouns.items(),key=lambda x:-x[1].frequency)[:10]
for i, (word,score) in enumerate(top100):
	print(word,score.score)
'''
