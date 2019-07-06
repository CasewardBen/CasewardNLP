from snownlp import SnowNLP

#返回情感分析结果
def get_sentiment(text):
    score = SnowNLP(text)
    return score