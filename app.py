import requests
from bs4 import BeautifulSoup

category = input("Which category are you interested: ")
url = f"https://wallhaven.cc/search?q={category}"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
links = soup.find_all("a", "preview")
first_link = links[0]
wallpaper_location = first_link["href"]

r2 = requests.get(wallpaper_location)
soup2 = BeautifulSoup(r2.content, "html.parser")
img_tag = soup2.find(id="wallpaper")
alt = img_tag["alt"]
src = img_tag["src"]

# Download image
wallpaper = requests.get(src)
open(f"{category}.jpg", "wb").write(wallpaper.content)
