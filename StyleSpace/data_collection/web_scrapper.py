import requests
from bs4 import BeautifulSoup

def scrape_fashion_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    fashion_data = []

    for item in soup.find_all('div', class_='fashion-item'):
        title = item.find('h2').text
        image_url = item.find('img')['src']
        fashion_data.append({'title': title, 'image_url': image_url})
    
    return fashion_data

if __name__ == "__main__":
    url = 'https://example-fashion-website.com/trends'
    data = scrape_fashion_data(url)
    print(data)
