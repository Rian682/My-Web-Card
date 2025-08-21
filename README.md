# My-Web-Card

Simple Python backend that serves Jinja templates.

## What this repo contains
- `server.py` — the Python web server (Flask recommended)
- `templates/` — Jinja templates (index.html, etc.)
- `static/` — static assets (assets/, images/, css, js)
- `requirements.txt` — Python dependencies
- `seed.py` (optional) — data seeding script

## Local run (developer)
1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. Install deps: `pip install -r requirements.txt`
4. Run: `python server.py`
5. Open `http://localhost:5000` (or port your app uses)

## Deploy (Render)
1. Push this repo to GitHub.
2. Create a new **Web Service** on Render and connect to this repo.
3. Use build command: `pip install -r requirements.txt`
4. Use start command: `gunicorn server:app` (or `python server.py` if needed).
5. Add any required environment variables in Render dashboard.

## Notes
- **Do not** commit `.env` with secrets. Use Render's environment variable settings.
- Ensure `templates/` and `static/` remain in the repo for templates and assets to work.

