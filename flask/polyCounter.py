from flask import Flask, request, render_template
import sympy as sp
from sympy import *


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        x = sp.symbols("x")
        func_f = request.values.get("function_f")
        func_g = request.values.get("function_g")
        action = request.values.get("action")
        tt = "("+func_f+")"+str(action)+"("+func_g+").simplify()"
        ans = eval(tt)
        return str(ans)
    return render_template("polySum.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
