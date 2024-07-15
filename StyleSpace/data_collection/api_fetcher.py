import requests

def fetch_social_media_data(api_url, params):
    response = requests.get(api_url, params=params)
    return response.json()

if __name__ == "__main__":
    api_url = 'https://api.example.com/fashion-trends'
    params = {'hashtag': 'fashion'}
    data = fetch_social_media_data(api_url, params)
    print(data)
