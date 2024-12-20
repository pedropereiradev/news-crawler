from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_news

app = Flask(__name__)
CORS(app)

@app.route('/search_news', methods=['GET'])
def search_news():
    news = scrape_news()
    return jsonify({'news': news, 'count': len(news) }), 200

if __name__ == '__main__':
    app.run(port=5000)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
