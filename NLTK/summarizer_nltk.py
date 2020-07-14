# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
   
# Input text - to summarize  
text = """
OpenGenus Foundation is an open-source non-profit organization with the aim to enable people to work offline for a longer stretch, reduce the time spent on searching by exploiting the fact that almost 90% of the searches are same for every generation and to make programming more accessible.OpenGenus is all about positivity and innovation.Over 1000 people have contributed to our missions and joined our family. We have been sponsored by three great companies namely Discourse, GitHub and DigitalOcean. We run one of the most popular Internship program and open-source projects and have made a positive impact over people's life.
"""
   
# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 

freqTable = dict() 
for word in words: 
    word = word.lower() 
    if word in stopWords: 
        continue
    if word in freqTable: 
        freqTable[word] += 1
    else: 
        freqTable[word] = 1

sentences = sent_tokenize(text) 
sentenceValue = dict() 
   
for sentence in sentences: 
    for word, freq in freqTable.items(): 
        if word in sentence.lower(): 
            if sentence in sentenceValue: 
                sentenceValue[sentence] += freq 
            else: 
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue: 
    sumValues += sentenceValue[sentence] 
   
# Average value of a sentence from the original text 
   
average = int(sumValues / len(sentenceValue)) 
   
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
        summary += " " + sentence 
print(summary) 