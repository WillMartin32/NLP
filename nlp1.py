# pip install TextBlob
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

text = "Today is a beautiful day. Tomorrow looks like bad weather."
#text = "You are the best."
text2 = "Hey neighbors! We're having a birthday party friday night at nine thirty. If we're being too loud text us and we'll quiet down. Feel free to come say hi."

#blob = TextBlob(text)
blob2 = TextBlob(text2)

#print(blob.sentences)

#print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#print(round(blob.sentiment.polarity, 3))
#print(round(blob.sentiment.subjectivity, 3))

#print(round(blob2.sentiment.polarity, 3))
#print(round(blob2.sentiment.subjectivity, 3))

for sentence in blob2.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))

'''
for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))
'''
'''
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

#print(blob.sentiment)


for sentence in blob.sentences:
    print(sentence.sentiment)


spanish = blob.translate(to='es')

print(spanish)

chinese = blob.translate(to='zh')

print(chinese)

print(chinese.translate())


from textblob import Word

index = Word('index')

print(index.pluralize())

cacti = Word('cacti')
print(cacti.singularize())

#wordlist

animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#spellcheck and correction
word = Word('theyr')

print(word.spellcheck())

print(word.correct())

# Normalization
word1 = Word('studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

print(word1.lemmatize())
print(word2.lemmatize())

# Definitions, Syninyms and Antonyms from WordNet
happy = Word('happy')

print(happy.definitions)

print(happy.synsets)

for s in happy.synsets:
    for l in s.lemmas():
        print(l.name())

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)
'''