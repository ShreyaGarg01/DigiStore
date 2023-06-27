import requests
import json
import random 

# def get_news():
#     BASE_URL = "https://saurav.tech/NewsAPI/"
#     top_headlines_api = "https://saurav.tech/NewsAPI//top-headlines/category/business/in.json"
#     # everything_api = "<BASE_URL>/everything/<source_id>.json"
#     res = requests.get(top_headlines_api).json()
#     response = res['articles'][0:6]
#     return response

def get_news():
    apikey = "6946fb967fc62eac509da39c343c6766"
    category = "business"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=in&max=10&apikey={apikey}"

    response = requests.get(url)
    data = response.json() 
    ret =  data['articles'][0:50]
    random.shuffle(ret)
    return ret 

# res = live_news() ; 
# print(type(res))

print(len((get_news())))

# data = res.json()
# print(type(data['articles'][0]))
# print(data)
# print(res['articles'][0])
# 'title'
# 'description'
# url
# urlToImage
# publishedAt



