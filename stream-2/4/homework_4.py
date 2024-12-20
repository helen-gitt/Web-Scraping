import re
import requests
import hashlib
import html


# html
def get_content(url):
    name = hashlib.md5(url.encode('utf-8')).hexdigest()
    try:
        with open(name, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except:
        response = requests.get(url)
        response.encoding = 'ISO-8859-1'  # замість 'utf-8'
        print('request was sent')
        with open(name, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return response.text

# vacancy
def extract_and_save_vacancy_titles(html_content, filename):
    pattern = r'<h3 class="jobCard_title m-0">(.*?)</h3>'
    titles = [html.unescape(title.strip()) for title in re.findall(pattern, html_content, re.DOTALL)]
    with open(filename, 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')
    print(f"Список вакансій збережено у файл: {filename}")


if __name__ == '__main__':
    url = 'https://www.lejobadequat.com/emplois'
    html_content = get_content(url)
    if html_content:
        extract_and_save_vacancy_titles(html_content, 'vacancy_titles.txt')