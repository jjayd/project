from gensim.models.wrappers import FastText

model = FastText.load_fasttext_format('wiki.ko.bin')

print("Finish creating model")

print(model.most_similar('전자'))

print(model.similarity('전자', '전기'))
