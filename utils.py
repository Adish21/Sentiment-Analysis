import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

def extract_article_text(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        h1 = soup.find('h1').text if soup.find('h1') else ''
        p_tags = ' '.join([p.text for p in soup.find_all('p')])
        return h1 + " " + p_tags
    except Exception as e:
        return "Could not extract content."

def generate_summary(text):
    try:
        return summarize(text, word_count=50).split('. ')
    except:
        return ["Summary not available."]
