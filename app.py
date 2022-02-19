from flask import Flask
from flask import request
from flask import render_template
import joblib

app = Flask(__name__)
linear_model = joblib.load("DBS_predict_linear")
tree_model = joblib.load("DBS_tree")
mlp_model = joblib.load("DBS_mlp")

# @ is a function decorator
# must run the app.route first before running any function below


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get('rates')
        print(rates)

        linear_pred = linear_model.predict([[float(rates)]])
        print(linear_pred)

        tree_pred = tree_model.predict([[float(rates)]])
        print(tree_pred)

        mlp_pred = mlp_model.predict([[float(rates)]])
        print(mlp_pred)

        # 2dp
        linear_share_price = "The Predicted DBS Share Price using Linear Regression model is: $" + \
            "{:.2f}".format(linear_pred[0][0])
        tree_share_price = "The Predicted DBS Share Price using Decision Tree model is: $" + \
            "{:.2f}".format(tree_pred[0])
        mlp_share_price = "The Predicted DBS Share Price using Neural Network model is: $" + \
            "{:.2f}".format(mlp_pred[0])

        return (render_template("index.html", result1=linear_share_price, result2=tree_share_price, result3=mlp_share_price))
    else:
        return (render_template("index.html", result1='No input submitted. Please submit a rate!', result2='No input submitted. Please submit a rate!', result3='No input submitted. Please submit a rate!'))
