import requests
import json

responseText = requests.get("https://gorest.co.in/public/v1/posts").text

posts = json.loads(responseText)["data"]

for post in posts:
    print(f"title: {post['title']}")
    print("============================")
