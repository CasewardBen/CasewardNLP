from snownlp import SnowNLP


#返回词性分析结果
def get_wordProperty(text):
    wordList = []
    propertyList = []
    wordDict = dict()
    propertyDict = dict()
    s = SnowNLP(text)
    tags = [x for x in s.tags]
    for wordtuple in tags:
        wordList.append(wordtuple[0])
        propertyList.append(wordtuple[1])
    for i in range(len(wordList)):
        wordDict[str(i)] = wordList[i]
        propertyDict[str(i)] = propertyList[i]
    return wordDict, propertyDict
