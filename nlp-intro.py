import nltk

from nltk.corpus import state_union

#tokenizing

# example_text = "Hello Mr. Smith, how are you doing today? The weather is great. The sky is purple-blue."

example_text = state_union.raw("2005-GWBush.txt")

from nltk.tokenize import sent_tokenize, word_tokenize

#print(word_tokenize(example_text))


from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_text)

# filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)

filtered_sentence = [w for w in words if not w in stop_words]

# print(filtered_sentence)


#stemming 

# from nltk.stem import PorterStemmer

# ps = PorterStemmer()

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("dogs"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("warships"))

print(lemmatizer.lemmatize("better", "a"))
print(lemmatizer.lemmatize("best", "a"))

print(lemmatizer.lemmatize("runs", "n"))
print(lemmatizer.lemmatize("runs", "v"))

#for w in filtered_sentence:
#    print(lemmatizer.lemmatize(w))

