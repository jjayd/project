import tfidf
import unittest
import io
import re

class TestTfIdf(unittest.TestCase):
    def test_similarity(self):
        table = TfIdf()
        table.add_document("foo", ["a", "b", "c", "d", "e", "f", "g", "h"])
        table.add_document("bar", ["a", "b", "c", "i", "j", "k"])
        table.add_document("baz", ["k", "l", "m", "n"])

        self.assertEqual(
            table.similarities(["a", "b", "c"]),
            [["foo", 0.6875], ["bar", 0.75], ["baz", 0.0]])


if __name__ == "__main__":
    r1 = r= io.open('../out1.txt',mode='r', encoding='utf-8')
    r2 = r= io.open('../out2.txt',mode='r', encoding='utf-8')
    r3 = r= io.open('../out3.txt',mode='r', encoding='utf-8')

    table = tfidf.tfidf()

    day = r1.readline()
    company = r1.readline()
    line = r1.readline()
    listwords = line.replace("'",'').replace(' ','').replace('[','').replace(']','').split(',')
    table.addDocument(company[:-1],listwords)
    print(listwords)
    
    day = r2.readline()
    company = r2.readline()
    line = r2.readline()
    listwords = line.replace("'",'').replace(' ','').replace('[','').replace(']','').split(',')
    table.addDocument(company[:-1],listwords)
    print(listwords)

    day = r3.readline()
    company = r3.readline()
    line = r3.readline()
    listwords = line.replace("'",'').replace(' ','').replace('[','').replace(']','').split(',')
    table.addDocument(company[:-1],listwords)
    print(listwords)
    
    sim = table.similarities(["서울대","노조","재활용"])
    for s in sim:
        print(s)

