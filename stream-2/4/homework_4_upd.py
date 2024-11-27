import re
import json
import requests

url = "https://www.lejobadequat.com/emplois"

response = requests.get(url)
response.raise_for_status()  # Перевірка статусу відповіді
html_content = response.text  # Отримуємо HTML-контент

pattern = re.compile(
    r'<a href="(https://www\.lejobadequat\.com/emplois/[^"]+)"[^>]*>.*?<h3 class="jobCard_title m-0">([^<]+)</h3>',
    re.DOTALL
)

matches = pattern.findall(html_content)

vacancies = [{"title": title.strip(), "url": link} for link, title in matches]

output_file = "vacancy_titles_upd.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(vacancies, file, ensure_ascii=False, indent=4)

print(f"Список вакансій збережено у файл: {output_file}")