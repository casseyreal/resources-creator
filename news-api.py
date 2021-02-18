import requests
import csv

resource_id = 1
sources = ["cnn", "abc-news", "bbc-news", "business-insider", "buzzfeed", "polygon",
           "newsweek", "the-wall-street-journal", "time", "wired", "vice-news"]
with open('resources.csv', mode='w') as resource_file:
    writer = csv.writer(resource_file)
    writer.writerow([
        "resource-id",
        "resource-type",
        "source",
        "author",
        "title",
        "description",
        "url",
        "thumbnail",
        "publishedAt",
        "content",
        "pubDate"
    ])
    for source in sources:
        url = 'https://newsapi.org/v2/everything?sources={}&sortBy=top&pageSize=100' \
              '&language=en&apiKey=571cc0052b524088a445d2a13b29b209'.format(source)
        response = requests.get(url)
        response_json = response.json()
        articles = response_json['articles']
        for item in articles:
            if item["urlToImage"] != "null":
                writer.writerow([
                    resource_id,
                    "news",
                    source,
                    item["author"],
                    item["title"],
                    item["description"],
                    item["url"],
                    item["urlToImage"],
                    item["publishedAt"],
                    item["content"],
                    "1612154438"
                ])
                resource_id = resource_id + 1

    print("Total resources added:", resource_id)
