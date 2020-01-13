from flask import Flask, render_template, redirect, request
from log_reg import wine_type
# import flask
app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    model_score, params_table, result_table, class_report, conf_table = wine_type()
    if request.method == 'POST':
        return render_template("index.html", result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table, class_report=class_report)  
    return render_template("index.html", result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table, class_report=class_report)

@app.route("/logistic", methods=["GET", "POST"])
def logistic():
    model_score, params_table, result_table, class_report, conf_table = wine_type()
    return redirect(url_for("index.html"), code=302)
    
if __name__ == "__main__":
    app.run(debug=True)

