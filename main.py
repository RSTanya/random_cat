import requests

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    str_result = response.text
    result = json.loads(str_result)

    return render_template('index.html', cats=result[0])


if __name__ == "__main__":
    app.run(debug=True)
