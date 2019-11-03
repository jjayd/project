from soykeyword.proportion import CorpusbasedKeywordExtractor
corpusbased_extractor = CorpusbasedKeywordExtractor(
    min_tf=20,
    min_df=2,
    tokenize=lambda x:x.strip().split(),
    verbose=True
)

# docs: list of str like

f=open('text/news/input5-1.txt','r')
lines=""
while True:
	line = f.readline()
	if not line: break
	lines+=line


docs=corpusbased_extractor.train(lines)
keywords = corpusbased_extractor.extract_from_docs(
    docs,
    min_score=0.8,
)
print(keywords)
