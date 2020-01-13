from flask import Flask, render_template, redirect, request
from log_reg import wine_type, wine_quality
import log_reg
# import flask
app = Flask(__name__)

title_Features = "Features"
title_Score = "Score: "
title_Classification_Report = "Classification Report"
title_Confusion_Matrix = "Confusion Matrix" 

@app.route("/")
def index():
    # model_score, params_table, result_table, class_report, conf_table = wine_type()
    # if request.method == 'POST':
    #     return render_template("index.html", result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table, class_report=class_report) 
    return render_template("index.html")


    # return render_template("index.html", title_Features=title_Features, title_Score=title_Score, title_Classification_Report=title_Classification_Report,\
        # title_Confusion_Matrix=title_Confusion_Matrix)

@app.route("/logistic_regression")
def logistic_regression():
    model_score, params_table, result_table, class_report, conf_table = wine_type()
    return render_template("index.html", title_Features=title_Features, title_Score=title_Score, title_Classification_Report=title_Classification_Report,\
        title_Confusion_Matrix=title_Confusion_Matrix, result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table,\
             class_report=class_report)



@app.route("/random_forrest")
def random_forrest():
   
    return render_template("index.html", params=params)



@app.route("/knn")
def knn():
  
    return render_template("index.html", params=params)



@app.route("/svc")
def svc():
   
    return render_template("index.html", params=params)

if __name__ == "__main__":
    app.run(debug=True)

