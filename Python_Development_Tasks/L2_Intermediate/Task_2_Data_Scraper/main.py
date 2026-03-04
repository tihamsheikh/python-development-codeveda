import requests 
import csv
import os
from bs4 import BeautifulSoup 
from fake_useragent import UserAgent 
import time
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv 

load_dotenv()


# Define directory and file path
directory = Path("data")
file_path = directory / f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}_scraped_data.csv"
# print(file_path)

proxie_auth = os.getenv("PROXIE_AUTH")

url = "https://www.kalerkantho.com/special/recent"


header = {
    "User-Agent": UserAgent().random,
    "Connection": "keep-alive",
    "referer": "https://www.google.com/"
}

proxie = {
    "http" : f"http://{proxie_auth}"
}

session = requests.Session()
time.sleep(2)
response = session.get(url=url, proxies=proxie, headers=header)
# print(response.status_code, "hi")

if response.status_code == 200:

    result = response.text 

    soup = BeautifulSoup(result, "html.parser")
    titles = soup.find_all("h5", class_="card-title")
    source = soup.find_all("span", class_="text-dangers")

    # for title in titles:
    #     print(title.text.strip())

    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Source"])
        for i, title in enumerate(titles):
            writer.writerow([title.text.strip(), source[i].text.strip() if i < len(source) else "N/A"])

    print(f"Data has been successfully scraped and saved to {file_path}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")