from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv) != 3:
    print("Usage:python WebWordCount.py <url> <word>")

else:
    url = sys.argv[1]
    word = sys.argv[2]
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    count = text.lower().count(word.lower())
    
    print(f"+ URL: {url} \n+ Word: {word} \n+ Count: {count}")