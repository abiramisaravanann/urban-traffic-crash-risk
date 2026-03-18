import requests

API_KEY = "AIzaSyAZpRRNHgPtLzFO7ipBzOlLuxRtsUz12W4"

keywords = [
    "chicago traffic accidents",
    "chicago road safety",
    "dangerous intersections chicago",
    "urban traffic accidents",
    "traffic accident news"
]

url = "https://www.googleapis.com/youtube/v3/search"

for word in keywords:

    params = {
        "part": "snippet",
        "q": word,
        "type": "video",
        "maxResults": 3,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("\nKeyword:", word)
    print("="*50)

    for item in data["items"]:
        print("Title:", item["snippet"]["title"])
        print("Description:", item["snippet"]["description"])
        print("-"*40)