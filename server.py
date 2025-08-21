import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Flask looks for templates in the "templates" folder by default
    return render_template("index.html")

if __name__ == "__main__":
    # Use PORT from the environment (Render sets this). Default to 5000 locally.
    port = int(os.environ.get("PORT", 5000))
    # Control debug via env too; default to True for local dev, set FLASK_DEBUG=0 on production
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
