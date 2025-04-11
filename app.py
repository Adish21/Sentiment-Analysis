from flask import Flask, render_template, request, jsonify
from cnn_model import predict_sentiment
from utils import extract_article_text, generate_summary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    input_text = request.form['inputText']
    is_url = input_text.startswith("http")
    
    if is_url:
        full_text = extract_article_text(input_text)
    else:
        full_text = input_text

    sentiment = predict_sentiment(full_text)
    summary = generate_summary(full_text)
    
    return jsonify({
        "sentiment": sentiment,
        "summary": summary
    })

if __name__ == '__main__':
    app.run(debug=True)
