from flask import Flask, render_template
import datetime as dt
import requests
import random

app = Flask(__name__)


@app.route("/")
def home():
    current_year = dt.date.today().year
    print(current_year)
    random_number = random.randint(0, 9)
    return render_template(
        "index.html", current_year=current_year, random_number=random_number
    )


@app.route("/blog/<blog_id>")
def get_blog(blog_id):
    url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)

    all_posts = response.json()

    return render_template("blog.html", all_posts=all_posts, blog_id=int(blog_id))


@app.route("/guess/<name>")
def guess(name: str):
    agify_url = f"https://api.agify.io"
    genderize_url = f"https://api.genderize.io"
    parameters = {"name": name}

    agify_response = requests.get(url=agify_url, params=parameters)
    genderize_response = requests.get(url=genderize_url, params=parameters)
    agify_data = agify_response.json()
    genderize_data = genderize_response.json()

    age = agify_data["age"]
    gender = genderize_data["gender"]

    print(gender, age)
    if gender != None and age != None:
        return render_template("index.html", name=name, gender=gender, age=age)
    else:
        return render_template("try_again.html")


if __name__ == "__main__":
    app.run(debug=True)
