import requests


query=input("What type of news are you looking for?")
api="0b191060091747b9b5ac79aa368ee561"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-02-088&sortBy=publishedAt&apiKey={api}"

print(url)
r=requests.get(url)

data=r.json()
articles=data["articles"]

for index,article in enumerate(articles):
    print("Title:", article["title"])
    print(index+1,"Description:", article["description"],"\nURL:", article["url"])
    print("\n***********************************\n")