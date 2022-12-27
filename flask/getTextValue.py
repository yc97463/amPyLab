from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "Success "+request.values.get("username")
    return render_template("postSubmit.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
