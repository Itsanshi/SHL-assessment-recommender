# Flask Backend for SHL Assessment Recommender
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    """Endpoint to get assessment recommendations"""
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)
