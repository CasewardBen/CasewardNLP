from snownlp import SnowNLP
import jieba
import pandas as pd
import codecs

#获取停用词表
def stopWordList(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

#对文本内容进行分词
def wordCut(sentence, stopwordDict):
    words = jieba.cut(sentence)
    wordList = list(words)
    output = ' '.join(wordList)
    #print(output)
    for word in wordList:
        if word in stopwordDict:
            output = output.replace(word, '')
    return output

#返回文本分词结果
def getWordCutResult(sentence):
    stopwordList = stopWordList("D:\\程设大作业NLP\\CasewardNLP\\stopword.txt")
    output = wordCut(sentence, stopwordList)
    return output

#设置只有名词或者英文可以作为关键词
def nounSentence(tags):
    nounList = []
    for wordtuple in tags:
        if wordtuple[1] == "n" or wordtuple[1] == "e":
            nounList.append(wordtuple[0])
    nounSentence = ' '.join(nounList)
    return nounSentence

#获取关键词
def get_keywords(text):
    output = getWordCutResult(text)
    s = SnowNLP(output)
    tags = [x for x in s.tags]
    #print("########"+str(tags))
    theNounSentence = nounSentence(tags)
    sNoun = SnowNLP(theNounSentence)
    keywords = sNoun.keywords(limit=5)
    print(keywords)
    return keywords
