import random
import requests
import uuid
from bs4 import BeautifulSoup

while True:
    category = input("Which category are you interested: ")
    words_in_category = category.casefold().rsplit(" ")
    url = ""
    if len(words_in_category) == 1:
        url = f"https://wallhaven.cc/search?q={category}"
    else:
        category_no_spaces = category.strip()
        category = category_no_spaces.replace(" ", "+")
        url = f"https://wallhaven.cc/search?q={category}"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    notice = str(soup.find("p", "pagination-notice")).rsplit(" ")
    category_found = True

    for word in notice:
        if "nothing" == word:
            category_found = False
            print("Category not found.")

    if category_found == True:
        links = soup.find_all("a", "preview")
        links_length = len(links) - 1
        random_link = random.randint(0, links_length)
        first_link = links[random_link]
        wallpaper_location = first_link["href"]

        r2 = requests.get(wallpaper_location)
        soup2 = BeautifulSoup(r2.content, "html.parser")
        img_tag = soup2.find(id="wallpaper")
        alt = img_tag["alt"]
        src = img_tag["src"]
        random_id = str(uuid.uuid4()).rsplit("-")[-1]

        # Download image
        wallpaper = requests.get(src)
        if "+" in category:
            category = category.replace("+", "-")
        open(f"{category}.jpg", "wb").write(wallpaper.content)
