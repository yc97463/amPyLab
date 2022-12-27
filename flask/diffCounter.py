from flask import Flask, request, render_template
import sympy as sp
from sympy import *


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        x = sp.symbols("x")
        ss = request.values.get("username")
        tt = "diff("+ss+")"
        ans = eval(tt)
        return "函數"+ss+"的微分是"+str(ans)
    return render_template("postSubmit.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
