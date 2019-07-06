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
    return output

#返回分词列表
def getWordCutResult(sentence):
    stopwordList = stopWordList("D:\\程设大作业NLP\\CasewardNLP\\stopword.txt")
    output = wordCut(sentence, stopwordList)
    return output
