from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://swapi.dev/api"
PEOPLE = "/people"

@app.route('/skywalker')
def index():  # put application's code here

    response_json = requests.get(BASE_URL + PEOPLE + "/?search=skywalker").json()

    description =[]
    for result in response_json["results"]:
        character_title = result["name"] + " participated in "
        films_title = ""
        films_length = len(result["films"])
        for i, film in enumerate(result["films"]):
            title = get_title_film(film)

            if i < films_length - 1:
                films_title += title + ", "
            else:
                films_title = films_title[:-2] + " and " + title + ", "


        films_title = films_title[:-2] + "."
        description.append(character_title + films_title)

    return jsonify({
        'status': 200,
        'description': ' '.join(e for e in description)
    })


def get_title_film(url):
    response_json = requests.get(url).json()

    return response_json["title"]

if __name__ == '__main__':
    app.run(debug=True, port=8001, host="127.0.0.1")
