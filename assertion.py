import requests
import json


# as an expected language use the short form of language, for example write "en" instead "english".
def assert_check_language(locator_language, expected_language):
    url = "https://fast-and-highly-accurate-language-detection.p.rapidapi.com/detect"

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "fast-and-highly-accurate-language-detection.p.rapidapi.com",
        "X-RapidAPI-Key": "8cd77509eemsh8a10ba15bc498e9p18f406jsn6814a82a5198"
    }
    payload = {
        "text": locator_language,
        "includePredictions": False
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    detected_language = json.loads(response.text)["lang"]

    assert(detected_language == expected_language), \
        "Detected language is not correct. Expected '" + expected_language + "' got '" + detected_language + "'"
