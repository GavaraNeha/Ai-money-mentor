from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

history = []

def generate_ai_advice(income, rent, food, other, savings):
    advice_list = []

    if savings < 0:
        advice_list.append("You are overspending and need to control expenses.")
    elif savings < income * 0.2:
        advice_list.append("Your savings are below recommended levels.")
    else:
        advice_list.append("You are maintaining a healthy savings habit.")

    if food > income * 0.4:
        advice_list.append("Food expenses are high.")
    if rent > income * 0.5:
        advice_list.append("Rent is consuming too much income.")
    if other > income * 0.3:
        advice_list.append("Other expenses are high.")

    tips = [
        "Follow the 50-30-20 rule.",
        "Track spending weekly.",
        "Reduce unnecessary expenses.",
        "Plan your budget properly."
    ]

    advice_list.append(random.choice(tips))
    return "💡 " + " ".join(advice_list)


@app.route("/", methods=["GET", "POST"])
def home():
    global history

    advice = ""
    savings = 0
    rent = food = other = goal = time = income = 0
    progress = 0
    score = 0
    monthly_required = 0
    recommendation = ""

    if request.method == "POST":
        income = int(request.form["income"])
        rent = int(request.form["rent"])
        food = int(request.form["food"])
        other = int(request.form["other"])
        goal = int(request.form["goal"])
        time = int(request.form["time"])

        expenses = rent + food + other
        savings = income - expenses

        history.append({"income": income, "savings": savings})

        if time > 0:
            monthly_required = round(goal / time)

        if goal > 0:
            progress = int((savings / goal) * 100)
            progress = min(progress, 100)

        if savings > 0:
            score += 20
        if savings > income * 0.2:
            score += 20
        if rent < income * 0.3:
            score += 20
        if food < income * 0.25:
            score += 20
        if other < income * 0.2:
            score += 20

        advice = generate_ai_advice(income, rent, food, other, savings)

        if savings < 0:
            recommendation = f"Cut expenses by ₹{abs(savings)}"
        elif savings < monthly_required:
            recommendation = f"Increase savings by ₹{monthly_required - savings}"
        else:
            recommendation = "Maintain current strategy"

    return render_template("index.html",
                           advice=advice,
                           savings=savings,
                           rent=rent,
                           food=food,
                           other=other,
                           goal=goal,
                           progress=progress,
                           history=history,
                           score=score,
                           monthly_required=monthly_required,
                           recommendation=recommendation,
                           income=income)


@app.route("/reset")
def reset():
    global history
    history = []
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)