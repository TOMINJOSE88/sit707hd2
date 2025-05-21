from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bmi", methods=["POST"])
def bmi():
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        if height <= 0:
            return render_template("index.html", error="Height must be greater than zero")
        bmi_value = round(weight / (height ** 2), 2)
        category = (
            "Underweight" if bmi_value < 18.5 else
            "Normal weight" if bmi_value < 25 else
            "Overweight" if bmi_value < 30 else
            "Obese"
        )
        return render_template("index.html", bmi=bmi_value, category=category)
    except (TypeError, ValueError):
        return render_template("index.html", error="Invalid input. Use numeric values for weight and height.")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
