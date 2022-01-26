import nltk

#download all
#nltk.download()

#build a tokenizer

example_text = "Hello Mr. Smith, how are you doing today? The weather is great. The sky is pinkish-blue. You should not eat cardboard."

#import some tokenizers
from nltk.tokenize import sent_tokenize, word_tokenize

#print(sent_tokenize(example_text))

# remove stop words
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

#print(stop_words)

words = word_tokenize(example_text)

# filtered_sentence = []

# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)

filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)

#stemming
from nltk.stem import PorterStemmer

ps = PorterStemmer()

for w in filtered_sentence:
    print(ps.stem(w))