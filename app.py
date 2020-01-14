from flask import Flask, render_template, redirect, request
from log_reg import wine_type, Logistic_Regression_Quality
import log_reg
# import flask
app = Flask(__name__)

title_Features = "Features"
title_Score = "Score: "
title_Classification_Report = "Classification Report"
title_Confusion_Matrix = "Confusion Matrix" 
title_Data = "Wine Data"
title_Wine_Type = "Wine Type"
title_Wine_Quality = "Wine Quality"
title_gridsearch = "Parameter Tuning with GridSearchCV"
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
    grid_search_quality, conf_table_quality, class_report_quality, result_table_quality, model_score_quality = Logistic_Regression_Quality()
    return render_template("index.html", title_Features=title_Features, title_Score=title_Score, title_Classification_Report=title_Classification_Report,\
        title_Confusion_Matrix=title_Confusion_Matrix, title_Wine_Quality=title_Wine_Quality, title_Wine_Type=title_Wine_Type, title_gridsearch=title_gridsearch, result_table=result_table, model_score=model_score, params_table=params_table, conf_table=conf_table,\
             class_report=class_report, grid_search_quality=grid_search_quality, conf_table_quality=conf_table_quality, class_report_quality=class_report_quality\
                 , result_table_quality=result_table_quality, model_score_quality=model_score_quality)



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

