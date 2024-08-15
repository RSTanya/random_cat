import requests

from flask import Flask, render_template
import json

app = Flask(__name__)


def get_cat():
    cat = {}
    while not cat:
        # print("hi")
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        str_result = response.text
        result = json.loads(str_result)
        if result[0]["width"] <= 1000 and result[0]["height"] <= 1000:
            cat = result[0]
    return cat


@app.route('/')
def index():
    cat = get_cat()
    return render_template('index.html', cats=cat)


if __name__ == "__main__":
    app.run(debug=True)

print(get_cat())
