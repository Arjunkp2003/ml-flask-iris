from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from ml.predict import make_prediction

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["GET", "POST"])
def predict():
    if "user" not in session:
        flash("Please log in to access predictions.")
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        data = request.form.to_dict()
        for key in data:
            data[key] = float(data[key])
        result = make_prediction(data)
        class_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        result_name = class_map[result]
        return render_template("predict.html", prediction=result_name)
    return render_template("predict.html", prediction=None)
