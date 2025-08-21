from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")  # The folder needs to be named 'templates'. if there's another folder
    # inside that templates folder for exmaple 'new' and inside that folder is the html file then you have to write
    # "render_template("new/index.html")"
# if you have an IMAGE or CSS file to show in your site then have to create a folder named 'static',
# then use "static/image.png" or "static/style.css"


# @app.route("/summon.html")
# def summon():
#     return render_template("summon.html")


if __name__ == "__main__":
    app.run(debug=True)























