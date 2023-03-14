from bs4 import BeautifulSoup
import requests

URL = "https://www.businessinsider.com/best-horror-movies-all-time-critics-2018-6"
response = requests.get(URL)
horror_page = response.text

soup = BeautifulSoup(horror_page, "html.parser")

all_titles = soup.find_all("h2", class_="slide-title-text")
titles = [title.getText() for title in all_titles]
movies = titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

