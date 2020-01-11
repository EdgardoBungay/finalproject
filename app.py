from flask import Flask, render_template, redirect
from log_reg import wine_me

app = Flask(__name__)


@app.route("/")
def index():
    model_score, params_table, result_table = wine_me("type")
    return render_template("index.html", result_table=result_table, model_score=model_score, params_table=params_table)


@app.route("/predict")
def predict():
    
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
