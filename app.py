from flask import Flask, render_template, redirect, request
from log_reg import wine_type, wine_quality
import log_reg
# import flask
app = Flask(__name__)



@app.route("/")
def index():
    model_score, params_table, result_table, class_report, conf_table = wine_type()
    # if request.method == 'POST':
    #     return render_template("index.html", result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table, class_report=class_report)  
    return render_template("index.html", result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table, class_report=class_report)
    # return(render_template("index.html"))

@app.route("/logistic", methods=["GET", "POST"])
def logistic():
    # model_score, params_table, result_table, class_report, conf_table = wine_type()
    params = wine_quality()
    return render_template("index.html", params=params)

if __name__ == "__main__":
    app.run(debug=True)

