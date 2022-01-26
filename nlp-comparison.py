from nltk.corpus import wordnet

#synonyms
syns = wordnet.synsets("program")
print(syns)
print(syns[0])
print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].lemmas()[0].name(), syns[0].definition())
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("syns: ", set(synonyms))
print("ants: ", set(antonyms))

word1 = wordnet.synset("good.n.01")
word2 = wordnet.synset("evil.n.01")

print(word1.wup_similarity(word2))

