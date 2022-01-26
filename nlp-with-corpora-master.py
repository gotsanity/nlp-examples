import nltk

# nltk.download()

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

print(train_text)

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sentence_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            #print(chunked)
            # chunked.draw()

    except Exception as e:
        print(str(e))

#process_content()

# lemmatizing
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("dogs"))
print(lemmatizer.lemmatize("warships"))
print(lemmatizer.lemmatize("geese"))

#the default behaver than noun. better than stemming generally
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", "a"))
print(lemmatizer.lemmatize("best", "a"))

print(lemmatizer.lemmatize("run", "n"))
print(lemmatizer.lemmatize("run", "v"))

#to find the corpus
#print(nltk.__file__)

#to compare words and such
from nltk.corpus import wordnet

#synonyms
syns = wordnet.synsets("program")
print(syns[0])
print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("boat.n.01")

print(word1.wup_similarity(word2))