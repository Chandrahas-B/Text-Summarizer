from flask import Flask, render_template,request
import os
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer

model = SBertSummarizer('paraphrase-MiniLM-L6-v2')
app = Flask(__name__)
os.environ["TOKENIZERS_PARALLELISM"] = "false"

@app.route("/")
def msg():
    return render_template('index.html')

@app.route("/summarize", methods=['POST','GET'])
def getSummary():
    body=request.form['data']
    result = model(body, num_sentences=5)
    return render_template('summary.html',result=result)

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
