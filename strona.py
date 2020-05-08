from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("omnie.html")

@app.route("/projekty")
def projekty():
    return render_template("projekty.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")








if __name__ == "__main__":
    app.run()
