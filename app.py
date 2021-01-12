import colorama
import os
import random
import requests
import uuid
from bs4 import BeautifulSoup

colorama.init()


while True:
    category = input(
        "Which category are you interested [to exit the program type quit]: "
    )
    if category == "quit":
        break
    words_in_category = category.casefold().rsplit(" ")
    url = ""
    if len(words_in_category) == 1:
        url = f"https://wallhaven.cc/search?q={category}"
    else:
        category_no_spaces = category.strip()
        category = category_no_spaces.replace(" ", "+")
        url = f"https://wallhaven.cc/search?q={category}"

    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    notice = str(soup.find("p", "pagination-notice")).rsplit(" ")
    category_found = True

    for word in notice:
        if "nothing" == word:
            category_found = False
            print("Category not found.")

    if category_found:
        links = soup.find_all("a", "preview")
        links_length = len(links) - 1
        random_link = random.randint(0, links_length)
        link = links[random_link]

        second_request = requests.get(link["href"])
        soup2 = BeautifulSoup(second_request.content, "html.parser")
        img_tag = soup2.find(id="wallpaper")
        wallpaper_src = img_tag["src"]

        # Download image

        wallpaper = requests.get(wallpaper_src)
        if "+" in category:
            category = category.replace("+", "-")

        if not "Wallpapers" in os.listdir():
            os.mkdir("Wallpapers")

        open(f"{category}.jpg", "wb").write(wallpaper.content)
        random_id = str(uuid.uuid4()).rsplit("-")[-1]
        os.rename(f"{category}.jpg", f"Wallpapers/{category}-{random_id}.jpg")
        print(
            colorama.Back.MAGENTA,
            (f"{category}-{random_id}.jpg save in the Wallpapers folder."),
            colorama.Style.RESET_ALL,
        )
