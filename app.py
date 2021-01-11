import requests

category = input("Which category are you interested: ")
url = f"https://wallhaven.cc/search?q={category}"
r = requests.get(url)
print(r.content)
