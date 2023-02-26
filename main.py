from flask import Flask

app = Flask("JobScrapper")


@app.route("/")
def home():
    return "Welcome to JobScrapper"


app.run()
