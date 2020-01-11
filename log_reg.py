
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import random

def wine_me(target):
    target = target.lower()
    if target != "type" and target != "quality":
        return print("target must be type or quality")

    red = pd.read_csv("winequality-red.csv")
    white = pd.read_csv("winequality-white.csv")
    red = red.append(white)
    wine = red
    X = wine.drop(columns=["type", "quality"])
    if target == "type":
        y = wine["type"]
    elif target == "quality":
        y = wine["quality"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y)
    
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test) 
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_scaled, y_train)
    #param
    model_score = model.score(X_test_scaled, y_test)

    ran = random.randrange(0, len(y_test))
    current_params = X_test.iloc[ran]
    current_pred = model.predict([current_params])
    current_params = current_params.to_dict()
    current_params_df = pd.DataFrame(current_params, index=[1])
    params_table = current_params_df.to_html(index=False)
    #param
    params_table = params_table.replace("\n", "")

    data = {
    "Predicted": current_pred,
    "Actual": y_test.iloc[ran]
    }
    result_table = pd.DataFrame(data)
    result_table = result_table.to_html()
    #param
    result_table = result_table.replace("\n", "")
    return (model_score, params_table, result_table)








