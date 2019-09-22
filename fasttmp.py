from __future__ import print_function
from gensim.models import KeyedVectors

# Creating the model
ko_model = KeyedVectors.load_word2vec_format('wiki.ko.vec')
ko_model.save('fasttext.model')

# Getting the tokens 
print("finish")
words = []
cnt=0
for word in ko_model.vocab:
        if cnt==10: break
        words.append(word)
        print(word)
        # Printing out number of tokens available
        print("Number of Tokens: {}".format(len(words)))

        # Printing out the dimension of a word vector 
        print("Dimension of a word vector: {}".format(
                len(ko_model[words[0]])
                ))

        # Print out the vector of a word 
        print("Vector components of a word: {}".format(
                ko_model[words[0]]
                ))

        print(words[0])
        cnt=cnt+1
