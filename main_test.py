from flask import Flask, request, render_template, jsonify
import json
web = Flask(__name__)
import cut_word
import sentiment_test1
import keyword_test1
import word_property_test1
import cluster_test1

@web.route("/index")
def firstGate():
    return render_template("index.html")

@web.route("/cluster")
def clusterGate():
    return render_template("cluster.html")

@web.route("/sentiment_analysis")
def sentimentGate():
    return render_template("sentiment_analysis.html")

@web.route("/classify")
def classifyGate():
    return render_template("classify.html")

@web.route("/word_property")
def wordPropertyGate():
    return render_template("word_property.html")

@web.route("/keyword")
def keywordGate():
    return render_template("keyword.html")

@web.route("/word_property/get_cutword", methods=['GET', 'POST'])
def get_wordcut():
    sentence = request.args.get('sentence')
    theSentence = sentence
    output = cut_word.getWordCutResult(theSentence)
    detail = {'cutSentence': output}
    wordDict, propertyDict = word_property_test1.get_wordProperty(theSentence)
    return jsonify(detail, wordDict, propertyDict)

@web.route("/sentiment_analysis/get_score", methods=['GET', 'POST'])
def get_score():
    sentence = request.args.get('sentence')
    theSentence = sentence
    s = sentiment_test1.get_sentiment(theSentence)
    score = s.sentiments
    print('##################score:'+str(score))
    theScore = {'score':score}
    return jsonify(theScore)

@web.route("/keyword_test1/get_keywords", methods=['GET', 'POST'])
def get_keywords():
    sentence = request.args.get('sentence')
    theSentence = sentence
    keywords = keyword_test1.get_keywords(theSentence)
    print(keywords)
    keywordsDict=dict()
    if keywords[0]:
        keywordsDict['0']=keywords[0]
    if keywords[1]:
        keywordsDict['1']=keywords[1]
    if keywords[2]:
        keywordsDict['2']=keywords[2]
    if keywords[3]:
        keywordsDict['3']=keywords[3]
    if keywords[4]:
        keywordsDict['4']=keywords[4]
    #keywordsDict = {'0':keywords[0], '1':keywords[1], '2':keywords[2], '3':keywords[3], '4':keywords[4]}
    return jsonify(keywordsDict)

@web.route("/cluster/get_result", methods=['GET','POST'])
def get_clusterResult():
    thetextDict = request.values.get('textDict')
    print("###############")
    print(thetextDict)
    thetextDict = json.loads(thetextDict)
    clusterResult=cluster_test1.get_clusterResult(thetextDict)
    staticResult = cluster_test1.get_static(clusterResult)
    return jsonify(clusterResult,staticResult)

@web.route("/classify/get_result", methods=['GET','POST'])
def get_classifyResult():
    thetextDict = request.values.get('textDict')
    thetextDict = json.loads(thetextDict)
    classifyResult=classify_test1.get_classifyResult(theTextDict)
    staticResult = classify_test1.get_static(classifyResult)
    return jsonify(classifyResult,staticResult)

if __name__ == "__main__":
    web.run(host="0.0.0.0", port = 8100, debug=True)