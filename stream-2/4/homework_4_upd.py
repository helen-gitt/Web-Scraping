import json
import requests
from bs4 import BeautifulSoup

url = "https://www.lejobadequat.com/emplois"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
vacancies = [
    {
        "title": card.find("h3", class_="jobCard_title").text.strip(),
        "url": f"https://www.lejobadequat.com{card.find('a', class_='jobCard_link')['href']}"
        if not card.find("a", class_="jobCard_link")["href"].startswith("http")
        else card.find("a", class_="jobCard_link")["href"]
    }
    for card in soup.find_all("article", class_="jobCard")
]

with open("vacancy_data.json", "w", encoding="utf-8") as f:
    json.dump(vacancies, f, ensure_ascii=False, indent=4)

    print("vacancy_data.json")