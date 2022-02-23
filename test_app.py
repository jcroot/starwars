import pytest, json
from app import get_title_film, index

def test_response_with_characters_skywalker():

    response_json = index()

    assert response_json == dict(status=200, description="Luke Skywalker participated in A New Hope, The Empire Strikes Back, Return of the Jedi and Revenge of the Sith. Anakin Skywalker participated in The Phantom Menace, Attack of the Clones and Revenge of the Sith. Shmi Skywalker participated in The Phantom Menace and Attack of the Clones.")

           # "{status:200, description: 'Luke Skywalker participated in A New Hope, The Empire Strikes Back, Return of the Jedi and Revenge of the Sith. Anakin Skywalker participated in The Phantom Menace, Attack of the Clones and Revenge of the Sith. Shmi Skywalker participated in The Phantom Menace and Attack of the Clones.'}"
