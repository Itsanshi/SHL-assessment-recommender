# SHL Assessment Recommender

An AI-powered recommendation system that suggests the most relevant SHL assessments based on job descriptions, built as a web-based RAG-style tool over an SHL product catalog.

## Live Deployment

- **Frontend (web app)**: `https://shl-assessment-recommender-ub15.vercel.app/`
- **Backend API**: `https://shl-assessment-recommender-4-howsonrender.com`;

	- Health: `GET /health`
	- Docs / Try-it UI: `GET /docs`
	- Recommend endpoint: `POST /recommend`

The frontend calls the deployed backend over HTTPS and returns recommendations in real time.

## Features

- **Catalog-based recommendations**: Uses an SHL assessment catalog with rich metadata.
- **LLM/RAG-ready design**: Retrieval layer is structured to plug in embeddings + FAISS later.
- **FastAPI REST API**: Simple JSON interface for programmatic access.
- **Web interface**: Clean, minimal UI for recruiters / hiring managers.
- **Evaluation framework**: Scripts to score recommendation quality on labeled data.
- **Data pipeline**: Crawler and cleaning utilities for building/updating the catalog.

## Project Structure

```
shl-assessment-recommender/
│
├── backend/              # FastAPI service and retrieval logic
│   ├── app.py            # API endpoints (/health, /recommend)
│   ├── retriever.py      # In-memory keyword-based retriever (FAISS-ready)
│   ├── utils.py          # Formatting + normalization helpers
│   ├── requirements.txt  # Backend dependencies
│   └── data/             # Catalog and placeholder index files
│
├── crawler/              # Data collection and cleaning scripts
├── evaluation/           # Evaluation scripts and labeled train.csv
├── inference/            # Batch inference utilities (e.g., Anshika_Anand.csv writer)
├── frontend/             # Static web UI (HTML/CSS/JS)
├── vercel.json           # Vercel config to serve frontend/
├── README.md
└── .gitignore
```

## Backend (FastAPI)

The backend is implemented in `backend/app.py` using FastAPI.

- **Endpoints**
	- `GET /` – simple JSON greeting with available endpoints.
	- `GET /health` – returns `{ "status": "healthy" }`.
	- `POST /recommend` – accepts a JSON body:

		```json
		{ "query": "Software Engineer with Python experience" }
		```

		and returns:

		```json
		{
			"recommended_assessments": [
				{
					"name": "...",
					"description": "...",
					"duration": 30,
					"test_type": ["..."],
					"url": "...",
					"adaptive_support": "Yes",
					"remote_support": "Yes"
				}
			]
		}
		```

- **Retrieval logic** (`backend/retriever.py`)
	- Currently uses a small in-memory set of representative SHL assessments.
	- Scores them via simple keyword overlap between query and assessment text.
	- Structured to be replaced later by a true embedding + FAISS index.

- **CORS**
	- Configured via `CORSMiddleware` to allow browser-based UIs (local and Vercel) to call the API.

### Run backend locally

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Then test:

- `http://localhost:8000/health`
- `http://localhost:8000/docs`

## Frontend (Vercel)

The frontend is a static app in `frontend/` deployed on Vercel.

- `index.html` – main page with input box and "Recommend" button.
- `style.css` – basic styling for layout and result cards.
- `app.js` – calls the Render backend:

	```javascript
	const API_URL = "https://shl-assessment-recommender-1-i99s.onrender.com/recommend";

	const response = await fetch(API_URL, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ query })
	});
	```

### Run frontend locally

```bash
cd frontend
python -m http.server 5500
```

Then open `http://localhost:5500` and click **Recommend**.

## Evaluation

Basic evaluation utilities live under `evaluation/`:

- `train.csv` – labeled pairs of `(job_description, assessment_id, label)`.
- `evaluate.py` – loads predictions and ground truth, computes precision/recall/F1.

## Batch Inference

`inference/generate_predictions.py` reads `inference/test.csv`, runs the retriever, and writes a submission-style file:

```bash
cd inference
python generate_predictions.py
```

Output: `Anshika_Anand.csv` at the repo root with columns:

- `Query`
- `Assessment_url`

## License

MIT License
