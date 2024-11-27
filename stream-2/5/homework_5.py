import re
import json
import requests
import sqlite3


def write_sql(data: list) -> None:
    filename = 'vacancies.db'

    # 1. create table
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT NOT NULL
        )
    """)

    # 2. insert data
    for idx, item in enumerate(data, start=1):  # generate id from 1 to 12
        cursor.execute("""
            INSERT OR REPLACE INTO vacancies (id, title, url)
            VALUES (?, ?, ?)
        """, (idx, item['title'], item['url']))

    conn.commit()
    conn.close()


def read_sql() -> None:
    filename = 'vacancies.db'

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    # 1. get all data
    cursor.execute("SELECT id, title, url FROM vacancies")
    rows = cursor.fetchall()

    print("vacancy list from db:")
    for row in rows:
        print(f"id: {row[0]}, title: {row[1]}, url: {row[2]}")

    conn.close()


def save_to_json(data: list) -> None:
    filename = 'vacancies.json'
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"save to json: {filename}")


def main():
    url = "https://www.lejobadequat.com/emplois"

    response = requests.get(url)
    response.raise_for_status()
    html_content = response.text

    pattern = re.compile(
        r'<a href="(https://www\.lejobadequat\.com/emplois/[^"]+)"[^>]*>.*?<h3 class="jobCard_title m-0">([^<]+)</h3>',
        re.DOTALL
    )
    matches = pattern.findall(html_content)

    vacancies = [{"title": title.strip(), "url": link} for link, title in matches]

    print("vacancy list:")
    print(json.dumps(vacancies, ensure_ascii=False, indent=4))

    # save to JSON
    write_sql(vacancies)
    save_to_json(vacancies)

    read_sql()


if __name__ == '__main__':
    main()
