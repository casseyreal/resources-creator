import requests
import csv

id_start = 2000
resource_id = id_start
query = ["netflix", "disney", "spotify", "youtube", "philippines"]
with open('resources-7.csv', mode='w') as resource_file:
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
    for q in query:
        url = 'https://newsapi.org/v2/everything?q={}&sortBy=top&pageSize=100' \
              '&language=en&apiKey=571cc0052b524088a445d2a13b29b209'.format(q)
        response = requests.get(url)
        response_json = response.json()
        articles = response_json['articles']
        for item in articles:
            if item["urlToImage"] != "null":
                writer.writerow([
                    resource_id,
                    "item",
                    item["source"]["name"],
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

    print("Total resources added:", resource_id-id_start)
