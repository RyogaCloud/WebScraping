import requests
import bs4

# response = requests.get("取得したいURL")
# print (response.text)

html_doc = requests.get("取得したいURL").text
soup = bs4.BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
# print(soup.prettify())

# ページのaタグを全て抜き出す
real_page_tags = soup.find_all("a")
for tag in real_page_tags:
    # print(tag)  # タグの取得
    print(tag.string)  # 取得したタグ内の文字を取得
    # print(tag.get("href"))  # 取得したタグの属性を取得