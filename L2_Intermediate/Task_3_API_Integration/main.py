import requests
import os
from dotenv import load_dotenv 
# from slugify import slugify 
from datetime import datetime, timedelta

load_dotenv()


# news_outlet = input("Enter a news outlet (e.g., bbc news, cnn): ").strip()
# news_outlet = slugify(news_outlet)
# # print(news_outlet)

# newsapi_key = os.getenv("NEWS_API_KEY")
# response = requests.get(f"https://newsapi.org/v2/top-headlines?sources={news_outlet}&apiKey={newsapi_key}")


topic = input("Enter any topic: ").strip()
prior_day = int(input("How old should the news be? (e.g.,(days) 7, 15): ").strip())


today = datetime.today()
past_date = (today - timedelta(days=prior_day)).strftime("%Y-%m-%d")

newsapi_key = os.getenv("NEWS_API_KEY")
response = requests.get(f"https://newsapi.org/v2/everything?q={topic}&from={past_date}&sortBy=popularity&apiKey={newsapi_key}")



if response.status_code == 200:
    data = response.json()
    if data["totalResults"] < 1:
        print(f"No articles found for the topic '{topic}'. Please check the topic and try again.")
        exit()

    articles = data["articles"]

    print("-" * 80)
    for article in articles:
        print(f"\033[1;34mTitle: {article['title']}\033[0m")
        print(f"\033[1;32mDescription: {article['description']}\033[0m")
        print(f"\033[1;36mURL: {article['url']}\033[0m")
        print(f"\033[90m{'-' * 80}\033[0m")


else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")