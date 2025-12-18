# SHL Assessment Recommender

An AI-powered recommendation system that suggests the most relevant SHL assessments based on job descriptions.

## Features

- **Semantic Search**: Uses sentence embeddings and FAISS for efficient similarity search
- **REST API**: Flask-based backend for easy integration
- **Web Interface**: Clean, modern frontend for recommendations
- **Evaluation Framework**: Tools to measure recommendation quality
- **Data Pipeline**: Crawler and cleaning utilities for SHL catalog

## Project Structure

```
shl-assessment-recommender/
│
├── backend/              # Flask API and ML components
├── crawler/              # Data collection scripts
├── evaluation/           # Model evaluation tools
├── inference/            # Testing and prediction scripts
├── frontend/             # Web interface
├── README.md
└── .gitignore
```

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

Simply open `frontend/index.html` in a browser, or serve it with:

```bash
cd frontend
python -m http.server 8000
```

## Usage

1. Start the backend server
2. Open the frontend interface
3. Enter a job description
4. Get personalized assessment recommendations

## Components

- **Embeddings**: Sentence-BERT for text encoding
- **Retrieval**: FAISS for fast similarity search
- **API**: Flask REST API with CORS support
- **Frontend**: Vanilla JavaScript with modern CSS

## Evaluation

Run evaluation on test dataset:

```bash
cd evaluation
python evaluate.py
```

## License

MIT License
