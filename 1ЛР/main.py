# Importing packages bs4 and requests, input url
from bs4 import BeautifulSoup
import requests
def get_page():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    page = requests.get(url)
    # Getting code from page
    soup = BeautifulSoup(page.text, "html.parser")
    all_films = soup.findAll('td', class_='titleColumn')
    all_rating = soup.findAll('td', class_='ratingColumn imdbRating')
    return all_films, all_rating
def imdb_parser_name():
    all_films, all_rating = get_page()
    filtered_films = []
    # Getting text from tag "a"
    for data in all_films:
        if data.find('a') is not None:
            filtered_films.append(data.text)
    all_films.clear()
    for data in filtered_films:
        filtered = data[16:]
        data = filtered[:-8]
        all_films.append(data)
    return all_films
def imdb_parser_rating():
    all_films, all_rating = get_page()
    filtered_films = []
    # Getting film rating from tag "tb"
    for data in all_rating:
        if data.find('strong') is not None:
            filtered_films.append(data.text)
    all_rating.clear()
    for data in filtered_films:
        filtered = data[1:4]
        all_rating.append(filtered)
    return all_rating
def main():
    all_films = imdb_parser_name()
    all_rating = imdb_parser_rating()
    # Joining two dictionaries
    result_dictionary = dict(zip(all_films, all_rating))
    print(result_dictionary)
if __name__ == "__main__":
    main()