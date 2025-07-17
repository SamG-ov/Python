from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
#print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
#article_text = articles.getText()
#article_link = articles.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_index = article_upvotes.index(max(article_upvotes))
#You can find the largest votes and choose the title and link for that

print(article_texts)
print(article_links)
print(article_upvotes)